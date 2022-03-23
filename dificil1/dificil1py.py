def main():
    mapa = [['M', 'M', 'P', 'M'],
            ['M', 'M', 'P', 'M'],
            ['M', 'M', 'P', 'M'],
            ['M', 'M', 'M', 'M']]

    travessia(mapa, 0, 0, 0, 3)


def travessia(mapa, xi, yi, xf ,yf):
    # Coleta ordem da matriz mapa
    ordem = len(mapa)

    # Verifica se a ordem é valida
    if ordem < 4 or ordem > 7:
        return

    # Verifica se ponto de partida está incluso no mapa
    if (xi < 0 or xi >= ordem) or (yi < 0 or yi >= ordem):
        return

    # Verifica se ponto de chegada está incluso no mapa
    if (xf < 0 or xf >= ordem) or (yf < 0 or yf >= ordem):
        return

    # Cria cópia temporária da matriz mapa
    distancias = []
    for i in range(ordem):
        lista = []
        for j in range(ordem):
            if (mapa[i][j] == 'M'):
                lista.append('M')
            else:
                lista.append("P")
        distancias.append(lista)

    # Percorre matriz mapeando distancia em relação ao ponto de partida
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

    # Imprime distância percorrida, caso for possível chegar até o destino final
    if distancias[xf][yf] == 'M':
        print('Movimentos necessários: SI')
    else:
        print(f'Movimentos necessários: {distancias[xf][yf]}')

    return

main()
