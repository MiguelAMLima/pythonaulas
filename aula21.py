# help() >>>pyhton console
# help(print)


# Docstring
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal CursoEmVideo.
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')


help(contador)


# Parâmetros opcionais
def somar(a, b, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(3, 2)


# Escopo de variáveis
def funcao():
    n1 = 5
    print(f'n1 dentro vale {n1}')
    global n2
    n2 = 6
    print(f'n2 dentro vale {n2}')


n1 = 10
n2 = 12
funcao()
print(f'n1 fora vale {n1}')
print(f'n2 fora vale {n2}')


# Retorno de valores
def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = soma(3, 2, 5)
r2 = soma(5, 10)
print(f'Os resultados foram {r1}, {r2} e {soma(20)}')
