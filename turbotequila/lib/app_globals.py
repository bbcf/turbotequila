# -*- coding: utf-8 -*-

"""The application's Globals object"""

__all__ = ['Globals']


class Globals(object):
    """Container for objects available throughout the life of the application.

    One instance of Globals is created during application initialization and
    is available during requests via the 'app_globals' variable.

    """

    def __init__(self):
        '''
        @param tmp_pkg : the temporary directory in GDV as a package name
        @param tmp_user : the name of a temporary user
        '''
        self.tmp_pkg = 'turbotequila.data.tmp'
        self.tmp_user_name = 'tmp_user'
        
        '''
        Default groups and permissions
        '''
        self.group_admins = 'Admins'
        self.group_users = 'Users'
        self.perm_read = 'read'
        self.perm_admin = 'admin'