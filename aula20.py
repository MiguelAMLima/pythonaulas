def lin():
    print('-' * 30)


def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos +=1


lin()
titulo('        CURSO EM VÍDEO        ')

contador(1, 9, 9, 7)
contador(4, 3, 1, 9, 9, 9)

valores = [2, 7, 1, 8, 2]
dobra(valores)
print(valores)
