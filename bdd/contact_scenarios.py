
import pytest
from pytest_bdd import scenario
from .contact_steps import *

from datagen.contact import testdata_for_modifying as testdata_for_edit


@scenario('contacts.feature', 'Add new contact')
def test_add_new_contact():
    pass


@scenario('contacts.feature', 'Delete a contact')
def test_delete_contact():
    pass


@pytest.mark.parametrize("contact_with_new_params", testdata_for_edit, ids=[repr(x) for x in testdata_for_edit])
@scenario('contacts.feature', 'Modify a contact')
def test_edit_contact(contact_with_new_params):
    pass
