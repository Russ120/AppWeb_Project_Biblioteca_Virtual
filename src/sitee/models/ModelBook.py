from sitee.models.entities import Book
from flask import Flask, Blueprint
from flask import render_template, request, redirect, send_from_directory, session,jsonify
from flask_login import LoginManager, login_user, logout_user, login_required
from datetime import datetime
import os


class ModelBook():


    @classmethod
    def get_by_id(cls, id, db):



        try:
            connection = db.obtener_conexion()
            cursor = connection.cursor()

            if id != None:
                slqSelect = "SELECT * FROM [dbo].[Libros] WHERE id = ?"
                cursor.execute(slqSelect, id)
                libros = cursor.fetchall()
                cursor.commit()
                cursor.close()

                return libros
            
            else:
                slqSelect = "SELECT * FROM [dbo].[Libros]"
                cursor.execute(slqSelect)
                libros = cursor.fetchall()
                cursor.commit()
                cursor.close()

                return libros
                
        except FileNotFoundError:
            return jsonify({"error": "El registro no se encontró por id."})

        except Exception as e:
            connection.rollback()  # Revertir cambios en caso de error
            return jsonify({"error es este": str(e)})
        


    @classmethod
    def get_all_books(cls, db, user_id = 0):
        try:
            connection = db.obtener_conexion()
            cursor = connection.cursor()

            if user_id == 0:
                slqSelect = "SELECT * FROM [dbo].[Libros]"
                cursor.execute(slqSelect)
                libros = cursor.fetchall()
                cursor.commit()
                cursor.close()
                return libros
                
            else:
                slqSelect = "SELECT * FROM [dbo].[Libros] WHERE [id_user] = ?"
                cursor.execute(slqSelect, user_id)
                libros = cursor.fetchall()
                cursor.commit()
                cursor.close()
                return libros
        
        except FileNotFoundError:
            return jsonify({"error": "los registros no se encontraron."})

        except Exception as e:
            connection.rollback()  # Revertir cambios en caso de error
            return jsonify({"error es este": str(e)})







    @classmethod
    def search_books(cls, db, parametro, id_user = 0):
        try:
            connection = db.obtener_conexion()
            cursor = connection.cursor()


            if id_user != 0:
                slqSelect = "SELECT * FROM [dbo].[Libros] WHERE ([titulo] LIKE ? OR [autor] LIKE ?) AND [id_user] = ? ORDER BY [titulo] ASC;"
                
                parametro = "%" + parametro + "%"
                datos = (parametro,parametro, id_user)
                cursor.execute(slqSelect, datos)
                libros = cursor.fetchall()
                connection.commit()
                cursor.close()

                return libros


            else:
                slqSelect = "SELECT * FROM [dbo].[Libros] WHERE [titulo] LIKE ? OR [autor] LIKE ? ORDER BY [titulo] ASC"
                parametro = "%" + parametro + "%"
                datos = (parametro,parametro)
                cursor.execute(slqSelect, datos)
                libros = cursor.fetchall()
                connection.commit()
                cursor.close()

                return libros
        
        except FileNotFoundError:
            return jsonify({"error": "los registros no se encontraron."})

        except Exception as e:
            connection.rollback()  # Revertir cambios en caso de error
            return jsonify({"error es este": str(e)})


    @classmethod
    def search_by_category(cls, categoria, db):
        try:
            connection = db.obtener_conexion()
            cursor = connection.cursor()

            slqSelect = "SELECT * FROM [dbo].[Libros] WHERE [categoria] = ? ORDER BY [titulo] ASC"
            cursor.execute(slqSelect, categoria)
            libros = cursor.fetchall()
            connection.commit()
            cursor.close()
            return libros
        
        except FileNotFoundError:
            return jsonify({"error": "los registros no se encontraron."})

        except Exception as e:
            connection.rollback()  # Revertir cambios en caso de error
            return jsonify({"error es este": str(e)})









    @classmethod
    def update(cls, libro, db):

        try:
            connection = db.obtener_conexion()
            cursor = connection.cursor()

            #si insertaron una imagen pues actualizala
            if libro.imagen != "":
                sql = "UPDATE [dbo].[Libros] SET [titulo] = ?,[autor] = ?,[editorial] = ?,[año] = ?,[descripcion] = ?,[imagen] =?,[url] = ?, [categoria] = ? WHERE id = ?"
                datos = (libro.titulo, libro.autor, libro.editorial, libro.año, libro.descripcion, libro.imagen, libro.url, libro.categoria, libro.id)
                cursor.execute(sql, datos)
                connection.commit()
                cursor.close()

                #si no insertaron una imagen pues deja la que está
            else:
                sql = "UPDATE [dbo].[Libros] SET [titulo] = ?,[autor] = ?,[editorial] = ?,[año] = ?,[descripcion] = ?,[url] = ?, [categoria] = ? WHERE id = ?"
                datos = (libro.titulo, libro.autor, libro.editorial, libro.año, libro.descripcion, libro.url, libro.categoria, libro.id)
                cursor.execute(sql, datos)
                connection.commit()
                cursor.close()


        except FileNotFoundError:
            return jsonify({"error": "los registros no se encontraron."})

        except Exception as e:
            connection.rollback()  # Revertir cambios en caso de error
            return jsonify({"error es este": str(e)})



    @classmethod
    def save(cls, libro, db):
        try:
            connection = db.obtener_conexion()
            cursor = connection.cursor()

            slq = "INSERT INTO [dbo].[Libros]([titulo],[autor],[editorial],[año],[descripcion],[imagen],[url],[categoria],[id_user]) VALUES(?,?,?,?,?,?,?,?,?);"
            # datos = (_nombre,_autor,_editorial,_año,_descripcion,str(nuevoNombre),_url)
            datos = (libro.titulo, libro.autor, libro.editorial, libro.año, libro.descripcion, libro.imagen, libro.url, libro.categoria, libro.user_id)

            cursor.execute(slq, datos)
            connection.commit()
            cursor.close()

        except FileNotFoundError:
            return jsonify({"error": "el registro no se guardó."})

        except Exception as e:
            connection.rollback()  # Revertir cambios en caso de error
            return jsonify({"error es este": str(e)})



    @classmethod
    def delete(cls, _id, db):
        connection = db.obtener_conexion()
        cursor = connection.cursor()

        #borrar registro
        slqDelete = "DELETE FROM [dbo].[Libros] WHERE id = ?;"
        cursor.execute(slqDelete, _id)
        connection.commit()
        cursor.close()










    @classmethod
    def delete_img(cls, libro):
        try:
            if libro:

                imagenURL = os.path.join(os.getcwd(), "src", "sitee", "staticc", "img", str(libro[0][6]))

                #si existe eliminala
                if os.path.exists(imagenURL):
                    os.unlink(imagenURL)


                #si existe eliminala
                # if os.path.exists("staticc/img/" + str(libro[0][8])):
                #     os.unlink("staticc/img/" + str(libro[0][8]))
                    # os.unlink("templates/Sitio/img/" + str(libro[0][8]))
                else:
                    print("Nos e puede eliminar por que la imagen no existe")
            
        except FileNotFoundError:
            return jsonify({"error": "al tratar de eliminar y/o guardar una imagen."})

        except Exception as e:
            return jsonify({"error es este": str(e)})



    @classmethod
    def update_img(cls, libro,_archivo):
        try:
            if libro:

                imagenURL = os.path.join(os.getcwd(), "src", "sitee", "staticc", "img", str(libro[0][6]))

                #si existe eliminala
                if os.path.exists(imagenURL):
                    os.unlink(imagenURL)

                # si no se metio en el if de arriba es por que no existe, y si existia ya valio y esto se va a crear por que se va a crear
                tiempo = datetime.now()
                horaActual = tiempo.strftime('%Y%H%M%S')
                nuevoNombre = horaActual + '_' + _archivo.filename


                ruta_absoluta = os.path.join(os.getcwd(), "src" , "sitee", "staticc", "img", nuevoNombre)
                _archivo.save(ruta_absoluta)

                return nuevoNombre
            
        except FileNotFoundError:
            return jsonify({"error": "al tratar de eliminar y/o guardar una imagen."})

        except Exception as e:
            return jsonify({"error es este": str(e)})
        

        
    @classmethod
    def save_rename_img(cls,_archivo):
        try:
            tiempo = datetime.now()
            horaActual = tiempo.strftime('%Y%H%M%S')
            nuevoNombre = horaActual + '_' + _archivo.filename


            ruta_absoluta = os.path.join(os.getcwd(), "src" , "sitee", "staticc", "img", nuevoNombre)
            _archivo.save(ruta_absoluta)

            return nuevoNombre
            
        except FileNotFoundError:
            return jsonify({"error": "al tratar de eliminar y/o guardar una imagen."})

        except Exception as e:
            return jsonify({"error es este": str(e)})
