import pytest
from fixture.application import Application

# если написать "@pytest.fixture", то наша функция из простой функции превращается в фикстуру
@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    fixture.session.login(username="admin", password="secret")
    def fin():
        fixture.session.logout()
        (fixture.destroy)
    request.addfinalizer(fin)
    return fixture