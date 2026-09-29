import os

import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def login_credentials() -> dict[str, str]:
    username = os.getenv("TEST_USERNAME")
    password = os.getenv("TEST_PASSWORD")
    if not username or not password:
        pytest.fail(
            "Set TEST_USERNAME and TEST_PASSWORD before running login tests.",
            pytrace=False,
        )
    return {
        "username": username,
        "password": password,
    }
