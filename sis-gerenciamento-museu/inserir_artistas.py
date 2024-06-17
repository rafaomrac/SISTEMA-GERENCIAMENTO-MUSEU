from db_artistas import db_artistas


def inserir_artistas():

    try:
        while True:
            pergunta_inicial = input("Adicionar artistas no sistema? (S/N): ")

            if pergunta_inicial.lower() != 's':
                break

            nome = input("Nome do artista: ")
            data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
            local_nascimento = input("Cidade em qual artista nasceu: ")
            bio = input("Biografia do artista: ")
            estilos = input("Estilos artísticos do artista (separados por vírgula): ").split(',')

            artistas = {
                'nome': nome,
                'data_nascimento': data_nascimento,
                'local_nascimento': local_nascimento,
                'bio': bio,
                'estilo': [estilo for estilo in estilos],
            }

            db_artistas.append(artistas)

        return db_artistas

    except Exception as error:

        return f"Ocorreu um erro ao inserir os artistas: {str(error)}"
