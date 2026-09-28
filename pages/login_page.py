from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        # Locators
        self.username_input = page.get_by_placeholder(
            "Username",
            exact=True,
        )
        self.password_input = page.get_by_placeholder(
            "Password",
            exact=True,
        )
        self.login_button = page.get_by_role(
            "button",
            name="Login",
            exact=True,
        )
        self.error_message = page.locator('[data-test="error"]')

    def open(self) -> None:
        self.page.goto("/")

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        