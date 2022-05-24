Nome : Eduardo da Fonseca (Skye)
Curso : Nanotecnologia

# ---Exercicios do arquivo "lab1.pdf" 6,7,10,11---

import math

#Exercicio 6 - Média Ponderada de dois numeros
def mediaponderada (n1,n2,peso1,peso2):
  """Insira os dados como : primeiro numero, segundo numero logo apos insira respectivamente o peso do primeiro numero e do
  segundo numero"""
  return float((peso1 * n1) + (peso2 * n2) / peso1 + peso2)

#Exercicio 7 - Erro entre o valor da soma de uma PG infinita e outra finita
def errodePG(n,q,a):
  a = 1.0
  return 1 / (1 - q) - a *(1 - q ** n) / (1 - q)

#Exercicio 10 - Calcular o saldo final de uma conta dado saldo inicial, numero de meses e taixa de juros
def SaldoFinaldaConta(Si,Nm,j):
  """Entre como o saldo inicial, numero de meses e taixa de juros e sera calculado o saldo final"""
  return Si * (1 + j * Nm / 100)

#Exercicio 11 - Calcular a distancia que a correnteza arrasta um barco que atravessa um rio.
def Correnteza(correnteza,largura,velocidadedobarco):
  """Entre com o valor da correnteza, a largura do rio e a velocidade do barco e sera calculada a distancia que a correnteza arrastou um barco"""
  return float(correnteza * (largura / velocidadedobarco))


# ---Exercicios do arquivo "lab2_IDLE.pdf"---

#Exercicio 1.a - testar as funções min e max
min(3,5,10)
max(3,5,10)

#Exercicio 1.b - Calcular a media de 3 numeros inteiros
def media(n1,n2,n3):
  """Entre com três numeros inteiros e sera calculada a media deles"""
  return (n1 + n2 + n3) / 3

#Exercicio 1.c - Calcular a diferença do maior deles com a media dos 3 numeros
def mediadois(x1,x2,x3):
  """Entre com tres numeros inteiros, e sera calculada a diferença entre o maior deles e a media dos tres"""
  return (media(x1,x2,x3) - max(x1,x2,x3))

#Exercicio 1.d - Calcular a diferença do menor deles com a media dos 3 numeros
def mediatres(x1,x2,x3):
  """Entre com tres numeros inteiros, e sera calculada a diferença entre o menor deles e a media dos tres"""
  return (media(x1,x2,x3) - min(x1,x2,x3))

#Exercicio 2.a - Calcular o discriminante dado os coeficiente a, b e c
def delta(a,b,c):
  """Entre os coeficientes a, b e c e sera calculada delta"""
  return (b ** 2) - (4 * a * c)

#Exercicio 2.b - Calcule a primeira raiz real de uma equação do segundo grau dado a, b e c
def primeiraraiz(a,b,c):
  """Entre com os coeficientes a,b e c e sera calculada a primeira raiz de bhaskara deles"""
  return ((b * -1) + math.sqrt(delta(a,b,c))) / (2 * a)

#Exercicio 2.c -  Calcule a segunda raiz real de uma equação do segundo grau dado a, b e c
def segundaraiz(a,b,c):
  """Entre com os coeficientes a,b e c e sera calculada a segunda raiz de bhaskara deles"""
  return ((b * -1) - math.sqrt(delta(a,b,c))) / (2 * a)

#Exercicio 3.b - Calcule o numero de termos  dados os valores inicial, final e razão
def Pa(a1,an,r):
  """Entre com valor inicial, o final e a razão e será calculado o numero de termos de uma PA"""
  return (an - a1) / r + 1 

#Exercicio 3.c - Calcule a soma da PA dados os valores inicial, final e razão
def PaDois(a1,an,r):
  """Entre com valor inicial, o final e a razão, e será calculada a soma de uma PA"""
  n = (an - a1) / r + 1 
  return (a1 + an) * n / 2

#Exercicio 4.a - Calcule a distancia entre dois pontos em um plano dadas suas coordenadas
def dist2ptos(x1,y1,x2,y2):
    """Entre com as coordenadas de dois pontos em um plano, e a distancia entre eles será calculada"""
    l1 = x2 - x1
    l2 = y2 - y1
    return math.hypot(l1, l2)

#Exercicio 4.b - Calcule o perimetro de um triangulo reto dado os catetos
def perimetro(l1,l2):
  """Entre com os catetos de um triangulo retangulo e será calculado o perimetro do triangulo"""
  return (math.sqrt(l1 ** 2 + l2 ** 2)) + l1 + l2

#Exercicio 4.c - Calcule a soma do quadrado do seno com o quadrado do cosseno de um angulo
def somaSinCos(ang):
    """Entre com o valor de um angulo, e será calculada a soma do quadrado do seno com o quadrado do cosseno do angulo"""
    ang = math.radians(ang)
    soma = math.sin(ang) ** 2 + math.cos(ang) ** 2
    return soma

#Exercicio 5 - Calcule a area de um setor circular, dados o raio e o angulo, usando argumento default para o angulo,
#se nao ouver angulo a função retorne a area do circulo inteiro
def setorCircular(raio,angulo = 360):
    """Entre com o raio e se possivel o angulo, e será calculada a area do setor circular"""
    angulo = math.radians(angulo)
    return angulo * raio ** 2