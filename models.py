from sqlalchemy import Column, Integer, String

import db

'''class Persona(db.Base):
    __tablename__ = "persona"
    __table_args__ = {"sqlite_autoincrement" : True}
    id = Column(Integer, primary_key = True)
    nombre = Column(String, nullable = False)
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"persona {self.nombre}" '''