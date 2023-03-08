import pytest
from fixture.application import Application

# если написать "@pytest.fixture", то наша функция из простой функции превращается в фикстуру
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture