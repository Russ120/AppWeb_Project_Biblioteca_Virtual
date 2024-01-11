from flask import Flask, url_for, redirect, render_template
from flask_login import LoginManager
from user.models.ModelUser import ModelUser
from sitee.models.ModelBook import ModelBook
import database.conexion as db

#Config
from app.config import Config, configDic

#esto es para proteger cuando un formulario no autentificado intenta hacer peticiones al servidor para evitar el Cross-site request forgery o CSRF
from flask_wtf.csrf import CSRFProtect

#importando bleuprints
from sitee.BookRoute import site_blueprint
from user.UserRoute import user_blueprint



def status_401(error):
    return redirect(url_for('user.login'))
def status_404(error):
    return render_template('errors/status_404.html'), 404


#instanceando el protector de Cross-site request forgery
csrf = CSRFProtect()

app = Flask(__name__)

login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)





def create_app():
    
    app.config.from_object(configDic['development'])
    app.secret_key = Config.SECRET_KEY

    csrf.init_app(app)
    app.register_error_handler(401,status_401)
    app.register_error_handler(404,status_404)
    
    
    # app.register_blueprint(blog)
    app.register_blueprint(user_blueprint, url_prefix='/user')
    app.register_blueprint(site_blueprint, url_prefix='/site')

    return app
