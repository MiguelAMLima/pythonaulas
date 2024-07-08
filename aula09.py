frase = 'Curso em Vídeo Python'
print(frase[9])
print(frase[9:13])
print(frase[9:21:2])  # colocar "21" não é o melhor modo de ir até o fim da frase, melhor deixar em branco #
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(frase[::2])
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

print(frase.replace('Python', 'Android'))  # Transformação: não muda a str original, apenas no uso do print #
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
frase2 = '   Aprenda Python  '
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())
print(frase.split())
print('-'.join(frase.split()))  # aqui acabam as transformações#

frase = frase.replace('Python', 'Android')  # Forma de mudar efetivamente a str original #
print(frase)
frase = frase.replace('Android', 'Python')

# Mais testes #
print(frase.upper().count('O'))
print(len(frase2), len(frase2.strip()))
print(frase.lower().find('vídeo'))
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])
