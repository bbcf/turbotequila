# -*- coding: utf-8 -*-
"""Error controller"""
from tg import request, expose
from turbotequila.lib.base import BaseController
from turbotequila.lib import constants
from turbotequila import model
from repoze.what.predicates import has_permission

__all__ = ['AdminController']


class AdminController(BaseController):
    allow_only = has_permission(constants.permission_admin_name)

    @expose('turbotequila.templates.admin')
    def index(self, *args, **kw):
        return {'page' : 'admin', 'admin_items' : [m.lower() for m in model.admin_models]}
