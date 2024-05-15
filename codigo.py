import random
random.seed()


continuar = "c"
while continuar == "c":
    linha = []*5
    matriz1 = [linha]*5
    matriz_para_selecao_numeros = []
    jogador1 = []
    jogador2 = []
    mat = []
    for i in range(10,61,1):
        matriz_para_selecao_numeros.append(i)
    for l in range(5):
        linha = []
        for c in range(5):
            num_aleatorio = random.choice(matriz_para_selecao_numeros) 
            matriz_para_selecao_numeros.remove(num_aleatorio)
            linha.append(num_aleatorio) 
            jogador1.append(num_aleatorio)
            matriz1[l] = linha
    print('****************'*4)
    print('****************'*4)
    nome1 = input('Qual o nome do jogador número 1? ')
    print('****************'*4)
    while nome1.isalpha() == False:
        print("----------Nome não pode ter números nem caracteres especiais:----------\n ")
        print('****************'*4)
        nome1 = input('Escreva um nome valido: ')
    print('****************'*4)
    print(' Matriz tabular\n')
    print('Cartela do(a) {}\n'.format(nome1))
    for lec in range(len(linha)):
        cart_1 = print(matriz1[lec])
    print('****************'*4)


    linha2 = []*5
    matriz2 = [linha2]*5
    matriz_para_selecao_numeros = []
    for i in range(10,61,1):
        matriz_para_selecao_numeros.append(i)
    for l in range(5):
        linha2 = []
        for c in range(5):
            num_aleatorio = random.choice(matriz_para_selecao_numeros) 
            matriz_para_selecao_numeros.remove(num_aleatorio)
            linha2.append(num_aleatorio) 
            jogador2.append(num_aleatorio)
            matriz2[l] = linha2
    print('****************'*4)
    nome2 = input('Qual o nome do jogador número 2? ')
    print('****************'*4)
    while nome2.isalpha() == False:
        print("----------Nome não pode ter números nem caracteres especiais:----------\n ")
        print('****************'*4)
        nome2 = input('Escreva um nome valido: ')
    print('****************'*4)
    print(' Matriz tabular\n')
    print('Cartela do(a) {}\n'.format(nome2))
    for lec in range(len(linha2)):
        cart_2 = print(matriz2[lec])
    print('****************'*4)
    print('****************'*4)
    matriz_para_selecao_numeros = []
    for i in range(10,61,1):
        matriz_para_selecao_numeros.append(i)
        

    op = ''
    while op == '':
        op = input('Deseja sortear um número digite (enter): ')
        print('****************'*4)
        print('****************'*4)
        while op != '':
            op = input('Deseja sortear um número digite (enter): ')
            print('****************'*4) 
        if op == '':
            num_aleatorio = random.choice(matriz_para_selecao_numeros)
            print('\n                   O número sorteado foi {}          \n'.format(num_aleatorio))
            print('****************'*4)
            for i in range(len(matriz2)):
                for ii in range(len(matriz2)):
                    if matriz1[i][ii] == num_aleatorio:
                        matriz1[i][ii] = ''
                        print('-------------------{} marcou ponto-------------------'.format(nome1))
                    if matriz2[i][ii] == num_aleatorio:
                        matriz2[i][ii] = ''
                        print('-------------------{} marcou ponto-------------------'.format(nome2))
            print('****************'*4)

            
            print('                              BINGO')
            print('Cartela do(a) {} =>)\n'.format(nome1))
            for lec in range(len(linha)):
                print(f"                      {matriz1[lec]}")
            print('****************'*4)

                
            print('                              BINGO')
            print('Cartela do(a) {} =>\n'.format(nome2))      
            for lec in range(len(linha2)):
                print(f"                      {matriz2[lec]}")
            print('****************'*4)    
                                                        
            if matriz1 == [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']] and matriz2 == [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]:
                print('Houve um empate')
                op = 'n'
            elif matriz1 == [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]:
                print('{} ganhou'.format(nome1))
                op = 'n'
            elif matriz2 == [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]:
                print('{} ganhou'.format(nome2))
                op = 'n'
            matriz_para_selecao_numeros.remove(num_aleatorio)
    print("Caso deseje jogar novamente digite c\nObservação: Qualquer outro caractere irá encerrar o programa!")
    continuar = input()