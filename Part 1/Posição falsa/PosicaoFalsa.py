# Implementação do método da Posição Falsa
# Autor: Fabiano Silva dos Santos

from math import sin, e, cos, pi, tan
import matplotlib.pyplot as pp


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
LIMITE_HORIZONTAL = float(entrada.readline())
LIMITE_VERTICAL = LIMITE_HORIZONTAL

lista_fc = [] # Lista de valores de f(c)

it = 0 # Número de iterações

def PosicaoFalsa(a, b):
    global it
    it += 1

    # Realiza os cálculos necessários para o método da Posição Falsa
    ra, rb = Funcao(a), Funcao(b)
    c = (a * rb - b * ra) / (rb - ra)
    rc = Funcao(c)
    erro_relativo = (b-a)/a
    final = [ra, rb, rc, a, b, c]

    lista_fc.append(rc)

    # Verifica a condição de parada e chama o método recursivamente
    if abs(erro_relativo) > LIMITE_HORIZONTAL and abs(rb) > LIMITE_VERTICAL and rc != 0:
        if ra*rc < 0: final = PosicaoFalsa(a, c)
        else: final = PosicaoFalsa(c, b)

    return final

if __name__ == '__main__':
    res = PosicaoFalsa(a_inicial, b_inicial)
    
    # Escrevendo o resultado no arquivo de saída
    saida.write(f'a: {res[3]}\nb: {res[4]}\nc: {res[5]}\n')
    saida.write(f'f(a): {res[0]}\nf(b): {res[1]}\nf(c): {res[2]}\n')
    saida.write(f'iteracoes: {it}')

    # Plotando e salvando gráfico de f(c)
    pp.plot(lista_fc)
    pp.savefig('grafico_fc')