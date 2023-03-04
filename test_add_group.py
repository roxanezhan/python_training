# этот скрипт пишет разработчик по тестам

# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


# если написать "@pytest.fixture", то наша функция из простой функции превращается в фикстуру
@pytest.fixture
def app():
    fixture = Application()
    request.addfinalyzer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="testgroup", header="testheader", footer="testfooter"))
    app.logout(wd)

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout(wd)

if __name__ == "__main__":
    unittest.main()
