import re

import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from test_data.login_data import INVALID_LOGIN_CASES


@pytest.mark.smoke
def test_successful_login(
    login_page: LoginPage,
    page: Page,
    login_credentials: dict[str, str],
) -> None:
    # Arrange: open the login page.
    login_page.open()

    # login_page.login("standard_user", "secret_sauce")
    # passing the credentials through environment variables , here through terminal($env:TEST_USERNAME = "standard_user")
    login_page.login(
        login_credentials["username"],
        login_credentials["password"],
    )

    # Assert: verify successful navigation and visible page content.
    expect(page).to_have_url(re.compile(r"/inventory\.html$"))
    expect(page.locator('[data-test="title"]')).to_have_text("Products")


@pytest.mark.negative
@pytest.mark.parametrize(
    "username, password, expected_error",
    INVALID_LOGIN_CASES,
)
def test_login_shows_expected_error(
    login_page: LoginPage,
    username: str,
    password: str,
    expected_error: str,
) -> None:
    # Arrange: open the login page.
    login_page.open()

    # Act: attempt login using the current dataset.
    login_page.login(username, password)

    # Assert: verify the expected error message.
    expect(login_page.error_message).to_have_text(
        expected_error,
        timeout=10000,
    )
