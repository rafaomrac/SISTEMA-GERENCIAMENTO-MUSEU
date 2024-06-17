from db_obras import db_obras


def inserir_obras():

    try:
        while True:
            pergunta_inicial = input("Adicionar obras no sistema? (S/N): ")

            if pergunta_inicial.lower() != 's':
                break

            titulo = input("Titulo da obra: ")
            data_criacao = input("Data de criação da obra: ")
            quantidade = int(input("Quantidade: "))
            tema = input("Tema: ")
            estilos_artisticos = input("Estilos artísticos do artista (separados por vírgula): ").split(',')
            descricao = input("Descrição da obra: ")
            tecnica = input("Tecnica utlizada: ")
            artista = input("Artista da obra: ")
            local_exposicao = input("Local de exposição da obra: ")

            obras = {
                'titulo': titulo,
                'data_criacao': data_criacao,
                'quantidade': quantidade,
                'tema': tema,
                'estilos': [estilo for estilo in estilos_artisticos],
                'descricao': descricao,
                'tecnica': tecnica,
                'artista': artista,
                'local_exposicao': local_exposicao
            }

            db_obras.append(obras)

        return db_obras

    except Exception as error:

        return f'Ocorreu um erro {str(error)}'







