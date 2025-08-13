import random


def cumprimento(texto):
    return f"Olá, {texto}"


def media_numeros_aleatorios():
    numeros = [random.randint(1, 100) for _ in range(7)]
    media = sum(numeros) / len(numeros)
    return media


print(cumprimento("André Luís França Essinger"))

media = media_numeros_aleatorios()
print(f"A média dos 7 números sorteados é: {media:.2f}")
