import random
random.seed()
linha = []*5
matriz1 = [linha]*5
tot = []
jogador1 = []
jogador2 = []
mat = []
for i in range(10,61,1):
    tot.append(i)
for l in range(5):
    linha = []
    for c in range(5):
        num_aleatorio = random.choice(tot) 
        tot.remove(num_aleatorio)
        linha.append(num_aleatorio) 
        jogador1.append(num_aleatorio)
        matriz1[l] = linha
print('****************'*4)
print('****************'*4)
nome = input('qual o nome do jogador numero 1?')
print('****************'*4)
while nome.isalpha() == False:
  print("----------nome não pode ter numeros nem caracteres especiais:----------\n ")
  print('****************'*4)
  nome = input('escreva um nome valido: ')
print('****************'*4)
print(' matriz tabular\n')
print('cartela do(a) {}\n'.format(nome))
for lec in range(len(linha)):
    cart_1 = print(matriz1[lec])
print('****************'*4)
linha2 = []*5
matriz = [linha2]*5
tot = []
for i in range(10,61,1):
    tot.append(i)
for l in range(5):
    linha2 = []
    for c in range(5):
        num_aleatorio = random.choice(tot) 
        tot.remove(num_aleatorio)
        linha2.append(num_aleatorio) 
        jogador2.append(num_aleatorio)
        matriz[l] = linha2
print('****************'*4)
nome2 = input('qual o nome do jogador numero 2?')
print('****************'*4)
while nome2.isalpha() == False:
  print("----------nome não pode ter numeros nem caracteres especiais:----------\n ")
  print('****************'*4)
  nome2 = input('escreva um nome valido: ')
print('****************'*4)
print(' matriz tabular\n')
print('cartela do(a) {}\n'.format(nome2))
for lec in range(len(linha2)):
    cart_2 = print(matriz[lec])
print('****************'*4)
print('****************'*4)
tot = []
for i in range(10,61,1):
    tot.append(i)
op = ''
while op == '':
    op = input('deseja sortear um numero digite (enter): ')
    print('****************'*4)
    print('****************'*4)
    while op != '':
       op = input('deseja sortear um numero digite (enter): ')
       print('****************'*4) 
    if op == '':
        num_aleatorio = random.choice(tot)
        for i in range(len(matriz)):
            for ii in range(len(matriz)):
                if matriz1[i][ii] == num_aleatorio:
                    matriz1[i][ii] = ''
                    print('-------------------{} marcou ponto-------------------'.format(nome))
                if matriz[i][ii] == num_aleatorio:
                    matriz[i][ii] = ''
                    print('-------------------{} marcou ponto-------------------'.format(nome2))
        print('****************'*4)
        print('\n                   o número sorteado foi {}          \n'.format(num_aleatorio))
        print('****************'*4)
        print('                              BINGO')
        print('cartela do(a) {} =>)\n'.format(nome))
        for lec in range(len(linha)):
            print(f"                      {matriz1[lec]}")
        print('****************'*4)
        print('\n                   o número sorteado foi {}          \n'.format(num_aleatorio))
        print('****************'*4)
        print('                              BINGO')
        print('cartela do(a) {} =>\n'.format(nome2))      
        for lec in range(len(linha2)):
            print(f"                      {matriz[lec]}")
        print('****************'*4)                                       
        if matriz1 == [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']] and matriz == [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]:
            print('houve um empate')
            op = 'n'
        elif matriz1 == [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]:
            print('{} ganhou'.format(nome))
            op = 'n'
        elif matriz == [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]:
            print('{} ganhou'.format(nome2))
            op = 'n'
        tot.remove(num_aleatorio)