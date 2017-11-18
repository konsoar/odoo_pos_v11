# -*- coding: utf-8 -*-
from dotop.tools import safe_eval, html_escape as escape

from . import fields
from . import assetsbundle

from .assetsbundle import AssetsBundle
from .qweb import unicodifier, QWebException
from .ir_qweb import IrQWeb, QWeb
