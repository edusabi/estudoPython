# tipo tupla é uma lista imutavél ou seja, que não pode ser mexida/editada
# para fazer uma tupla pode ser feita de 2 maneiras ou deixando sem nada, exemplo:
nomes1 = "Luís", "Maria", "Edu"
print("")
print(nomes1, "/", type(nomes1))
print("")

# ou simplesmente colocando ( )
nomes2 = ("síul", "airam", "ude")
print(nomes2, "/", type(nomes2))
print("")

# e é possivel converter tuplas para lista e vice versa, exemplos:

nomes1List = list(nomes1) #convertendo a tupla para lista
print(nomes1List, "/", type(nomes1List))
print("")

nomes1ListForTuplas = tuple(nomes1List) #convertendo a lista para tupla
print(nomes1ListForTuplas, "/", type(nomes1ListForTuplas))
print("")

