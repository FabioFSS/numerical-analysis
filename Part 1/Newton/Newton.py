# Implementação do método de Newton
# Autor: Fabiano Silva dos Santos

from sympy import diff, Symbol
from math import e, pi, tan, sin, cos, log
from matplotlib import pyplot as pp

# Realizando a abertura dos arquivos de entrada e saída
entrada = open('arquivo_entrada.txt', 'r')
saida = open('arquivo_saida.txt', 'w')

# Realiza a leitura da função em texto e criação da 
# função equivalente em python
expr = entrada.readline()
Funcao = lambda x: eval(expr)

x = Symbol('x')
diff = diff(expr, x)
Funcao_diff = lambda x: eval(str(diff))

# Leitura dos valores de intervalo inicial a e b, e
# limite de precisão horizontal e vertical
a_inicial = float(entrada.readline())
b_inicial = float(entrada.readline())
PRECISAO = float(entrada.readline())

c_inicial = (a_inicial + b_inicial) / 2 # Ponto médio entre a e b, que será o valor inicial

lista_fc = [] # Lista de valores de f(c)

it = 0 # Número de iterações

def Newton(c):
    global it
    it += 1
    
    # Realiza o cálculo do novo c
    c = c - (Funcao(c) / Funcao_diff(c))
    lista_fc.append(Funcao(c))

    # Verifica a condição de parada e chama recursivamente a função
    if abs(Funcao(c)) > PRECISAO: c, fc = Newton(c)

    return c, Funcao(c)

if __name__ == '__main__':
    c, fc = Newton(c_inicial)

    # Escrevendo resultados na saída
    saida.write(f'c: {c}\nf(c): {fc}\niteracoes: {it}')

    # Plotando gráfico de f(c)
    pp.plot(lista_fc)
    pp.savefig('grafico_fc.jpg')
