from playwright.sync_api import Page,expect


def test_successful_login(page: Page):
    page.goto("https://www.saucedemo.com")
    # page.pause()
    expect(page).to_have_title("Swag Labs")
    username_input=page.get_by_placeholder("Username")
    password_input=page.get_by_placeholder("password")
    login_button=page.get_by_role("button",name="Login")
    username_input.fill("standard_user")
    password_input.fill("secret_sauce")
    login_button.click()
    products_title=page.get_by_text("Products",exact=True)
    expect(products_title).to_be_visible()
    # page.pause()


def test_locked_out_user_cannot_login(page:Page):
        page.goto("https://www.saucedemo.com")
        page.get_by_placeholder("Username").fill("locked_out_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button",name="Login").click()
        error_message = page.get_by_text("Epic sadface: Sorry, this user has been locked out.")
        expect(error_message).to_be_visible()