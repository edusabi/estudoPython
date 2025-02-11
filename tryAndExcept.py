# try -> tenta executar o código
# except -> ocorreu algum erro ao tentar executar

algo = input("Digite algo: ")

try:
    algo_int = int(algo)
    print(f"Olá você digitou: {algo_int}")
except:
    print("Você não digitou algo certo")    