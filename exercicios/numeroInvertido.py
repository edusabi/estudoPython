# numero = input("Digite um número: ")
# numero_invertido = ""

# for numeros in numero:
#     numero_invertido = numeros + numero_invertido

# print(numero_invertido)

numero = int(input("Digite um número: "))  
numero_invertido = 0  

while numero > 0:
    resto = numero % 10  # Pega o último dígito
    numero_invertido = (numero_invertido * 10) + resto  # Constrói o número invertido
    numero //= 10  # Remove o último dígito
    print(numero_invertido)
    print(numero)

print("Número invertido:", numero_invertido)
