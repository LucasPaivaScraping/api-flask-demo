from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import sqlite3
app = Flask(__name__)
api = Api(app)


@app.route("/")
def init():
    return {"data": "My first API Rest"}


@app.route('/helloworld/<name>', methods=['get'])
def saludar(name):
    return {
        "data": {
            "hello": name
        }
    }


@app.route('/alumnos', methods=['get'])
def listado_alumnos():
    conn = sqlite3.connect("alumnos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alumnos")
    alumnos = cursor.fetchall()
    json_alumnos = []

    for id, nombre, apellido, edad, curso in alumnos:
        json_alumnos.append({
            "id": id,
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "curso": curso
        })

    return {"data": json_alumnos}


@app.route('/alumnos/nuevo/<nombre>/<apellido>/<edad>/<curso>', methods=['get'])
def agregar_alumno(nombre, apellido, edad, curso):
    conn = sqlite3.connect("alumnos.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO alumnos VALUES (?,?,?,?,?)",
        (None, nombre, apellido, edad, curso)
    )
    conn.commit()
    return {"resultado": "Nuevo alumno ingresado!"}


if __name__ == '__main__':
    app.run(port=8000)
