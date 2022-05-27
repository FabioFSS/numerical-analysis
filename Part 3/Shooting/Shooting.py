from RungeKutta4 import runge_kutta4
from matplotlib import pyplot as pt

def shooting(funcoes, pontos1, pontos2, param, h, ordem) -> float:
    '''
    Aplica o método de Shooting para solução de equações diferenciais.
    
    Parâmetros:
        funcoes (list): as funcoes que serão aplicadas
        pontos1 (list): a lista com os pontos que serão tomados como referência
        no primeiro chute
        pontos2 (list): a lista com os pontos que serão tomados como referência
        no segundo chute
        param(list): valores que serão tomados como parâmetro para a regra de 3
        h (float): o intervalo entre os pontos que será calculado
        ordem (int): a ordem do ponto desejado

    Retorno:
        resultado (float): o resultado estimado da equação diferencial
    '''

    res1, hist1 = runge_kutta4(funcoes, pontos1, h, ordem)
    res2, hist2 = runge_kutta4(funcoes, pontos2, h, ordem)

    resultado = pontos1[1][1] + ((pontos2[1][1] - pontos1[1][1])/(res2[0] - res1[0])) * (param[1] - res1[0])
    r4resultado = runge_kutta4(funcoes, [pontos1[0], [pontos1[0][0], resultado]], h, ordem)

    return resultado, r4resultado, hist1, hist2 

def grafico(solucao, nome_arquivo='grafico.jpg'):
    if len(solucao[0]) == 2:
        x = [ponto[0] for ponto in solucao]
        y = [ponto[1] for ponto in solucao]
        pt.plot(y)
        pt.savefig('grafico.jpg')
        pt.show()

    else:
        x = [ponto[0] for ponto in solucao]
        y = [ponto[1] for ponto in solucao]
        z = [ponto[2] for ponto in solucao]
        pt.plot(y)
        pt.plot(z)
        pt.savefig(nome_arquivo)
        pt.show()

if __name__ == '__main__':
    with open('arquivo_entrada.txt', 'r') as file:
        # Lendo a funcao e criando uma funcao anônima
        funcoes_string = file.readline().strip()
        funcoes = funcoes_string.split('|')

        # Lendo os pontos
        pontos1 = file.readline().strip().split('|')
        pontos1 = [ponto.split() for ponto in pontos1]
        pontos1 = [[float(valor) for valor in ponto] for ponto in pontos1]

        pontos2 = file.readline().strip().split('|')
        pontos2 = [ponto.split() for ponto in pontos2]
        pontos2 = [[float(valor) for valor in ponto] for ponto in pontos2]

        param = file.readline().strip().split()
        param = [float(valor) for valor in param]

        # Valores de h, ordem e iterações
        h = float(file.readline())
        o = int(file.readline())

        # Chama a função com os valores
        resultado = shooting(funcoes, pontos1, pontos2, param, h, o)
        # erro = erro_shooting(funcao_string, x, y, h, o)

        # Escreve o resultado na saída
        with open('arquivo_saída.txt', 'w') as out:
            out.write(f'resultado: ({resultado[0]})\n\n')

            out.write(f'iteracoes do primeiro tiro:\n')
            for i in range(len(resultado[2])):
                out.write(f'it {i+1}: {resultado[2][i]}\n')

            out.write(f'\niteracoes do segundo tiro:\n')
            for i in range(len(resultado[3])):
                out.write(f'it {i+1}: {resultado[3][i]}\n')
                
            out.write(f'\niteracoes do tiro final:\n')
            for i in range(len(resultado[1][1])):
                out.write(f'it {i+1}: {resultado[1][1][i]}\n')

        grafico(resultado[2], 'grafico1')
        grafico(resultado[3], 'grafico2')
        grafico(resultado[1][1], 'grafico3')

        #pt.savefig('grafico_final')
        #pt.show()

