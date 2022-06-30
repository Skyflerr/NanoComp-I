"""
Lista de revisão

Eduardo da Fonseca (Skye)
Turma de Nanotecnologia
"""

# 1 - Representando a função z(x), insira um numero real entre 0 e 11
def ZdeX(x):
    if x<0 or x>11:
        return "X está fora do escopo de numeros reais"
    if x>=0 and x<=3:
        return x**2
    elif x>3 and x<=5:
        return 9-x
    elif x>5 and x<=9:
        return 4
    elif x>9 and x<=11:
        return x**3 - 4

# 2 

# 3.1 - Insira uma string, a função retornara-la invertida , exemplo : "hello" -> "olleh"
def stringreverse(s):
    return s[::-1]

# 3.2 - Insira um numero inteiro, a função retornara-lo invertido, exemplo : 123 -> 321
def integerreverse(i):
    aux = str(i)
    return aux[::-1]

# 3.3 - Insira uma lista, a função retornara-la invertida, exemplo : 1,2,3,4,5 -> 5,4,3,2,1
def listreverse(l):
    return l.reverse()

# 4
def lojadetintas(metrosquadrados):
    """1 Litro -> 3 metros quadrados"""
    litros = int(metrosquadrados / 3)

# 5

# 6 - Insira uma string a função retornara quantas palavras ela possui 
def wordcount(s):
    return len(s.split())
