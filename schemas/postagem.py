from pydantic import BaseModel
from typing import Optional, List
from models.postagem import Postagem


class PostagemSchema(BaseModel):
    """Define como uma nova postagem a ser inserida deve ser representada"""

    titulo: str = "Camiseta"
    subtitulo: str = 29.99
    texto: str = "Uma camiseta confortável e estilosa"
    postagem_mae: int = None


class PostagemViewSchema(BaseModel):
    """Define como uma nova postagem a ser inserida deve ser representada"""

    id: int = 1
    titulo: str = "Título do post"
    subtitulo: str = "Subtítulo"
    texto: str = "Um texto genérico vai aqui representando o conteúdo"
    data_insercao: str = ""
    curtidas: int = 0
    postagem_mae: int = None


class PostagemAtualizacaoSchema(BaseModel):
    """Define como uma nova postagem a ser atualizada deve ser representada"""

    id: int = 1
    titulo: str = "Título do post"
    subtitulo: str = "Subtítulo"
    texto: str = "Um texto genérico vai aqui representando o conteúdo"


class PostagemBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca."""

    termo: str = "Lorem ipsum"
    pagina: int = 1


class PostagemBuscaPorIDSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca. Que será
    feita apenas com base no ID da postagem.
    """

    id: int = "1"


class ListagemPostagensSchema(BaseModel):
    """Define como uma listagem de postagens será retornada."""

    postagens: List[PostagemViewSchema]


def apresenta_postagens(postagens: List[Postagem]):
    """Retorna uma representação da postagem seguindo o schema definido em
    ListagemPostagensSchema.
    """
    result = []
    for postagem in postagens:
        result.append(
            {
                "id": postagem.id,
                "titulo": postagem.titulo,
                "subtitulo": postagem.subtitulo,
                "texto": postagem.texto,
                "data_insercao": postagem.data_insercao,
                "curtidas": postagem.curtidas,
                "postagem_mae": postagem.postagem_mae,
            }
        )

    return {"postagens": result}


class PostagemDelSchema(BaseModel):
    """Define como deve ser a estrutura do dado retornado após uma requisição
    de remoção.
    """

    mensagem: str


def apresenta_postagem(postagem: Postagem):
    """Retorna uma representação da postagem seguindo o schema definido em
    PostagemViewSchema.
    """
    return {
        "id": postagem.id,
        "titulo": postagem.titulo,
        "subtitulo": postagem.subtitulo,
        "texto": postagem.texto,
        "data_insercao": postagem.data_insercao,
        "curtidas": postagem.curtidas,
        "postagem_mae": postagem.postagem_mae,
    }


class PostagensPagina(BaseModel):
    """Define como deve ser a estrutura que representa a paginação.
    """

    pagina: int = 1
