frutas = ('maça','banana','laranja','uva') #tupla que se identifica por () e não são alteradas, tendo que transformar em listas para poder alterar, e depois tuplas novamente.

if 'banana' in frutas: #if=se tiver o termo 'banana' na tupla referente que é 'in' 'frutas', então 'print'(mostre 'tem banana na lista')
    print('tem banana na lista!') 
else: #else=se não, mostre 'vish, tem nao'
    print('vish, tem não')

frutas = list(frutas) #transoforma a tupla em lista para poder alterar seu conteudo
frutas.append('abacaxi') #adiciona o abacaxi na lista
frutas = tuple(frutas) #transforma a lista em tupla novamente

print(frutas) #mostra o resultado final de todas modificações feitas

#obs, tuplas podem ter listas, dicionarios e outras tuplas dentro de si 