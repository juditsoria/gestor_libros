from sqlalchemy import Column, Integer, String, Boolean

import db

class LibrosPendientes(db.Base):
    __tablename__ = "librosPendientes"
    __table_args__ = {"sqlite_autoincrement" : True}
    id = Column(Integer, primary_key = True)
    titulo = Column(String, nullable = False)
    autor = Column(String, nullable=True, default = "Desconocido")
    leido = Column(Boolean)
    def __init__(self, titulo, autor, leido):
        self.titulo = titulo
        self.autor = autor
        self.leido = leido
    def __str__(self):
        return f"El libro {self.titulo}, escrito por {self.autor}¿Ha sido leido?: {self.leido}"