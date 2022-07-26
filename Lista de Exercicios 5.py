 """
 Lista de exercicios 5

 Eduardo da Fonseca Oliveira (Skye)
 Nanotecnologia
 
 """
 
 # Matrizes de exemplo usadas
 matrix = [[10, 13, 44], [11, 2, 3], [5, 3, 1]] 
 matrix2 = [[7, 16, -6], [9, 20, -4],  [-1, 3 , 27]]

# Questão 2
# Recebe duas matrizes(lista de listas) e retorna a soma delas 
 def matrixsum(m1,m2):
    result = [[0,0,0],[0,0,0],[0,0,0]]
    for x in range(0,(len(m1))):
        for y in range(0,(len(m2))):
            result[x][y] = m1[x][y] + m2[x][y]
    return result

# Questão 3
# Recebe duas matrizes(lista de listas) e retorna a subtração delas
 def matrixsubtraction(m1,m2):
    result = [[0,0,0],[0,0,0],[0,0,0]]
    for x in range(0,(len(m1))):
        for y in range(0,(len(m2))):
            result[x][y] = m1[x][y] - m2[x][y]
    return result

# Questão 4
# Recebe uma matriz e a multiplica por um numero inteiro, retorna a matriz com os valores multiplicados
def matrixmultiply(m,c):
    result = [[0,0,0],[0,0,0],[0,0,0]]
    for x in range(0,(len(m))):
        for y in range(0,3):
            result[x][y] = m[x][y] * c
    return result
