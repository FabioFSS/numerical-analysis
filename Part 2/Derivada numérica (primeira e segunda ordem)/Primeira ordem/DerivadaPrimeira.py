from math import log

def DerivadaCentrada(indice, pontosx, pontosy=None, funcao=None):
    if funcao != None:
        res = (funcao(pontosx[indice+1]) - funcao(pontosx[indice-1])) / (2 * (pontosx[indice] - pontosx[indice-1]))
    else:
        res = (pontosy[indice+1] - pontosy[indice-1]) / (2 * (pontosx[indice] - pontosx[indice-1]))
    
    return res

def DerivadaRetardada(indice, pontosx, pontosy=None, funcao=None):
    if funcao != None:
        res = (funcao(pontosx[indice]) - funcao(pontosx[indice-1])) / (pontosx[indice] - pontosx[indice-1])
    else:
        res = (pontosy[indice] - pontosy[indice-1]) / (pontosx[indice] - pontosx[indice-1])

    return res

def DerivadaAvancada(indice, pontosx, pontosy=None, funcao=None):
    if funcao != None:
        res = (funcao(pontosx[indice+1]) - funcao(pontosx[indice])) / (pontosx[indice+1] - pontosx[indice])
    else:
        res = (pontosy[indice+1] - pontosy[indice]) / (pontosx[indice+1] - pontosx[indice])

    return res


if __name__ == '__main__':
    # faz a leitura dos dados de entrada
    with open('arquivo_entrada.txt', 'r') as file:
        # faz a leitura dos dados de entrada para função
        # funcao_str = file.readline()

        # funcao = lambda x: eval(funcao_str)

        # ponto = float(file.readline())
        # intervalo = float(file.readline())

        # pontosx = [ponto-intervalo*2, ponto-intervalo, ponto, ponto+intervalo, ponto+intervalo*2]
        # pontosy = [funcao(ponto) for ponto in pontosx]


        # faz a leitura dos dados de entrada para pontos
        pontosx = file.readline().strip().split()
        pontosx = [float(ponto) for ponto in pontosx]

        pontosy = file.readline().strip().split()
        pontosy = [float(ponto) for ponto in pontosy]


        res1 = DerivadaCentrada(2, pontosx, pontosy)
        res2 = DerivadaRetardada(2, pontosx, pontosy)
        res3 = DerivadaAvancada(2, pontosx, pontosy)

        # res1 = DerivadaCentrada(2, pontosx, funcao=funcao)
        # res2 = DerivadaRetardada(2, pontosx, funcao=funcao)
        # res3 = DerivadaAvancada(2, pontosx, funcao=funcao)

        with open('arquivo_saida.txt', 'w') as file:
            file.write(f'Centrada: {res1}\n')
            file.write(f'Retardada: {res2}\n')
            file.write(f'Avancada: {res3}\n')
