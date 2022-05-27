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
matriz_original = [linha.copy() for linha in matriz]
b = [linha.pop(-1) for linha in matriz_original]


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

def EliminacaodeGauss(matriz):
    '''Realiza a eliminação de Gauss em uma matriz.
    Parâmetros: matriz - matriz em que será feita a eliminação de Gauss.
    Retorna:    resultado - vetor de resultados dos valores de x1, x2, ..., xn.
                matriz - matriz modificada.
    '''

    Pivoteamento(matriz)
    n_linhas, n_colunas = len(matriz), len(matriz[0])

    # Aplica o algoritmo de eliminação de Gauss.
    # Primeiro é escolhido um pivô, em seguida um multiplicador
    # e então aplicada a fórmula nos valores da linha.
    for i in range(n_linhas-1):
        pivo = matriz[i][i]

        for j in range(i+1, n_linhas):
            m = matriz[j][i] / pivo

            for k in range(n_colunas):
                matriz[j][k] = matriz[j][k] - (m * matriz[i][k])

    resultado = ResolveSistema(matriz)

    return resultado, matriz 
    
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
    resultado, matriz = EliminacaodeGauss(matriz)

    # Transforma os valores da matriz para float
    resultado = [float(valor) for valor in resultado]
    matriz = [[float(valor) for valor in linha] for linha in matriz]

    # Escreve os resultados na saóda
    saida.write(f'Matriz:\n{matriz}\n\nResultado [x1, x2, x3, ..., xn]:\n{resultado}')

    # Realiza o teste dos resultados obtidos
    teste = TestaResultados(matriz_original, resultado)
    teste = [float(valor) for valor in teste]

    # Escreve os resultados do teste em um arquivo
    with open('teste_resultados.txt', 'w') as file:
        for i in range(len(teste)):
            file.write(f'{teste[i]} = {float(b[i])}\n')