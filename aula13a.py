for c in range(6, 0, -1):
    print(c)
print('-=' * 6)
for c in range(0, 7, 2):
    print(c)
print('-=' * 6)
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('-=' * 6)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('-=' * 6)
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
