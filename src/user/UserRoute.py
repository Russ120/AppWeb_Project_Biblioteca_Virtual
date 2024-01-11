from flask import Flask, render_template,request, redirect, url_for, flash, Blueprint

#imports del login, manejar su logueado, requerir que esté logueado, almacenar un logueado y cerrar el logueado
from flask_login import LoginManager, login_user, logout_user, login_required
# Database
import database.conexion as db
# Models
from user.models.ModelUser import ModelUser
# Entities
from user.models.entities.User import User



app = Flask(__name__)


user_blueprint = Blueprint('user', __name__,template_folder='templates', static_folder='static')


#instanceando el manejador de logueos
login_manager_app = LoginManager(user_blueprint)


#este es un metodo que se tiene que crear para poder obyener todos los datos del usuario logueado osea que acaba de iniciar session
#el usuario loggeado se almacenó en la funcion login user al momento de confirmar que la contraseña es correcta
#cargar info del usuario logueado
@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)



@user_blueprint.route('/')
def index():
    # el url_for('login') lo que hace es que trae la url de el metodo que le digas en este caso es el login arriba esta
    # redireigiendo a la ruta que ejecuta el login osea /login por eso ese metodo tambien es get
    return redirect(url_for('user.login'))



#Acceder
@user_blueprint.route('/login', methods=['GET','POST'])
def login():

    #si el form mando un metodo post
    if request.method=='POST':

        user = User(0, request.form['txtUser'], request.form['txtPassword'] )

        #esta variable aunque no lo parezca es el usuario encontrado,
        # si se encontro el usuario tiene los datos de el y un booleano que es true si la contraseña es correcta y si no pues false
        # pero si no se encuentra retorna None
        logged_user = ModelUser.login(db,user)


        #aqui revisa que si se haya encontrado
        if logged_user != None:

            #aqui revisa si la contraseña es true osea si es correcta
            if logged_user.password:

                #almacenando el usuario logeado
                login_user(logged_user)
                return redirect(url_for('sitee.admin_index'))

            #si no es correcta te deja en login
            else:
                # return redirect(url_for('home'))
                flash("Contraseña invalida ...")
                return render_template('auth/login.html')
            
            #.\templates\auth\login.html

        #si no se encontro te dice eso y te deja en login
        else:
            flash("Usuario no encontrado ...")
            return render_template('auth/login.html')
            
    #si no es post pues no ingreso nada asi que se requiere un get y devuelve la plantilla de login
    else:
        return render_template('auth/login.html')
        #return render_template('auth/login.html')





#Cerrar
# @user_blueprint.route('/logout')
# def logout():
#     logout_user()
    
#     return redirect(url_for('user.login'))

# Logout
@user_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user.login'))




#Crear cuenta
@user_blueprint.route('/signin',methods=['GET','POST'])
def signin():
        #si el form mando un metodo post
    if request.method=='POST':

        user = User(0, request.form['txtUser'], request.form['txtPassword'],request.form['txtEmail'],request.form['txtFullname'] )

        existe = ModelUser.user_exist(db, user)

        if existe:
            flash("El nombre de usuario ya existe.")
            return render_template('auth/signin.html')
        
        else:
            registered = ModelUser.signin(db,user)

            if registered:
                return redirect(url_for('user.login'))
                
            #si no se encontro te dice eso y te deja en login
            else:
                flash("user could not be registered ...")
                return render_template('auth/signin.html')
            
    #si no es post pues no ingreso nada asi que se requiere un get y devuelve la plantilla de login
    else:
        return render_template('auth/signin.html')




@user_blueprint.route("/home")
@login_required
def home():
    return render_template('auth/home.html')


@user_blueprint.route("/protected")
@login_required
def protected():
    return render_template('errors/status_404.html')

