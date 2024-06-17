from db_artistas import db_artistas


def consultar_artistas(artistas_listados, chave):
    try:
        if len(artistas_listados) < 2:
            return artistas_listados

        pivo = artistas_listados[0]
        left_sublist = [artista for artista in artistas_listados[1:] if artista[chave] <= pivo[chave]]
        right_sublist = [artista for artista in artistas_listados[1:] if artista[chave] > pivo[chave]]

        return consultar_artistas(left_sublist, chave) + [pivo] + consultar_artistas(right_sublist, chave)
    except Exception as error:

        return f'Ocorreu um erro: {str(error)}'

