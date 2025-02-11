"Peça um número ao usuário e veja se ele é impar ou par"

while True:
    try:
        numero = int(input("Digite um número: "))
        if numero % 2 == 0:
            print("Número par!")
            break
        else:
            print("Número impar!")
            break
    except ValueError:
        print("Você digitou uma letra.")
        continue