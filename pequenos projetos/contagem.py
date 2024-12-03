import time
## Contador de contagem regressiva onde o usuario pode adcionar o input que ele desejar
contador = int(input("Informe qual o numero do contador: "))
while contador > 0:
    contador = contador - 1
    time.sleep(1)
    print(contador)