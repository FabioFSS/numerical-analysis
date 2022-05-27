from FatoracaoLU import FatoracaoLU
from sympy import integrate, Symbol, Mul
from sympy.abc import x
from fractions import Fraction

def MMQContinuo(funcao, intervalo, pontosy=None):
    # calcula os vetores u em determinado grau
    grau = 2
    u = []
    b = []

    if pontosy != None:
        b = pontosy

    for i in range(grau+1):
        if i == 0: stringy = '1'
        else: stringy = f'x**{i}'
        b.append(Mul(eval(funcao), eval(stringy)))
        temp = []
        for j in range(grau+1):
            if j == 0: stringx = '1'
            else: stringx = f'x**{j}'
            temp.append(Mul(eval(stringx), eval(stringy)))

        u.append(temp)

    # calcula os produtos escalares
    for i in range(grau+1):
        b[i] = integrate(b[i], (x, intervalo[0], intervalo[1]))
        for j in range(grau+1):
            u[i][j] = integrate(u[i][j], (x, intervalo[0], intervalo[1]))

    print(u)

    # realiza o calculo do resultado da matriz utilizando Fatoracao LU
    matriz_completa = [u[i].copy() for i in range(len(u))]
    for i in range(len(u)): matriz_completa[i].append(b[i])
    matriz, mL, mU, mTempResultado, resultado = FatoracaoLU(matriz_completa)

    return resultado



if __name__ == '__main__':
    # faz a leitura dos pontos do arquivo de entrada
    with open('arquivo_entrada.txt', 'r') as file:
        funcao = file.readline().strip()
        intervalo = file.readline().split()
        intervalo = [Fraction(valor) for valor in intervalo]
        
    res = MMQContinuo(funcao, intervalo)

    # faz a escrita no arquivo de saida
    with open('arquivo_saida.txt', 'w') as file:
        file.write(f'Polinomio: {res[0]}')
        for i in range(1, len(res)):
            file.write(f' + {res[i]}x**{i}')
