def soma(*args):
    total = 0

    for numero in args:
        total += numero
    return total

soma1 = soma(1,2,3,4,5,6,7,8,9)
soma2 = soma(10,20,30,40,50,60,70,80,90)

print(soma1)
print(soma2)