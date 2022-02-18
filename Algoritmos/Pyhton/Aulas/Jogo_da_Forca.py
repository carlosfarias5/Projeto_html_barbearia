import random

def desenho_forca():
        print("  _______     ")
        print(" |/      |    ")

        if (erros == 1):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if (erros == 2):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if (erros == 3):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if (erros == 4):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if (erros == 5):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if (erros == 6):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if (erros == 7):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

enforcou = False
acertou = False

with open("Lista-de-Palavras.txt", "r") as arquivo:
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

numero = random.randrange(0,len(palavras))

palavrasecreta = palavras[numero]

letras_certas = ["_" for letra in palavrasecreta]

erros = 0

while (not enforcou and not acertou):

    chute = input("Digite uma letra: ")

    if chute.upper() in palavrasecreta:
        index = 0
        for letra in palavrasecreta:
            if chute.upper() == letra.upper():
                letras_certas[index] = chute
            index += 1
    else:
        desenho_forca()
        erros += 1

    print(letras_certas)
    print(f'Voce tem {erros} erros.')
    if erros == 8:
        print("Voce perdeu!!")
        print(f"A palavra secreta era: {palavrasecreta}")
        enforcou = True
    elif "_" not in letras_certas:
        print("Voce ganhou!!")
        print(f"A palavra secreta era: {palavrasecreta}")
        acertou = True



