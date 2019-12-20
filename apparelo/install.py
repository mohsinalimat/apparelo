from __future__ import print_function, unicode_literals

import frappe
from frappe import _
from frappe.desk.page.setup_wizard.setup_wizard import add_all_roles_to
from frappe.custom.doctype.custom_field.custom_field import create_custom_field
from apparelo.apparelo.doctype.knitting import knitting
from apparelo.apparelo.doctype.dyeing import dyeing
from apparelo.apparelo.doctype.bleaching import bleaching
from apparelo.apparelo.doctype.compacting import compacting
from apparelo.apparelo.doctype.steaming import steaming
from apparelo.apparelo.doctype.cutting import cutting
from apparelo.apparelo.doctype.piece_printing import piece_printing
from apparelo.apparelo.doctype.stitching import stitching
from apparelo.apparelo.doctype.label_fusing import label_fusing
from apparelo.apparelo.doctype.checking import checking
from apparelo.apparelo.doctype.ironing import ironing
from apparelo.apparelo.doctype.packing import packing


def after_install():
    create_item_attributes()
    create_item_template()

def create_item_attributes():
    knitting.create_item_attribute()
    dyeing.create_item_attribute()
    cutting.create_item_attribute()

def create_item_template():
    knitting.create_item_template()
    dyeing.create_item_template()
    bleaching.create_item_template()
    compacting.create_item_template()
    steaming.create_item_template()
    cutting.create_item_template()
    piece_printing.create_item_template()
    stitching.create_item_template()
    label_fusing.create_item_template()
    checking.create_item_template()
    ironing.create_item_template()
    packing.create_item_template()

