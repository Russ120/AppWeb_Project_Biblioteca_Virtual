from werkzeug.security import check_password_hash, generate_password_hash

#esto es para que el objeto user tenga el atributo is_activate para saber si está activo, para esto ponemos a la clase User a heredar de UserMixin
from flask_login import UserMixin


class User(UserMixin):
    {
    #constructor de esta clase basicamente el obtiene los parametros e iguala las prop de la cla
    }
    def __init__(self, id, username, password,email="", fullname="") -> None:
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.fullname = fullname

    {
    #class method es para que el metodo se pueda invocar sin instancear la clase
    #este metodo lo que hace es
        #hashed_password es la contraseña que se guarda en la bd ya cambiada o asegurada
}
    
    
    @classmethod
    def check_password(cls,hashed_password,password):
        try:
            return check_password_hash(hashed_password, password)
        except Exception as e:
            print(f"Error al verificar la contraseña: {e}")
            return False
    
    @classmethod
    def generate_password(cls,password):
        try:
                return generate_password_hash(password, method='pbkdf2:sha256')
        except Exception as e:
                print(f"Error al generar la contraseña: {e}")
                return False

        # return generate_password_hash(password)

