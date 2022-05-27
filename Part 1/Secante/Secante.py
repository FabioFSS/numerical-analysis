# Implementação do método de Secante
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

# Leitura dos valores de intervalo inicial a e b, e
# limite de precisão horizontal e vertical
a_inicial = float(entrada.readline())
b_inicial = float(entrada.readline())
PRECISAO = float(entrada.readline())

lista_fc = [] # Lista de valores de f(c)

it = 0 # Número de iterações

def Secante(c, ca):
    global it
    it += 1

    # Realiza o cálculo do novo c
    c_novo = c - ((Funcao(c) * (c - ca)) / (Funcao(c) - Funcao(ca)))
    lista_fc.append(Funcao(c_novo))
    
    # Verifica a condição de parada e chama recursivamente a função
    if abs(Funcao(c_novo)) > PRECISAO: c_novo = Secante(c_novo, c)
    
    return c_novo

if __name__ == '__main__':
    c = Secante(a_inicial, b_inicial)

    # Escrevendo resultados na saída
    saida.write(f'c: {c}\nf(c): {Funcao(c)}')
    saida.write(f'\niteracoes: {it}')

    # Plotando gráfico de f(c)
    pp.plot(lista_fc)
    pp.savefig('grafico_fc')