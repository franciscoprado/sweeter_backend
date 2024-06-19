from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError

from helpers.postagem import encurtar_url
from models import Session, Postagem
from schemas import *
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)
resultados_por_pagina = 10

# definindo tags
home_tag = Tag(
    name="Documentação",
    description="Seleção de documentação: Swagger, Redoc ou RapiDoc",
)
postagem_tag = Tag(
    name="Postagem", description="Adição, visualização e remoção de postagens à base"
)


@app.get("/", tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação."""
    return redirect("/openapi")


@app.post(
    "/postagem",
    tags=[postagem_tag],
    responses={"200": PostagemViewSchema,
               "409": ErrorSchema, "400": ErrorSchema},
)
def add_postagem(form: PostagemSchema):
    """Adiciona um novo Postagem à base de dados

    Retorna uma representação dos postagem.
    """
    postagem = Postagem(
        titulo=form.titulo.strip(),
        subtitulo=form.subtitulo.strip(),
        texto=form.texto.strip(),
    )

    try:
        session = Session()
        session.add(postagem)
        session.commit()
        return apresenta_postagem(postagem), 200

    except IntegrityError as e:
        error_msg = "Postagem de mesmo nome já salvo na base :/"
        return {"mensagem": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        return {"mensagem": error_msg}, 400


@app.get(
    "/postagens",
    tags=[postagem_tag],
    responses={"200": ListagemPostagensSchema, "404": ErrorSchema},
)
def get_postagens(query: PostagensPagina = 1):
    """Faz a busca por todos os posts cadastrados

    Retorna uma representação da listagem de postagens.
    """

    pagina = query.pagina - 1
    session = Session()
    postagens = session.query(Postagem).order_by(
        desc(Postagem.data_insercao)).offset(resultados_por_pagina * pagina).limit(resultados_por_pagina).all()

    if not postagens:
        return {"postagens": []}, 200

    return apresenta_postagens(postagens), 200


@app.get(
    "/postagem",
    tags=[postagem_tag],
    responses={"200": PostagemViewSchema, "404": ErrorSchema},
)
def get_postagem(query: PostagemBuscaPorIDSchema):
    """Faz a busca por uma postagem a partir do id.

    Retorna uma representação das postagens.
    """
    postagem_id = query.id
    session = Session()
    postagem = session.query(Postagem).filter(
        Postagem.id == postagem_id).first()

    if not postagem:
        error_msg = "Postagem não encontrada na base :/"
        return {"mensagem": error_msg}, 404

    return apresenta_postagem(postagem), 200


@app.delete(
    "/postagem",
    tags=[postagem_tag],
    responses={"200": PostagemDelSchema, "404": ErrorSchema},
)
def del_postagem(query: PostagemBuscaPorIDSchema):
    """Deleta uma Postagem a partir do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
    postagem_id = query.id
    session = Session()
    count = session.query(Postagem).filter(Postagem.id == postagem_id).delete()
    session.commit()

    if count:
        return {"mensagem": "Postagem removida", "id": postagem_id}

    error_msg = "Postagem não encontrado na base :/"
    return {"mensagem": error_msg}, 404


@app.get(
    "/busca_postagem",
    tags=[postagem_tag],
    responses={"200": ListagemPostagensSchema, "404": ErrorSchema},
)
def busca_postagem(query: PostagemBuscaSchema):
    """Faz a busca por postagens a partir de um termo.

    Retorna uma representação das postagens.
    """
    termo = unquote(query.termo).strip()
    pagina = query.pagina - 1
    session = Session()
    postagens = (
        session.query(Postagem)
        .filter(
            Postagem.titulo.ilike(f"%{termo}%")
            | Postagem.subtitulo.ilike(f"%{termo}%")
            | Postagem.texto.ilike(f"%{termo}%")
        )
        .offset(resultados_por_pagina * pagina).limit(resultados_por_pagina).all()
    )

    if not postagens:
        return {"postagens": []}, 200

    return apresenta_postagens(postagens), 200


@app.put(
    "/postagem",
    tags=[postagem_tag],
    responses={"200": PostagemViewSchema,
               "409": ErrorSchema, "400": ErrorSchema},
)
def update_postagem(form: PostagemAtualizacaoSchema):
    """Atualiza uma postagem na base de dados

    Retorna uma representação dos postagem.
    """
    dados = {"titulo": form.titulo,
             "subtitulo": form.subtitulo, "texto": encurtar_url(form.texto)}

    try:
        session = Session()
        session.query(Postagem).filter(Postagem.id == form.id).update(dados)
        session.commit()
        postagem = session.query(Postagem).filter(
            Postagem.id == form.id).first()
        return apresenta_postagem(postagem), 200

    except IntegrityError as e:
        error_msg = "Postagem de mesmo nome já salvo na base :/"
        return {"mensagem": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        return {"mensagem": error_msg}, 400


@app.put(
    "/curtir",
    tags=[postagem_tag],
    responses={"200": PostagemViewSchema,
               "409": ErrorSchema, "400": ErrorSchema},
)
def curtir(form: PostagemAtualizacaoSchema):
    """Adiciona uma curtida a uma postagem na base de dados

    Retorna uma representação do total de curtidas.
    """
    try:
        session = Session()
        postagem = session.query(Postagem).filter(
            Postagem.id == form.id).first()
        postagem.curtidas += 1
        session.commit()
        return apresenta_postagem(postagem), 200

    except IntegrityError as e:
        error_msg = "Postagem de mesmo nome já salvo na base :/"
        return {"mensagem": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        return {"mensagem": error_msg}, 400
