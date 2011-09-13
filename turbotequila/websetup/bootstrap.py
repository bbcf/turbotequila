# -*- coding: utf-8 -*-
"""Setup the turbotequila application"""

from turbotequila import model
from sqlalchemy.exc import IntegrityError
import transaction
from tg import app_globals as gl

def bootstrap(command, conf, vars):
    """Place any commands to setup turbotequila here.
    Note that you will have to log in the application one before launching the bootstrap."""
    try:
        # admin
        #admin = model.DBSession.query(model.User).filter(model.User.email == 'your_email_on_tequila@your_university.ch').first()
        admin = model.DBSession.query(model.User).filter(model.User.email == 'yohan.jarosz@epfl.ch').first()

        if admin:
            print 'Adding default groups and permissions'
            # ADMIN GROUP
            admins = model.Group()
            admins.name = gl.group_admins
            admins.users.append(admin)
            model.DBSession.add(admins)
        
            # ADMIN PERMISSION
            perm = model.Permission()
            perm.name = gl.perm_admin
            perm.description = u'This permission give admin right to the bearer'
            perm.groups.append(admins)
            model.DBSession.add(perm)
            transaction.commit()
            
             # ADMIN GROUP
            users = model.Group()
            users.name = gl.group_users
            users.users.append(admin)
            model.DBSession.add(users)
            
            # READ PERMISSION
            read = model.Permission()
            read.name = gl.perm_read
            read.description = u'This permission give "read" right to the bearer'
            read.groups.append(users)
            model.DBSession.add(read)
            
        
            transaction.commit()
        else :
            print '''
                    
                    Change email value in " turbotequila.websetup.bootstrap.py ".
                    Launch " paster serve --reload development.ini ".
                    Log in the application.
                    Re-run "python setup-app development.ini". 
                    It will gives you admin rights.
                    
                  '''
           
    except IntegrityError:
        print 'Warning, there was a problem adding your auth data, it may have already been added:'
        import traceback
        print traceback.format_exc()
        transaction.abort()
        print 'Ending with bootstrapping...'
        
        
        
    