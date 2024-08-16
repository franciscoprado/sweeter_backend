from pydantic import BaseModel


class ErrorSchema(BaseModel):
    """ Define como uma mensagem de erro será representada
    """
    mensagem: str


class UnauthorizedSchema(BaseModel):
    """ Define como uma mensagem de usuário não autorizado será representada
    """
    msg: str
