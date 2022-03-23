def main():
    mapa = [['M', 'M', 'P', 'M'],
            ['M', 'M', 'P', 'M'],
            ['M', 'M', 'P', 'M'],
            ['M', 'M', 'M', 'M']]

    travessia(mapa, 0, 0, 0, 3)


def travessia(mapa, xi, yi, xf ,yf):
    # Coleta ordem da matriz mapa
    ordem = len(mapa)

    # Verifica se a ordem � valida
    if ordem < 4 or ordem > 7:
        return

    # Verifica se ponto de partida est� incluso no mapa
    if (xi < 0 or xi >= ordem) or (yi < 0 or yi >= ordem):
        return

    # Verifica se ponto de chegada est� incluso no mapa
    if (xf < 0 or xf >= ordem) or (yf < 0 or yf >= ordem):
        return

    # Cria c�pia tempor�ria da matriz mapa
    distancias = []
    for i in range(ordem):
        lista = []
        for j in range(ordem):
            if (mapa[i][j] == 'M'):
                lista.append('M')
            else:
                lista.append("P")
        distancias.append(lista)

    # Percorre matriz mapeando distancia em rela��o ao ponto de partida
    distancias[xi][yi] = 0
    encontrou_caminho = 1
    valor_procurado = 0
    while (encontrou_caminho):
        encontrou_caminho = 0
        for i in range(ordem):
            for j in range(ordem):
                if distancias[i][j] == valor_procurado:
                    if i + 1 < ordem and distancias[i + 1][j] == 'M':
                        distancias[i + 1][j] = valor_procurado + 1
                        encontrou_caminho = 1
                    if i - 1 >= 0 and distancias[i - 1][j] == 'M':
                        distancias[i - 1][j] = valor_procurado + 1
                        encontrou_caminho = 1
                    if j + 1 < ordem and distancias[i][j + 1] == 'M':
                        distancias[i][j + 1] = valor_procurado + 1
                        encontrou_caminho = 1
                    if j - 1 >= 0 and distancias[i][j - 1] == 'M':
                        distancias[i][j - 1] = valor_procurado + 1
                        encontrou_caminho = 1
        valor_procurado += 1

    # Imprime dist�ncia percorrida, caso for poss�vel chegar at� o destino final
    if distancias[xf][yf] == 'M':
        print('Movimentos necess�rios: SI')
    else:
        print(f'Movimentos necess�rios: {distancias[xf][yf]}')

    return

main()
