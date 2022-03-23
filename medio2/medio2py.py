def main():
    print(crossbots(5))


def crossbots(num):
    # Devolve "Crossbots" caso numero informado seja multiplo de 3 e 5
    if num % 3 == 0 and num % 5 == 0:
        return "CrossBots"
    # Devolve "Cross" caso numero informado seja apenas multiplo de 3
    elif num % 3 == 0:
        return "Cross"
    # Devolve "Bots" caso numero informado seja apenas multiplo de 5
    elif num % 5 == 0:
        return "Bots"
    # Devolve o proprio numero, caso esse nao seja multiplo de 3 ou 5
    else:
        return num


main()
