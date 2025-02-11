"Peça ao usuário qualquer numero e conte quantos digitos ele tem"

while True:

    try:
        numero = int(input("Digite qualquer número: "))
    except ValueError:
        print("Você digitou uma letra, digite um número!")
        continue

    qntNumerosStr = str(numero)
    qntdDigitos = len(qntNumerosStr)
    print(f"O número que você digitou foi: {numero} e ele tem: {qntdDigitos} digitos.")
    break
    