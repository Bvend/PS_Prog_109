def main():
    print(repeti("Crossbots", 3))


def repeti(item, num_rep):
    lista = []

    # Insere item informado num_rep vezes na lista
    for i in range(num_rep):
        lista.append(item)

    # Devolve lista
    return lista


main()
