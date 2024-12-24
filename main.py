import db
from flask import Flask, render_template, request, redirect, url_for
from models import LibrosPendientes

app = Flask(__name__)


# Función para asignar colores a los libros
def asignar_colores(libros):
    colores = ["list-group-item-primary", "list-group-item-secondary", "list-group-item-success",
               "list-group-item-danger", "list-group-item-warning", "list-group-item-info"]
    for libro in libros:
        libro.color = colores[hash(libro.titulo) % len(colores)]
    return libros


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/deseos")
def deseos():
    todos_los_libros = db.session.query(LibrosPendientes).all()
    libros_con_colores = asignar_colores(todos_los_libros)
    return render_template("deseos.html", libros=libros_con_colores)


@app.route("/crear-libro", methods=["POST"])
def crear():
    libro = LibrosPendientes(titulo=request.form["titulo_libro"], autor=request.form["autor_libro"], leido=False)
    db.session.add(libro)
    db.session.commit()
    return redirect(url_for("deseos"))

@app.route("/libro-leido/<id>")
def leido(id):
    libro = db.session.query(LibrosPendientes).filter(LibrosPendientes.id == int(id)).first()
    libro.leido = not(libro.leido)
    db.session.commit()
    return redirect(url_for("deseos"))

@app.route("/eliminar-libro/<id>")
def eliminar(id):
    libro = db.session.query(LibrosPendientes).filter(LibrosPendientes.id == int(id)).delete()
    db.session.commit()
    return redirect(url_for("deseos"))

@app.route("/editar-libro/<id>", methods=["GET", "POST"])
def editar(id):
    libro = db.session.query(LibrosPendientes).filter(LibrosPendientes.id == int(id)).first()
    if request.method == "POST":
        libro.titulo = request.form["titulo"]
        libro.autor = request.form["autor"]
        libro.leido = "leido" in request.form
        db.session.commit()
        return redirect(url_for("deseos"))
    return render_template("editarLibro.html", libro=libro)



if __name__ == "__main__":
    # Crea todas las tablas si no existen
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)
