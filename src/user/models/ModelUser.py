from user.models.entities.User import User
from werkzeug.security import check_password_hash, generate_password_hash

class ModelUser():



    @classmethod
    def login(cls,db,user):
        try:
            conection = db.obtener_conexion()
            cursor = conection.cursor()

            sql = """select id, username, password, email, fullname from [dbo].[user]
                        where username = '{}'""".format(user.username)
            cursor.execute(sql)
            row = cursor.fetchone()
            cursor.commit()
            
            print(row)
            #si se encontro registro
            if row != None:
                #BOOL
                {
                    # aqui se le manda la contraseña hasheada osea asegurada recuerda que esto es revisar si existe de por si en el crear se hasheó
                    # por eso el metodo check recibe la asegurada y la real por que las compara si deshasheada son iguales devuelve true
                    # entonces esa variable es un booleano,
                    # si la contraseña del registro que tiene el mismo usuario que el que se ingreso en el form osea el que se busco ahora mismo arriba
                    # si esa contraseña deshasheada es igual a la contraseña que se ingreso en el form pues esta variable será true no pues false
                }
                try:
                    password = User.check_password(row[2], user.password)
                    #password = check_password_hash(row[2],user.password)
                    
                    #aqui le asignamos la info del registro encontrado y la contraseña revisada a un onjeto de la clase user el tiene todos los datos
                    user = User(row[0],row[1], password ,row[3],row[4])

                    # y este user con los datos es lo que se retorna

                    return user
                
                except Exception as e:
                    print(f"Error metodo login: {e}")
                    return False

            #si no se encontro registro
            else:
                return None
            
        except Exception as ex:
            raise Exception(ex)
        



    @classmethod
    def signin(cls, db,user):

        password = user.generate_password(user.password)

        try:
            conection = db.obtener_conexion()
            cursor = conection.cursor()

            sql = """INSERT INTO [dbo].[user] ([username],[email],[password],[fullname])
            VALUES ('{}','{}','{}','{}')""".format(user.username,user.email,password,user.fullname)

            cursor.execute(sql)
            cursor.commit()
            cursor.close()
            return True
        
        except Exception as ex:
            raise Exception(ex)
        
        



    @classmethod
    def get_by_id(cls, db,id):

        try:
            conection = db.obtener_conexion()
            cursor = conection.cursor()

            sql = """select id, username, email, fullname from [dbo].[user]
                        where id = '{}'""".format(id)

            cursor.execute(sql)
            row = cursor.fetchone()
            cursor.commit()
            cursor.close()
            
            if row != None:
                try:
                    logged_user = User(row[0],row[1],None,row[2],row[3])
                    return logged_user
                
                except Exception as e:
                    print(f"Error metodo get_by_id: {e}")
                    return False

            #si no se encontro registro
            else:
                return None

        
        except Exception as ex:
            raise Exception(ex)
    


    @classmethod
    def user_exist(cls,db, user):
        try:
            conection = db.obtener_conexion()
            cursor = conection.cursor()

            sql = "select * from [dbo].[user] where username = ?"

            cursor.execute(sql, user.username)
            row = cursor.fetchone()
            cursor.commit()
            cursor.close()
            
            if row != None:
                try:
                    #return True diciendo que si existe otro usuario
                    return True
                
                except Exception as e:
                    print(f"Error metodo user_exist: {e}")
                    return True

            #si no se encontro registro
            else:
                #return False diciendo que no existe otro usuario
                return False

        
        except Exception as ex:
            raise Exception(ex)




    @classmethod
    def get_user_from_username(cls,db, username):
        
        try:
            conection = db.obtener_conexion()
            cursor = conection.cursor()

            sql = """select * from [dbo].[user]
                        where username = '{}'""".format(username)

            cursor.execute(sql)
            row = cursor.fetchone()
            cursor.commit()
            cursor.close()
            
            if row != None:
                try:
                    logged_user = User(row[0],row[1],None,row[2],row[3])
                    return logged_user
                
                except Exception as e:
                    print(f"Error metodo get_id_by_username: {e}")
                    return False

            else:
                return None

        
        except Exception as ex:
            raise Exception(ex)