numeroCerto = 100
tentativas = 0

while True:
    tentativas += 1

    try:
        numero = int(input("Digite um número: "))
    except ValueError:
        print("Você digitou uma letra.")
        continue

    if isinstance(numero,int):
        if numero == numeroCerto:
            print("Parabéns você acertou!!")
            print(f"O número era {numeroCerto}.")
            print(f"E o número de tentativas foi {tentativas}x")
            break
        elif numero > numeroCerto:
            print("O número que você digitou é maior.")
        else:
            print("O número que você digitou é menor.")
        continue



