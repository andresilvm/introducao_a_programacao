from random import randint

Q = []

for numero in range(20):
    Q.append(randint(1, 100))

print(Q)

maior = -1
menor = 101

for item_da_lista in Q:
    if maior < item_da_lista:
        maior = item_da_lista

    if menor > item_da_lista:
        menor = item_da_lista 

print('O maior valor é: {maior}')
print('O menos valor é: {menor}')

# FORMA MAIS SIMPLIFICADA

# Q = []

# for numero in range(20):
#     Q.append(randint(1, 100))

# print(Q)
# print(f"O maior valor é: {max(Q)}")
# print(f"O menor valor é: {min(Q)}")