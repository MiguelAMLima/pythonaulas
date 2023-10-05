num = [2, 5, 9, 1]
print(num)
num[2] = 3  # Transforma valor na 2ª posição em 3
num.append(7)  # Adiciona valor 7 no fim
num.insert(2, 0)  # Adiciona valor 0 na posição 2
print(num)
num.sort()  # Ordem alfabética
print(num)
num.sort(reverse=True)  # Ordem alfabética ao contrário
print(num)
num.pop()  # Remove último valor
num.pop(2)  # Remove valor na posição 2
if 5 in num:
    num.remove(5)  # Remove o primeiro valor 5
else:
    print('Essa lista não possui o número 5')
print(num)
valores = list()
for cont in range(1, 5):
    valores.append(int(input(f'Digite o {cont}º valor inteiro: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor {v}')
clone = valores  # Cria uma ligação entre as listas, o que muda em uma muda em outra
clone2 = valores[:]  # Cria uma cópia da lista, o que muda em uma não muda em outra
