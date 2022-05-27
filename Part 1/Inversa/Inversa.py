# Implementação do método de Eliminação de Gauss
# Autor: Fabiano Silva dos Santos

import numpy as np
import fractions as ft

# Realizando a abertura dos arquivos de entrada e saída
entrada = open('arquivo_entrada.txt', 'r')
saida = open('arquivo_saida.txt', 'w')

# Preparando matrizes a partir do arquivo de entrada
linhas = entrada.readlines()
matriz = [[ft.Fraction(valor) for valor in linha.split()] for linha in linhas]
b = [linha.pop(-1) for linha in matriz]

def Pivoteamento(matriz):
    '''Realiza o pivoteamento da matriz na diagonal principal.
    Parâmetros: matriz - matriz em que será feito o pivoteamento.
    '''

    n_linhas, n_colunas = len(matriz), len(matriz[0])

    # Verifica os valores da diagonal principal e troca as linhas onde houve o valor 0
    for i in range(n_linhas):
        if matriz[i][i] == 0:
            elementos = [matriz[j][i] for j in range(n_linhas)]            
            matriz[i], matriz[elementos.index(max(elementos))] = matriz[elementos.index(max(elementos))], matriz[i]

def InversaGaussJordan(matriz):
    '''Realiza o cálculo da inversa a partir do método de Gauss-Jordan.
    Parâmetros: matriz - matriz que será calculada a inversa.
    Retorno: inversa - matriz inversa calculada.
    '''

    Pivoteamento(matriz)
    n_linhas, n_colunas = len(matriz), len(matriz[0])

    # Cria a matriz identidade e a junta com a matriz original
    identidade = [[1 if i == j else 0 for i in range(n_linhas)] for j in range(n_colunas)]
    matriz_completa = [matriz[j] + identidade[j] for j in range(n_linhas)]

    # Aplica o método de Gauss na matriz completa
    for i in range(n_linhas):
        pivo = matriz_completa[i][i] 

        for j in range(n_colunas*2):
            matriz_completa[i][j] /= pivo

        pivo = matriz_completa[i][i]

        for j in range(n_linhas):
            if j == i: continue

            m = matriz_completa[j][i] / pivo

            for k in range(n_colunas*2):
                matriz_completa[j][k] = matriz_completa[j][k] - (m * matriz_completa[i][k])

    matriz_completa = [[float(valor) for valor in linha] for linha in matriz_completa]

    # Separa a inversa da matriz completa
    inversa = [linha[int(len(linha)/2):] for linha in matriz_completa]

    return inversa
    
    
if __name__ == '__main__':
    inversa = InversaGaussJordan(matriz)

    # Escreve o resultado na saída
    saida.write('Inversa:\n')
    for linha in inversa:
        saida.write(f'{linha}\n')
