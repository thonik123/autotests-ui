import pytest


@pytest.mark.smoke
def test_somoke_case():
    ...

@pytest.mark.regression
def test_regression_case():
    ...

@pytest.mark.smoke
@pytest.mark.regression
class TestSuite:
    @pytest.mark.smoke
    def test_case1(self):
        ...

    def test_case2(self):
        ...

@pytest.mark.regression
class TestUserAuthentication:
    @pytest.mark.smoke
    def test_login(self):
        ...

    @pytest.mark.slow
    def test_password_reset(self):
        ...
    def test_logout(self):
        ...

