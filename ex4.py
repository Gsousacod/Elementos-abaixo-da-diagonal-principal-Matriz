matriz =  [ [0,0,0], [0,0,0], [0,0,0]]
lista_adiagonal = []
for i in range (0,3):
    for j in range(0,3):
        matriz[i][j] = int(input("Digite um elemento:"))
        if(i>j):
             lista_adiagonal.append(matriz[i][j])
print('<<>>'*5)
for i in range (0,3):
        for j in range(0,3):
                print(f'[{matriz[i] [j] :^5}]', end = "")
        print()
print('<<>>'*5)
print(matriz)
print('<<>>'*5)
print(lista_adiagonal)