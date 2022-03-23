def main():
    print(converte(5))


def converte(horas):
    tempo = []

    # Converte horas para meses
    tempo.append(int(horas / 720))
    # Converte horas para semanas
    tempo.append(int(horas / 168))
    # Converte horas para dias
    tempo.append(int(horas / 24))
    # Converte horas para minutos
    tempo.append(horas * 60)
    # Converte horas para segundos
    tempo.append(horas * 3600)
    # Converte horas para milissegundos
    tempo.append(horas * 3600000)

    return tempo


main()
