# Implementação do método de Fatoração LU
# Autor: Fabiano Silva dos Santos

import numpy as np
import fractions as ft


def ResolveSistema(matriz):
    '''Resolve um sistema a partir de uma matriz do sistema.
    Parâmetros: matriz - matriz que será utilizada para resolver o sistema.
    Retorno: resultado - resultado dos valores x1, x2, ..., xn da matriz.
    '''

    tam = len(matriz)
    
    # Cria o vetor de resultados e calcula o primeiro valor
    resultado = [None for i in range(tam)]
    resultado[-1] = matriz[-1][-1] / matriz[-1][-2]

    # Aplica retro substituição
    for i in range(tam-1, -1, -1):
        s = 0

        for j in range(i+1, tam):
            s = s + (matriz[i][j] * resultado[j])
            resultado[i] = (matriz[i][-1] - s) / matriz[i][i]

    return resultado

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

def FatoracaoLU(matriz):
    '''Realiza a fatoração LU em uma matriz.
    Parâmetros: matriz - matriz em que será feita a fatoração LU.
    Retorna:    resultado - vetor de resultados dos valores de x1, x2, ..., xn.
                matriz - matriz modificada.
    '''

    Pivoteamento(matriz)
    n_linhas, n_colunas = len(matriz), len(matriz[0])

    # Cria a matriz L
    mL = [[1 if i == j else 0 for i in range(n_colunas-1)] for j in range(n_linhas)]

    # Realiza os calculos na matriz para encontrar a matriz L
    for i in range(n_linhas-1):
        pivo = matriz[i][i]

        for j in range(i+1, n_linhas):
            m = matriz[j][i] / pivo
            mL[j][i] = m

            for k in range(n_colunas-1):
                matriz[j][k] = matriz[j][k] - (m * matriz[i][k])

    # Cria a matriz U
    mU = [[matriz[i][j] if j >= i else 0 for j in range(n_colunas-1)] for i in range(n_linhas)]

    # Resolve a matriz L
    mTemp = [linha.copy() for linha in mL]
    for i in range(len(mTemp)): mTemp[i].reverse()
    for i in range(n_linhas): mTemp[i] += [matriz[i][-1]]
    mTemp.reverse()
    mTempResultado = ResolveSistema(mTemp)
    mTempResultado.reverse()

    # Resolve a matriz U
    mTemp = [linha.copy() for linha in mU]
    for i in range(n_linhas): mTemp[i] += [mTempResultado[i]]
    resultado = ResolveSistema(mTemp)

    return resultado
    
def TestaResultados(matriz, resultados):
    '''Testa os valores da matriz com um vetor de resultados.
    Parâmetros: matriz - matriz que será testada.
                resultados - vetor de resultados.
    Retorno: resultados_teste - matriz com os resultados do teste.
    '''
    
    resultados_teste = []
    for linha in matriz:
        s = 0
        for i in range(len(linha)):
            if linha[i] != 0:
                s += linha[i]*resultados[i]

        resultados_teste.append(s)

    return resultados_teste

if __name__ == '__main__':
    
    # Realizando a abertura dos arquivos de entrada e saída
    entrada = open('arquivo_entrada.txt', 'r')
    saida = open('arquivo_saida.txt', 'w')

    # Preparando matrizes a partir do arquivo de entrada
    linhas = entrada.readlines()
    matriz = [[ft.Fraction(valor) for valor in linha.split()] for linha in linhas]
    matriz_original = [linha.copy() for linha in matriz]
    b = [linha.pop(-1) for linha in matriz_original]

    matriz, mL, mU, mTempResultado, resultado = FatoracaoLU(matriz)

    # Transforma os valores para float
    matriz = [[float(valor) for valor in linha] for linha in matriz]
    mL = [[float(valor) for valor in linha] for linha in mL]
    mU = [[float(valor) for valor in linha] for linha in mU]
    mTempResultado = [float(valor) for valor in mTempResultado]
    resultado = [float(valor) for valor in resultado]

    # Escreve os resultados na saída
    saida.write(f'Matriz:\n{matriz}\n\nMatriz L:\n{mL}\n\nMatriz U:\n{mU}\n\n')
    saida.write(f'L x Y = B [Y1, Y2, Y3, ..., Yn]:\n{mTempResultado}\n\n')
    saida.write(f'U x X = Y [X1, X2, X3, ..., Xn]:\n{resultado}')

    # Realiza o teste dos resultados obtidos
    teste = TestaResultados(matriz_original, resultado)
    teste = [float(valor) for valor in teste]

    # Escreve os resultados do teste em um arquivo
    with open('teste_resultados.txt', 'w') as file:
        for i in range(len(teste)):
            file.write(f'{teste[i]} = {float(b[i])}\n')