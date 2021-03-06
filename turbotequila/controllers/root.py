# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, request

from turbotequila.lib.base import BaseController
from turbotequila.model import DBSession
from repoze.what.predicates import has_permission



from turbotequila.controllers import ErrorController, LoginController, GroupController
from turbotequila.controllers import PermissionController, UserController, AdminController


 
__all__ = ['RootController']


import inspect
from sqlalchemy.orm import class_mapper

import turbotequila.model.auth
models = {}
for m in turbotequila.model.auth.__all__:
    m = getattr(turbotequila.model.auth, m)
    if not inspect.isclass(m):
        continue
    try:
        mapper = class_mapper(m)
        models[m.__name__.lower()] = m
    except:
        pass


class RootController(BaseController):
    """
    The root controller for the turbotequila application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """
    
   
    error = ErrorController()
    login = LoginController()
    

    groups = GroupController(DBSession, menu_items=models)
    permissions = PermissionController(DBSession, menu_items=models)
    users = UserController(DBSession, menu_items=models)

    admin = AdminController()


    @expose('turbotequila.templates.index')
    def index(self,*args,**kw):
        return dict(page='index')
    
    @expose('turbotequila.templates.index')
    def login_needed(self):
        flash('You need to login', 'error')
        return dict(page='index')

    @expose('turbotequila.templates.about')
    def about(self):
        """Handle the 'about' page."""
        return dict(page='about')


    
    
    
    
    
    ## DEVELOPMENT PAGES ##
    
    @require(has_permission('admin', msg='Only for admins'))
    @expose('turbotequila.templates.environ')
    def environ(self):
        """This method showcases TG's access to the wsgi environment."""
        return dict(page='environ',environment=request.environ)

    @require(has_permission('admin', msg='Only for admins'))
    @expose('turbotequila.templates.data')
    @expose('json')
    def data(self, **kw):
        """This method showcases how you can use the same controller for a data page and a display page"""
        return dict(page='data',params=kw)


    
    
    
