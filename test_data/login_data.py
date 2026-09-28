import pytest


INVALID_LOGIN_CASES = [
    pytest.param(
        "locked_out_user",
        "secret_sauce",
        "Epic sadface: Sorry, this user has been locked out.",
        id="locked-user",
    ),
    pytest.param(
        "standard_user",
        "wrong_password",
        "Epic sadface: Username and password do not match any user in this service",
        id="wrong-password",
    ),
    pytest.param(
        "",
        "secret_sauce",
        "Epic sadface: Username is required",
        id="empty-username",
    ),
]