import random
palavras = ["gato", "cachorro", "porco", "largatixa"]
palavras = random.choice(palavras)
def words():
    contador = 3
    while contador > 0 :
        escolha=input("Digite a palvra que você acha que é, a dica é animal: ")
        if escolha == palavras:
            print("Voce acertou!!!")
            break
        elif contador == 0:
            print("Você utilizou todas as tentativas")
        else:
            contador = contador - 1 
            print(f"Voce errou tente novamente")
words()