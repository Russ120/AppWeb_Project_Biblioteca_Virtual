import pyodbc
from flask import Flask
from app.config import DevelopmentConfig

app = Flask(__name__)


# app.secret_key = Config.SECRET_KEY
app.config['SQL_SERVER_DRIVER'] = DevelopmentConfig.DRIVER
app.config['SQL_SERVER_SERVER'] = DevelopmentConfig.SERVER
app.config['SQL_SERVER_DATABASE'] = DevelopmentConfig.DATABASE
app.config['SQL_SERVER_UID'] = DevelopmentConfig.USERNAME
app.config['SQL_SERVER_PWD'] = DevelopmentConfig.PASSWORD

def obtener_conexion():
    try:
        connection = pyodbc.connect(
            f"DRIVER={{{app.config['SQL_SERVER_DRIVER']}}};SERVER={app.config['SQL_SERVER_SERVER']};DATABASE={app.config['SQL_SERVER_DATABASE']};UID={app.config['SQL_SERVER_UID']};PWD={app.config['SQL_SERVER_PWD']}"
        )
        print("Conexión exitosa")
        return connection
    except Exception as ex:
        print(ex)