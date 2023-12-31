from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Función para establecer una conexión con la base de datos MySQL
def crear_conexion():
    conexion = mysql.connector.connect(
     user= 'root',
     password= 'root',
     database= 'calculo_tarifario')
    return conexion

# Ruta para mostrar la lista de usuarios desde la base de datos
@app.route('/')
def mostrar_usuarios():
    try:
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute('SELECT id, usuario,contraseña FROM usuarios')
        usuarios = cursor.fetchall()
        cursor.close()
        conexion.close()
        return render_template('usuarios.html', usuarios=usuarios)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)