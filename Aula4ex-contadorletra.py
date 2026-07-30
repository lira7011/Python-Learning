palavra = input('digite uma palavra!') #pego palavra e peço uma str de variavel para entrada

contador = 0 #afirmo número 1 como começo da contagem para variavel
for letra in palavra: #para cada 'letra em palavra':
    contador = contador + 1  #use o contador começando de zero e adicione +1(pegue o contador inciando em 0 e para cada letra na palavra adicione +1 até o final dela)

print(f'A palavra tem {contador} letras') #mostre o contador final