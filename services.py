import jaydebeapi
import os
from dotenv import load_dotenv

load_dotenv()


DEFAULT_DB_NAME=os.getenv('DEFAULT_DB_NAME')
DEFAULT_DB_USER=os.getenv('DEFAULT_DB_USER')
DEFAULT_DB_PASSWORD=os.getenv('DEFAULT_DB_PASSWORD')
DEFAULT_DB_HOST=os.getenv('DEFAULT_DB_HOST')
DEFAULT_DB_PORT=os.getenv('DEFAULT_DB_PORT')
JDBC_DRIVER_NAME = "org.postgresql.Driver"

def create_connect_jdbc():

    # jdbc_driver_loc = os.path.join('postgresql-42.5.1')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    jdbc_driver_loc =  os.path.dirname(os.path.realpath(__file__)) + '/' + 'postgresql-42.5.1.jar'
    print(jdbc_driver_loc)
    sql_str = "select version()"

    connection_string = 'jdbc:postgresql://' + DEFAULT_DB_HOST + ':' + DEFAULT_DB_PORT + '/' + DEFAULT_DB_NAME

    # url = '{0}:user={1};password={2}'.format(connection_string, DEFAULT_DB_USER, DEFAULT_DB_PASSWORD)
    print("Connection String: " + connection_string)

    conn = jaydebeapi.connect(JDBC_DRIVER_NAME, connection_string, { 'user': DEFAULT_DB_USER, 'password': DEFAULT_DB_PASSWORD },
                              jdbc_driver_loc)
    curs = conn.cursor()
    return curs


def excute_model(curs):
    curs.execute('CREATE TABLE IF NOT EXISTS Roles(role_id SERIAL PRIMARY KEY,role_name VARCHAR(50)  NOT NULL)')
    curs.execute('CREATE TABLE IF NOT EXISTS Users(user_id SERIAL PRIMARY KEY,user_name VARCHAR(50)  NOT NULL, '
    'role_id INT, '
    'CONSTRAINT fk_user FOREIGN KEY(role_id)  REFERENCES Roles(role_id))')


# def export_metada():
#     from sqlalchemy import MetaData, create_engine

