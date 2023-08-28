# Biliotecas padrão
import pandas as pd
import numpy as np
import time

# Bibliotecas do projeto
import src.construcao as construcao
import src.utils as utils
import src.menus as menu


# Parametros
arquivo = 'data/c50.txt'
nome_index = 'index'
nome_coord_x = 'coord_x'
nome_coord_y = 'coord_y'

# Carrega dados
df_cidades = utils.carrega_dados(arquivo, nome_index, nome_coord_x, nome_coord_y)

# Calcula quantidade de cidades
n = len(df_cidades)

# Gera matriz de distancias
d = utils.calc_distancias(df_cidades, nome_index, nome_coord_x, nome_coord_y)

# Converter DataFrame para array NumPy
cidades = df_cidades[['coord_x', 'coord_y']].values


menu.menu_principal()
escolha_principal = input("Escolha: ")

match escolha_principal:
    # Solução inicial
    case "1":
        menu.menu_solucao_inicial()
        escolha_sol_inicial = input("Escolha: ")

        match escolha_sol_inicial:
            case "1":
                print('==================================\nSolução Inicial \n-- Gulosa (Vizinho mais proximo)')
                inicio_contagem_tempo = time.time() # Inicia contagem de tempo da construção da solução
                s = [] 
                s = construcao.constroi_guloso_vizinho_mais_proximo(n, s, d)
                fim_contagem_tempo = time.time() # Encerra contagem de tempo da construção
                print(f'\nForam gastos {round(fim_contagem_tempo - inicio_contagem_tempo, 4)} segundos na construção dessa solução')
                fo = utils.calcula_fo(n, s, d)
                print("\nSolucao construida pela Heurística Gulosa do Vizinho mais Proximo:")
                utils.imprime_rota(s, n)
                print(f"\n\nFuncao objetivo = {round(fo, 2)}")
            case "2":
                print('==================================\nSolução Inicial \n-- Parcialmente gulosa (Vizinho mais proximo)')
                print('Método ainda não implementado - tente a opção 5 - Aleatória')
            case "3":
                print('==================================\nSolução Inicial \n-- Gulosa (Insercao Mais Barata)')
                print('Método ainda não implementado - tente a opção 5 - Aleatória')
            case "4":
                print('==================================\nSolução Inicial \n-- Parcialmente gulosa (Insercao Mais Barata)')
                print('Método ainda não implementado - tente a opção 5 - Aleatória')
            case "5":
                print('==================================\nSolução Inicial \n-- Aleatória')
                inicio_contagem_tempo = time.time() # Inicia contagem de tempo da construção da solução
                s = [] 
                s = construcao.constroi_solucao_aleatoria(n, s, d)
                fim_contagem_tempo = time.time() # Encerra contagem de tempo da construção
                print(f'\nForam gastos {round(fim_contagem_tempo - inicio_contagem_tempo, 4)} segundos na construção dessa solução')
                fo = utils.calcula_fo(n, s, d)
                print("\nSolucao construida de forma aleatoria:")
                utils.imprime_rota(s, n)
                print(f"\n\nFuncao objetivo = {round(fo, 2)}")
    
            case _:
                print("Opção incorreta.")

    case _:
        print("Opção ainda não implementada.")


print("\nFim\n==================================")
