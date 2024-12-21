from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine permite a sqlAlchemmy conectarse a la BBDD
engine = create_engine("sqlite:///database/librosPendientes.db",
                        # sirve para que no se ejecute en el mismo hilo que el de la web
                       connect_args = {"check_same_thread": False}) # solo flask
# crear la sesion, lo que nos permite realizar transacciones dentro de la BBDD
Session = sessionmaker(bind = engine)
session = Session()
# sirve para que la informacion de los modelos de datos se mapee en la BBDD
Base = declarative_base()