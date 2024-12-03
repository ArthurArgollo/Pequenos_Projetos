import random

def numero (x):
    numero_aleatorio = random.randint(1, x)
    numero = 0
    while numero != numero_aleatorio:
        numero = int(input(f"Chute um numero entre 1 e {x}: "))
        if numero < numero_aleatorio:
            print("Você chutou muito baixo")
        elif numero > numero_aleatorio:
            print("Você chutou muito alto")
    print(f"Você acertou o numero era {numero_aleatorio}")
    dnv()
def dnv():
    escolha= input("Deseja jogar novamente S ou N: ")
    if escolha == "S":
        numero(10)
    elif escolha == "N":
        print("O jogo será finalizado")
    else:
        print("Escolha a opção correta")  
        dnv()
numero(10)