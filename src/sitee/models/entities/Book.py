#esto es para que el objeto user tenga el atributo is_activate para saber si está activo, para esto ponemos a la clase User a heredar de UserMixin
import datetime
from flask_login import UserMixin




class Book(UserMixin):
    {
    #constructor de esta clase basicamente el obtiene los parametros e iguala las prop de la cla
    }
    def __init__(self, id = 0, titulo = "", autor = "", editorial = "", año ="", descripcion = '', imagen='', url='', categoria="", user_id = 0) -> None:
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.año = año
        self.descripcion = descripcion
        self.imagen = imagen
        self.url = url
        self.categoria = categoria
        self.user_id = user_id

    {
    #class method es para que el metodo se pueda invocar sin instancear la clase
    #este metodo lo que hace es
        #hashed_password es la contraseña que se guarda en la bd ya cambiada o asegurada
}
    

    