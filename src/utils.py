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
    distancias = cdist(coordenadas, coordenadas)

    # Criar um DataFrame a partir da matriz de distâncias
    df_distancias = pd.DataFrame(distancias, columns=df[nome_index], index=df[nome_index])

    return df_distancias


# Função para calcular a distância entre duas cidades
def calc_dist_euclidiana(cidade1, cidade2):
    return np.sqrt((cidade1[0] - cidade2[0])**2 + (cidade1[1] - cidade2[1])**2)


# Função para calcular a Função Objetivo (Distancia total percorrida)
def calcula_fo(n, s, d):
    distancia_total = sum(calc_dist_euclidiana(d[s[i]], d[s[i + 1]]) for i in range(n - 1))
    distancia_total += calc_dist_euclidiana(d[s[-1]], d[s[0]])

    return distancia_total


def imprime_rota(s, n):
    for i in range(n+1):
        print(f'{s[i]}', end='')

        if i != n:
            print(' -> ', end='')