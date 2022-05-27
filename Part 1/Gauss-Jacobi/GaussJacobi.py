# Implementação do método de Gauss Jacobi
# Autor: Fabiano Silva dos Santos

import numpy as np
import fractions as ft

# Realizando a abertura dos arquivos de entrada e saída
entrada = open('arquivo_entrada.txt', 'r')
saida = open('arquivo_saida.txt', 'w')


PRECISAO = float(entrada.readline())

# Preparando matrizes a partir do arquivo de entrada
linhas = entrada.readlines()
matriz = [[ft.Fraction(valor) for valor in linha.split()] for linha in linhas]
b = [linha.pop(-1) for linha in matriz]
matriz_original = [linha.copy() for linha in matriz]
b_original = b.copy()


def NormaVetor(vetor, x):
    '''Calcula a norma de um vetor.
    Parâmetros: vetor - vetor que será calculada a norma.
                x - segundo vetor para cálculo da norma.
    Retorno: maxnum/maxden - norma do vetor.
    '''

    tam = len(vetor)

    # Calcula os máximos numeradores e denominadores
    maxnum = max([abs(vetor[i] - x[i]) for i in range(tam)])
    maxden = max([abs(vetor[i]) for i in range(tam)])

    return maxnum/maxden

def GaussJacobi(matriz, b, precisao, iterMax=50):
    '''Realiza o método de Gauss-Jacobi.
    Parâmetros: matriz - matriz em que será aplicada o método.
                b - resultados do sistema da matriz.
                precisao - precisao desejada.
                iterMax - máximo de iterações.
    Retornos: v - vetor de resultados.
    '''

    tam = len(matriz)
    x = [0 for i in range(tam)]
    v = [0 for i in range(tam)]

    for i in range(tam):
        for j in range(tam):
            if i != j:
                matriz[i][j] = matriz[i][j]/matriz[i][i]
                
        b[i] = b[i]/matriz[i][i]
        x[i] = b[i]
    
    for k in range(1, iterMax+1):
        for i in range(tam):
            S = 0
            for j in range(tam):
                if i != j:
                    S = S + matriz[i][j] * x[j]
            v[i] = b[i] - S
        d = NormaVetor(v, x)
        if d <= precisao:
            return v

        x = v[:]

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
    resultado = GaussJacobi(matriz, b, PRECISAO, 1000)

    # Transforma os valores para float
    resultado = [float(valor) for valor in resultado]

    # Escreve os resultados na saída
    saida.write(f'Resultado [X1, X2, X3, ..., Xn]:\n{resultado}')

    # Realiza o teste dos resultados obtidos
    teste = TestaResultados(matriz_original, resultado)
    teste = [float(valor) for valor in teste]

    # Escreve os resultados do teste em um arquivo
    with open('teste_resultados.txt', 'w') as file:
        for i in range(len(teste)):
            file.write(f'{teste[i]} = {float(b[i])}\n')