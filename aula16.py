lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[:3:2])
print('-=' * 12)
for cont in range(0, len(lanche)):
    print(lanche[cont])
print('-=' * 12)
for comida in lanche:
    print(comida)
print('-=' * 12)
for posicao, comida in enumerate(lanche):
    print(comida, posicao)
print('-=' * 12)
print(sorted(lanche))
print('-=' * 12)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print('-=' * 12)
print(c.count(5))
print(c.index(8))
print(c.index(5, 1))
print('-=' * 12)
pessoa = ('Miguel', 26, 'M', 71.5)
del pessoa
