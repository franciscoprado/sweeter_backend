from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from models import Base


class Postagem(Base):
    __tablename__ = "postagens"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(250))
    subtitulo = Column(String(250))
    texto = Column(String())
    data_insercao = Column(DateTime, default=datetime.now())
    curtidas = Column(Integer, default=0)
    postagem_mae = Column(Integer)

    def __init__(
        self, titulo, subtitulo, texto, postagem_mae = None, data_insercao: Union[DateTime, None] = None
    ):
        """Cria uma postagem

        Args:
            titulo (str): O título da postagem.
            subtitulo (str): O subtítulo da postagem.
            texto (str): O texto.
            postagem_mae (int): A postagem que está sendo respondida, caso seja uma resposta.
            data_insercao (Union[DateTime, None], optional): Data de inserção. Defaults to None.
        """
        self.titulo = titulo
        self.subtitulo = subtitulo
        self.texto = texto
        self.postagem_mae = postagem_mae

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

    def to_dict(self):
        """
        Retorna a representação em dicionário do Objeto Postagem.
        """
        return {
            "id": self.id,
            "titulo": self.titulo,
            "subtitulo": self.subtitulo,
            "texto": self.texto,
            "data_insercao": self.data_insercao,
            "curtidas": self.curtidas,
            "postagem_mae": self.postagem_mae
        }

    def __repr__(self):
        """
        Retorna uma representação da Postagem em forma de texto.
        """
        return f"Postagem(id={self.id}, titulo='{self.titulo}', subtitulo='{self.subtitulo}', texto='{self.texto}', curtidas={self.curtidas}, postagem_mae={self.postagem_mae})"
