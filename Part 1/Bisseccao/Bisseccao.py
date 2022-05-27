# Implementação do método da bissecção
# Autor: Fabiano Silva dos Santos

from math import sin, e, tan, cos, pi
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

def Bisseccao(a, b):
    '''Encontra a raiz da função a partir de um determinado intervalo
    utilizando o método da bissecção.

    Parâmetros: a - intervalo da esquerda
                b - intervalo da direita.

    Retorno: final - lista com valores de a, b, c e suas imagens com a
                    função.
    '''

    global it
    it += 1 

    # Realiza os cálculos necessários do método de Bissecção
    c = (a+b)/2
    ra, rb, rc = Funcao(a), Funcao(b), Funcao(c)
    lista_fc.append(rc)
    erro_relativo = (b-a)/a
    
    final = [ra, rb, rc, a, b, c]

    # Verifica a condilção de parada e chama recursivamente o método
    if abs(erro_relativo) > LIMITE_HORIZONTAL and abs(rb) > LIMITE_VERTICAL and rc != 0:
        if ra*rc < 0: final = Bisseccao(a, c)
        else: final = Bisseccao(c, b)

    return final

if __name__ == '__main__':
    res = Bisseccao(a_inicial, b_inicial)
    
    # Escrevendo o resultado no arquivo de saída
    saida.write(f'a: {res[3]}\nb: {res[4]}\nc: {res[5]}\n')
    saida.write(f'f(a): {res[0]}\nf(b): {res[1]}\nf(c): {res[2]}\n')
    saida.write(f'iteracoes: {it}')

    # Plotando e salvando gráfico de f(c)
    pp.plot(lista_fc)
    pp.savefig('grafico_fc')