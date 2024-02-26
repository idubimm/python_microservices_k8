# server.py

import datetime,os
# --------------------------------------------------------
#             #########  SYS_HACK #########              #  
# --------------------------------------------------------
#  this way I load the module from any folder below src  #
# --------------------------------------------------------

import sys
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)

#             #########  SYS_HACK #########              #
from configuration import config
# --------------------------------------------------------


import jwt
from flask import Flask,request
from flask_mysqldb import MySQL





conobj = config.ConfigSingleton()
conobj.loadModuleConfiguration('auth')  # Load auth.ini
username = conobj.auth.DB.USER_NAME
password = conobj.auth.DB.PASSWORD

conobj.loadModuleConfiguration('orders')  # Load auth.ini

print(f'username : {username} , password :{password} {conobj.orders.BONUS.AmouNt}')
username = conobj.auth.DB.USER_NAME2
print(f'username : {username} ')
conobj.loadModuleConfiguration('auth')  # Load auth.ini
username = conobj.auth.DB.USER_NAME3
print(f'username : {username} ')











 