from db_artistas import db_artistas
from consultar_artistas import consultar_artistas
from inserir_artistas import inserir_artistas
from inserir_obras import inserir_obras


def main():
    inserir_artistas()
    inserir_obras()

    p = input("Quer consultar os artistas em ordem alfabética? (S/N): ")

    if p.lower() == 's':

        print(consultar_artistas(db_artistas, 'nome'))

    print("Programa encerrado!")


if __name__ == "__main__":
    main()
