# -*- coding: utf-8 -*-
import importlib
import json
import jsonpickle
import os.path

import pytest

from fixture.application import Application
from fixture.db import DbFixture
from fixture.orm import ORMFixture

fixture = None
target = None


# @py# test.fixture(scope="session")
@pytest.fixture
def app(request):
    global fixture
    global target

    browser = request.config.getoption("--browser")

    web_config = load_config(request.config.getoption("--target"))['web']

    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])

    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])

    return fixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'],
                          user=db_config['user'], password=db_config['password'])

    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)

    return dbfixture


@pytest.fixture(scope="session")
def orm(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    ormfixture = ORMFixture(host=db_config['host'], name=db_config['name'],
                            user=db_config['user'], password=db_config['password'])

    def fin():
        ormfixture.destroy()
    request.addfinalizer(fin)

    return ormfixture


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as config:
            target = json.load(config)
    return target


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")


def pytest_generate_tests(metafunc):
    for fxt in metafunc.fixturenames:
        if fxt.startswith("data_"):
            testdata = load_from_module(fxt[5:])
            metafunc.parametrize(fxt, testdata, ids=[str(i) for i in testdata])
        if fxt.startswith("json_"):
            testdata = load_from_json(fxt[5:])
            metafunc.parametrize(fxt, testdata, ids=[str(i) for i in testdata])


def load_from_module(module):
    return importlib.import_module("data.static_%s" % module).testdata


def load_from_json(module):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "data/%s.json" % module)) \
            as data_source:
        return jsonpickle.decode(data_source.read())
