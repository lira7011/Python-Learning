aluno = {'nome': 'Maria', 'idade': 20, 'curso': 'engenharia'} #dicionarios, identificados por {}, guardam o conteudo referente a uma chave especifica, assim como nas div, guardam informações, como nome = cleiton

aluno['nota'] = 9.5 #adiciona a chave nota, dizendo que o valor dessa nota é 9.5
aluno['idade'] = 21 #adiciona a chave idade, atribue o valor de 21 
aluno.pop('curso') #remove a chave de curso

aluno['curso'] = ['psicologia', 'fisica', 'matematica'] #adiciona uma nova chave tambem chamada curso, porem com 3 novos em formato de listas e em outra posição!

print(aluno) #Mostra o resultado final de todas modificações feitas no dicionario.

#obs, dicionarios podem ter listas, tuplas e outros dicionarios dentro de si 