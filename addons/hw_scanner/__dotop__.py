# -*- coding: utf-8 -*-
# Part of dotop. See LICENSE file for full copyright and licensing details.

{
    'name': 'Barcode Scanner Hardware Driver',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'Hardware Driver for Barcode Scanners',
    'website': 'http://www.dotopyun.com',
    'description': """
Barcode Scanner Hardware Driver
================================

This module allows the web client to access a remotely installed barcode
scanner, and is used by the posbox to provide barcode scanner support to the
point of sale module. 

""",
    'depends': ['hw_proxy'],
    'external_dependencies': {'python': ['evdev']},
}
