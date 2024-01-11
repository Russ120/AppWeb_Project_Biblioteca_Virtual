from flask import Flask, Blueprint, url_for
from flask import render_template, request, redirect, send_from_directory
from flask_login import current_user, login_required
import os
from sitee.models.ModelBook import ModelBook
from sitee.models.entities.Book import Book
from database import conexion as db
from flask_wtf.csrf import CSRFProtect

from user.models.ModelUser import ModelUser




app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

site_blueprint = Blueprint('sitee', __name__,template_folder='templates', static_folder='staticc')


# Metodos para buscar


@site_blueprint.route('/libro/search', methods=["POST"])
@login_required
def search_book():
    parametro = request.form['txtSearch']

    if parametro != "":
        Lista_libros = ModelBook.search_books(db, parametro)
        print(parametro)

        return render_template('sitio/libros.html', libros = Lista_libros)
    else:
        return redirect("/site/libros")
    



@site_blueprint.route('/admin/libros/search', methods=["POST"])
@login_required
def search_admin_book():
    parametro = request.form['txtAdminSearch']

    if parametro != "":
        LoggedUser = ModelUser.get_user_from_username(db, current_user.username)
        print(LoggedUser.id)

        Lista_libros = ModelBook.search_books(db, parametro, LoggedUser.id)
        print(parametro)

        return render_template('admin/ADlibros.html', libros = Lista_libros)
    else:
        return redirect("/site/admin/libros")

    


@site_blueprint.route('/libros/search/category/<categoria>')
@login_required
def search_by_category(categoria):

    if categoria != "":
        if categoria == "Todas":
            return redirect("/site/libros")
        else:
            Lista_libros = ModelBook.search_by_category(categoria, db)

            return render_template('sitio/libros.html', libros = Lista_libros)
    else:
        return redirect("/site/libros")















#metodos de añadir libros-------------------------------------------------


@site_blueprint.route('/libro/añadir')
@login_required
def añadir():
    return render_template('admin/ADañadir.html')


#ingresar un libro
@site_blueprint.route('/admin/libros/guardar', methods=['POST'])
@login_required
def admin_libros_guardar():

    # _LoggedUser = request.form["txtLoggedUsername"]
    _nombre = request.form['txtNombreLibro']
    _url = request.form['txtURL']
    _archivo = request.files['txtImagen']
    _autor = request.form['txtAutorLibro']
    _editorial =request.form['txtEditorial']
    _año =request.form['txtAño']
    _descripcion =request.form['txtDescripcion']
    _categoria = request.form.get('txtCategorias')



    #conseguir el id del usuario que esta logueado mediante su username
    LoggedUser = ModelUser.get_user_from_username(db, current_user.username)


    if _archivo.filename != "":
        nuevoNombre = ModelBook.save_rename_img(_archivo)


    Libro = Book(titulo=_nombre,autor=_autor,editorial=_editorial,año=_año,descripcion=_descripcion,imagen=nuevoNombre,url=_url, categoria=_categoria, user_id =LoggedUser.id)
    ModelBook.save(Libro,db)

    return redirect('/site/admin/libros')






#metodos de eliminar libros-------------------------------------------------


#Eliminar Libro
@site_blueprint.route("/admin/libros/borrar",methods=["POST"])
@login_required
def admin_libros_borrar():
    
    _id = request.form["txtID"]
    
    if _id != "":
    #Primero eliminamos la imagen del archivo
        libro = ModelBook.get_by_id(_id, db)
        ModelBook.delete_img(libro)
        
        ModelBook.delete(_id, db)

        return redirect('/site/admin/libros')






#metodos de editar libros-------------------------------------------------
    

@site_blueprint.route('/admin/libros/editar', methods=['POST'])
@login_required
def admin_libros_editar():
    _id = request.form["txtIDedit"]

    libro = ModelBook.get_by_id(_id, db)


    return render_template('admin/ADeditar.html', libro = libro )







#actualizar un libro
@site_blueprint.route('/admin/libros/actualizar', methods=['POST'])
@login_required
def admin_libros_actualizar():
    
    _id = request.form["txtID"]
    _nombre = request.form['txtNombreLibro']
    _url = request.form['txtURL']
    _archivo = request.files['txtImagen']
    _autor = request.form['txtAutorLibro']
    _editorial =request.form['txtEditorial']
    _año =request.form['txtAño']
    _descripcion =request.form['txtDescripcion']
    _categoria = request.form.get('txtCategorias')


    #si ingreso una imagen
    if _archivo.filename != "":
        libro = ModelBook.get_by_id(_id, db)

        #si existia la borre y se crea de nuevo sino pues simplemente se crea un nombre
        nuevoNombre = ModelBook.update_img(libro,_archivo)

        Libro = Book(id=_id,titulo=_nombre,autor=_autor,editorial=_editorial,año=_año,descripcion=_descripcion,imagen= nuevoNombre,url=_url, categoria=_categoria)
        ModelBook.update(Libro, db)

    
    else:
        Libro = Book(id=_id,titulo=_nombre,autor=_autor,editorial=_editorial,año=_año,descripcion=_descripcion,url=_url,categoria=_categoria)
        ModelBook.update(Libro, db)
        
    return redirect('/site/admin/libros')





#metodos de obtener todos los libros -------------------------------------------------


#obtener todos los libros
@site_blueprint.route('/libros')
@login_required
def libros():
    
    Lista_libros = ModelBook.get_all_books(db)
    return render_template('sitio/libros.html', libros = Lista_libros )


#obtener todos los libros para admin
@site_blueprint.route('/admin/libros')
@login_required
def admin_libros():
    LoggedUser = ModelUser.get_user_from_username(db, current_user.username)

    Lista_libros = ModelBook.get_all_books(db, LoggedUser.id)

    return render_template('admin/ADlibros.html', libros = Lista_libros)




#metodos de obtener las vistas del inicio o index -------------------------------------------------


@site_blueprint.route('/')
@login_required
def inicio():
    return render_template('sitio/index.html')


@site_blueprint.route('/admin')
def admin_index():
    return render_template('admin/ADindex.html')




#metodo para mostrar imagen que se reciba-------------------------------------------------

#Mostrar imagen
@site_blueprint.route("/img/<imagen>")
@login_required
def imagenes(imagen):
    directorio = os.path.join(os.getcwd(), "src", "sitee", "staticc", "img")

    return send_from_directory(directorio, imagen)




#metodo para mandarle el libro del cual se quiere obtener mas informacion------------------------------------------------

@site_blueprint.route('/informacion/<id>',methods=["POST","GET"])
@login_required
def info_libro(id):

    libros = ModelBook.get_by_id(id, db)

    return render_template('Sitio/infoLibro.html', libro= libros[0])












#metodos de obtener diferentes vistas -------------------------------------------------


@site_blueprint.route('/nosotros')
@login_required
def nosotros():
    return render_template('sitio/nosotros.html')


@site_blueprint.route("/epa")
def epa():
    return render_template('admin/index.html')





