while True: #Loop que assume valor verdade rodar sempre
    tabuada = int(input('Insira um número de 1 a 10')) #pego termo tabuada, atribuo valor de inteiro, peço um número de entrada
    for n in range(0,11): #loop que para n em um intervalo de 0 a 11 faz:
        resultado = tabuada * n #faz um resultado que é a tabuada(número inteiro que pediu no começo) '*' que é x o n 
        print(f'{tabuada} x {n} = {resultado}') #torno o código visivel, coloco 2 variaveis, 'tabuada' e 'n' com um termo str(string) x para simbolizar multiplicação, e outro '=' para resultado.
        


