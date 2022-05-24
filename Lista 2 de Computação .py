# Lista de Exercicios 2
# Eduardo da Fonseca (Skye)
# Turma de Nanotecnologia

import math

# 0. Detector de Colisão, inserindo as cordenadas das diagonais de dois retangulos
# retorna true se há colisão ou false se não há
def Colision(x1,y1,x2,y2,x3,y3,x4,y4):
  if x1 > x4 or y1 > y4 or x2 > x3 or y2 > y3:
    return True
  else: 
    return False

# 1. Recebe valores int e retorna seu valor absoluto
def ValorAbsoluto(x):
  if x > 0 :
    return x
  else : 
    return x * (-1)

# 2. Função que retorna as duas raizes, se existirem, de uma equação do segundo grau
def delta(a,b,c):
  return (b ** 2) - (4 * a * c)

def RaizUm(a,b,c):
  if delta(a,b,c) >= 0:
    return ((b * -1) + math.sqrt(delta(a,b,c))) / (2 * a)
  if delta(a,b,c) < 0:
    return "não existe"

def RaizDois(a,b,c):
  if delta(a,b,c) >= 0: 
    return ((b * -1) - math.sqrt(delta(a,b,c))) / (2 * a)
  if delta(a,b,c) < 0:
    return "não existe"

# 3. Recebe um texto e repete-o quantas vezes você quiser, insira quantas vezes quer que repita, e o texto
def TextRepeat(n,texto):
  result = ""
  for x in range(1,int(n) + 1):
    result += (str(texto) + ", ")
  
  return result

# 4. Inserindo dia mes e ano, retorna um modelo de data dd/mm/aa
def Calendario(dia,mes,ano):
  def MesOuDiaComDigitoUnico(x):
    if x < 10 :
      return '0' + str(x)
    else :
      return x

  data = str(MesOuDiaComDigitoUnico(dia)) + "/" + str(MesOuDiaComDigitoUnico(mes)) + "/" + str(ano)
  return data

# 5. Função que tem comportamento da função matematica da figura da lista
def FuncaoMatematica(x):
  if x < 0:
     return 0
  if x <= 2:
    return x
  if 2 <= x <= 3.5:
    return 2.0
  if 5 >= x > 3.5:
    return 3.0
  if x > 5:
    return x ** 2 - 10 * + 28

# 6.1 Calcula o desconto do INSS, entrando com salario bruto, de acordo com a formula 
def INSS(s):
  if s <= 2000:
    return (0.06 * s)
  elif s <= 3000:
    return (0.08 * s)
  elif s > 3000:
    return (0.1 * s)

# 6.2 Calcula o desconto do imposto de renda, entrando com salario bruto,  de acordo com a tabela
def IR(s):
  if s <= 2500:
    return (0.11 * s)
  elif s <= 5000:
    return (0.15 * s)
  elif s > 5000:
    return (0.22 * s)

# 6.3 Calcula o valor do salario liquido, entrando com salario bruto, apartir das funções anteriores
def SL(s):
  return s - (INSS(s) + IR(s))