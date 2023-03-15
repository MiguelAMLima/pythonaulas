print('\033[7;30;45mOlá, Mundo!\033[m')
print('\033[1;32;46mOlá, Mundo!\033[m')
print('\033[4;31;44mOlá, Mundo!\033[m')
print('\033[0;33;47mOlá, Mundo!\033[m')
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
nome = 'Galio'
print('Meu nome do meio é Justiça, {}{}{} Justiça Justiça!'
      .format('\033[1;35m', nome, '\033[m'))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;97m'}
print('Meu nome do meio é Justiça, {}{}{} Justiça Justiça!'
      .format(cores['pretoebranco'], nome, cores['limpa']))
