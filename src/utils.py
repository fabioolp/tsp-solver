import numpy as np
import pandas as pd
from io import StringIO
from scipy.spatial.distance import cdist


# Função para carregar os dados
def carrega_dados(arquivo, nome_index, nome_coord_x, nome_coord_y):
    # Lê arquivo txt
    f = open(arquivo)
    cidades = f.read()
    f.close()

    # Converte para DataFrame
    data_io = StringIO(cidades)
    columns = [nome_index, nome_coord_x, nome_coord_y]
    df = pd.read_csv(data_io, sep=' ', names=columns, header=None)

    return df


# Função para calcular as distâncias entre as cidades
def calc_distancias(df, nome_index, nome_coord_x, nome_coord_y):
    # Extrair as coordenadas das cidades
    coordenadas = df[[nome_coord_x, nome_coord_y]].values

    # Calcular as distâncias euclidianas entre as coordenadas usando cdist
    distancias_array = cdist(coordenadas, coordenadas, metric='euclidean')

    # Outra forma de calcular a distancia euclidiana - sem método pronto
    # distancias_array = np.zeros((len(coordenadas), len(coordenadas)))
    # for i in range(len(coordenadas)):
    #     for j in range(i + 1, len(coordenadas)):
    #         distancias_array[i][j] = np.sqrt(((coordenadas[i][0] - coordenadas[j][0])**2) + ((coordenadas[i][1] - coordenadas[j][1])**2))
    #         distancias_array[j][i] = distancias_array[i][j]

    # Criar um DataFrame a partir da matriz de distâncias
    df_distancias = pd.DataFrame(distancias_array, columns=df[nome_index], index=df[nome_index])

    return df_distancias


# Função para calcular a Função Objetivo (Distancia total percorrida)
def calcula_fo(n, s, d):
    distancia_total = sum(d[s[i]][s[i+1]] for i in range(n - 1))
    distancia_total += d[s[-1]][s[0]]

    return distancia_total


def imprime_rota(s, n):
    print('\nSolução:')
    for i in range(n+1):
        print(f'{s[i]}', end='')

        if i != n:
            print(' -> ', end='')