import json
from flask import jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from configparser import ConfigParser
from mysql.connector import connection
import mysql.connector
    
config = ConfigParser()
config.read('config.ini')

user = config['mysql']['user']
password = config['mysql']['password']
host = config['mysql']['host']
database = config['mysql']['database']
conn_str = f'mysql://{user}:{password}@{host}/{database}'

engine = create_engine(conn_str, echo=True)
session_maker = sessionmaker(engine)

mysql_config = {
  'user': user,
  'password': password,
  'host': host,
  'database': database,
  'raise_on_warnings': True
}
