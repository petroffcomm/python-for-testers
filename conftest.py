# -*- coding: utf-8 -*-
import pytest
import json, jsonpickle
import os.path
import importlib

from fixture.application import Application

fixture = None
target = None


# @py# test.fixture(scope="session")
@pytest.fixture
def app(request):
    global fixture
    global target

    browser = request.config.getoption("--browser")

    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   request.config.getoption("--target"))
        with open(config_file) as config:
            target = json.load(config)

    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])

    fixture.session.ensure_login(username=target['username'], password=target['password'])

    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")


def pytest_generate_tests(metafunc):
    for fxt in metafunc.fixturenames:
        if fxt.startswith("data_"):
            testdata = load_from_module(fxt[5:])
            metafunc.parametrize(fxt, testdata, ids=[str(i) for i in testdata])
        if fxt.startswith("json_"):
            testdata = load_from_json(fxt[5:])
            metafunc.parametrize(fxt, testdata, ids=[str(i) for i in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(module):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "data/%s.json" % module)) \
            as data_source:
        return jsonpickle.decode(data_source.read())