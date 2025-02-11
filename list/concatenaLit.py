lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

# possui 2 jeitos de fazer usando o " + " e a função extend
#a função extend mexe diretamente com a lista que foi adiciona e não pode ser jogado em uma variavel
lista_c = lista_a + lista_b
print(lista_c,", variavel da soma da lista A com B, sendo concatenadas e jogadas em uma variavel")

lista_a.extend(lista_b)
print(lista_a,", LISTA A MODIFICADA USANDO EXTEND")