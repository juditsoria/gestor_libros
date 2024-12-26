Gestor de Libros
Este proyecto es una aplicación web para gestionar libros pendientes por leer. Está desarrollada utilizando Flask como framework de backend y SQLite como sistema de base de datos. El propósito de la aplicación es permitir a los usuarios agregar libros a una lista, marcar aquellos que ya han sido leídos, editarlos y eliminarlos.

Funcionalidades
Agregar libros: El usuario puede agregar un libro a la lista de libros pendientes por leer, proporcionando un título y un autor.
Ver libros: Los libros almacenados en la base de datos se muestran en una lista, con información sobre el título, autor y si el libro ha sido leído.
Marcar como leído: Los usuarios pueden marcar un libro como leído, lo que cambiará su visualización en la lista.
Editar libros: Al hacer clic en un icono de lápiz, el usuario puede modificar la información de un libro.
Eliminar libros: El usuario puede eliminar un libro de la lista si ya no lo desea.
Tecnologías
Flask: Framework web utilizado para desarrollar el backend de la aplicación.
SQLite: Base de datos utilizada para almacenar la información de los libros.
SQLAlchemy: ORM (Object-Relational Mapper) utilizado para facilitar la interacción con la base de datos.
Bootstrap: Framework de CSS utilizado para el diseño y la interfaz de usuario, en particular el tema Sketchy.
HTML/CSS: Lenguajes utilizados para la estructura y el diseño de las páginas web.

Estructura del Proyecto
Copiar código
/gestor-libros
│
├── static/
│   └── main.css          # Estilos CSS personalizados
│
├── templates/
│   └── editarLibro.html  # Página para editar libros
│   └── libros.html       # Página principal con la lista de libros
│
├── db.py                 # Configuración de la base de datos y la conexión con SQLAlchemy
├── main.py               # Lógica principal de la aplicación, rutas y vistas
├── models.py             # Definición de las clases y tablas de la base de datos
├── databases/            # Carpeta que contiene la base de datos (libros.db)
└── requirements.txt      # Archivo con las dependencias del proyecto
Requisitos
Antes de ejecutar el proyecto, asegúrate de tener Python y pip instalados. También necesitarás las siguientes bibliotecas, que puedes instalar mediante el archivo requirements.txt:


Copiar código
pip install -r requirements.txt

Instalación y Ejecución
Clona este repositorio:
Copiar código
git clone https://github.com/tu-usuario/gestor-libros.git
cd gestor-libros

Instala las dependencias:
Copiar código
pip install -r requirements.txt

Ejecuta la aplicación:
Copiar código
python main.py
Accede a la aplicación a través de tu navegador en la siguiente dirección:
Copiar código
http://127.0.0.1:5000/
Uso
Al abrir la aplicación, verás un formulario para agregar un nuevo libro a la lista.
Después de agregar un libro, serás redirigido a la lista de libros, donde podrás ver todos los libros almacenados.
Cada libro tiene opciones para marcarlo como leído, editar su información o eliminarlo.
Al editar un libro, podrás cambiar el título, autor y el estado de leído.
Capturas de Pantalla
A continuación se muestran algunas capturas de pantalla de la aplicación en funcionamiento:

Pantalla de inicio: Formulario para agregar un libro.
![Captura de pantalla 2024-12-24 183818](https://github.com/user-attachments/assets/7f1c9a3b-a720-4996-9a73-11ea2ec2c0f1)
Pantalla de libros pendientes: Lista de libros con opciones para editar o eliminar.
![Captura de pantalla 2024-12-24 185347](https://github.com/user-attachments/assets/259e8906-75ba-4b59-85bf-a6dc3e35bb04)
Marcar un libro como leído o eliminarlo de la lista.
![Captura de pantalla 2024-12-24 185915](https://github.com/user-attachments/assets/0e59edf2-c3fd-4173-8b46-ef87628802fe)
Formulario de edición: Página para modificar los detalles de un libro.
![Captura de pantalla 2024-12-24 190525](https://github.com/user-attachments/assets/d43a090b-813b-4837-876b-fd10cd305ba8)






Contribuciones
Si deseas contribuir a este proyecto, puedes hacerlo mediante un fork del repositorio y enviando un pull request con tus cambios.
