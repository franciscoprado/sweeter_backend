from pydantic import BaseModel


class LoginSchema(BaseModel):
    email: str = 'test'
    senha: str = 'test@test.com'


class UsuarioTokenSchema(BaseModel):
    access_token: str = ''
