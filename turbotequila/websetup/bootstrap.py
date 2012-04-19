# -*- coding: utf-8 -*-
"""Setup the turbotequila application"""

from turbotequila import model
from turbotequila.lib import constants
from sqlalchemy.exc import IntegrityError
import transaction

group_admins = 'Admins'
perm_admin = 'admin'

group_users = 'Users'
perm_user = 'user'

def bootstrap(command, conf, vars):
    """Place any commands to setup turbotequila here.
    Note that you will have to log in the application one before launching the bootstrap."""
    try:
        print 'Adding groups and permissions'

        # ADMIN GROUP
        admins = model.Group()
        admins.name = constants.group_admins_name
        admins.id = constants.group_admins_id
        model.DBSession.add(admins)

        # ADMIN PERMISSION
        perm = model.Permission()
        perm.name = constants.permission_admin_name
        perm.description = constants.permission_admin_desc
        perm.groups.append(admins)
        model.DBSession.add(perm)

        # USER GROUP
        users = model.Group()
        users.name = constants.group_users_name
        users.id = constants.group_users_id
        model.DBSession.add(users)

        # READ PERMISSION
        read = model.Permission()
        read.name = constants.permissions_read_name
        read.description = constants.permission_read_desc
        read.groups.append(users)
        model.DBSession.add(read)
        transaction.commit()

           
    except IntegrityError:
        print 'Warning, there was a problem adding your auth data, it may have already been added:'
        import traceback
        print traceback.format_exc()
        transaction.abort()
        print 'Ending with bootstrapping...'
        
        
        
    