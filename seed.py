import datetime
import lorem
from models import Session, Postagem

total_itens = 12  # O número de postagens a ser gerado.

if __name__ == "__main__":
    print("Iniciando o seeding...")
    session = Session()

    for numero in range(total_itens):
        data_insercao = datetime.datetime.now() - datetime.timedelta(days=numero)
        favorito = Postagem(
            titulo=lorem.sentence(),
            subtitulo=lorem.sentence(),
            texto=lorem.text(),
            data_insercao=data_insercao)
        session.add(favorito)

    session.commit()
    print("Seeding concluído")
