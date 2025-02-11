"peça a o usuario que digite um numero N" \
"e somo todos os numero de 1 até N" \
"exemplos n = 5 saida 15: (1 + 2 + 3 + 4 + 5)"

numeroVezes = 0
numerosSomados = 0

while True:
    
    try:
        numero = int(input("Digite um número: "))
    except ValueError:
        print("Você digitou uma letra. Digite um número!!!")
        continue


    while numeroVezes < numero:
        
        numeroVezes += 1
        numerosSomados += numeroVezes
        

    if numeroVezes == numero:
        print(f'O número que você digitou foi: {numerosSomados} e a quantidade deles somados é: {numerosSomados}')
        break
    
        
        