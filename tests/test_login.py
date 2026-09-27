from playwright.sync_api import Page,expect
from pages.login_page import LoginPage


def test_successful_login(page:Page):
    login_page=LoginPage(page)
    login_page.open()
    login_page.login("standard_user","secret_sauce")
    products_title=page.get_by_text("Products",exact=True)
    expect(products_title).to_be_visible
    

def test_locked_out_user_cannot_login(page:Page):
    login_page=LoginPage(page)
    login_page.open()
    login_page.login("locked_out_user","secret_sauce")
    expect(login_page.error_message).to_contain_text("Sorry, this user has been locked out.")
      
     