import numpy as np


def constroi_solucao_aleatoria(n, s, d):
    '''
    Esta função implementa o método construtivo aleatório para resolver o Problema do Caixeiro Viajante.
    '''
    # Lista para armazenar as cidades visitadas
    cidade_visitada = []

    # Seleciona uma cidade inicial aleatória
    cidade_inicial = np.random.randint(n)
    cidade_visitada.append(cidade_inicial)

    # Cria uma lista de cidades não visitadas
    cidade_nao_visitada = list(range(n))
    cidade_nao_visitada.remove(cidade_inicial)

    # Construção aleatória
    cidade_atual = cidade_inicial
    while cidade_nao_visitada:
        proxima_cidade = np.random.choice(cidade_nao_visitada)
        cidade_visitada.append(proxima_cidade)
        cidade_nao_visitada.remove(proxima_cidade)
        cidade_atual = proxima_cidade

    # Fecha percurso retornando à cidade inicial
    cidade_visitada.append(cidade_inicial)

    s = cidade_visitada

    return s

def constroi_guloso_vizinho_mais_proximo(n, s, d):
    '''
    Esta função implementa o método construtivo guloso utilizando a heurística do Vizinho Mais Próximo para resolver o Problema do Caixeiro Viajante.
    '''
    visitados = set()
    s = []
    
    # Escolher uma cidade inicial aleatoriamente
    cidade_inicial = np.random.choice(n)
    s.append(cidade_inicial)
    visitados.add(cidade_inicial)
    
    # Construção da solução
    while len(s) < n:
        cidade_atual = s[-1]
        proxima_cidade = None
        menor_distancia = float('inf')
        
        # Encontrar a cidade mais próxima ainda não visitada
        for cidade in range(n):
            # Se a cidade não foi visitada e a distância entre a cidade atual e essa cidade é menor que menor_distancia, atualizamos proxima_cidade e menor_distancia.
            if (cidade not in visitados) and (d[cidade_atual][cidade] < menor_distancia):
                menor_distancia = d[cidade_atual][cidade]
                proxima_cidade = cidade
        
        s.append(proxima_cidade)
        visitados.add(proxima_cidade)
    
    # Fecha circuito de cidades
    s.append(cidade_inicial)
    
    # Retornar a solução completa
    return s