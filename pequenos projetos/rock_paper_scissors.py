import random
def game ():
    jogada = input("Escolha entre pedra papel ou tesoura: ")
    random_choice = random.choice(["pedra","papel","tesoura"])
    if jogada == random_choice:
        return "Vocês escolheram a mesma coisa usuario computador"
    if ganhou(jogada, random_choice):
        return 'Você ganhou'
    return 'Voce perdeu'
def ganhou(usuario, computador):
    if (usuario == "pedra" and computador == "tesoura") or (usuario == "papel" and computador == "pedra") or \
        (usuario == "tesoura" and computador == "papel"):
        return True
print(game())