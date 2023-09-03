# Biliotecas padrão
import pandas as pd
import numpy as np
import time

# Bibliotecas do projeto
import src.construcao as construcao
import src.descida as descida
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
        print('==================================\nSolução Inicial')
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
                print('Método ainda não implementado - tente a opção 5 - Aleatória ou Guloso Vizinho Mais Proximo')
            case "3":
                print('==================================\nSolução Inicial \n-- Gulosa (Inserção Mais Barata)')
                print('Método ainda não implementado - tente a opção 5 - Aleatória ou Guloso Vizinho Mais Proximo')
            case "4":
                print('==================================\nSolução Inicial \n-- Parcialmente gulosa (Inserção Mais Barata)')
                print('Método ainda não implementado - tente a opção 5 - Aleatória ou Guloso Vizinho Mais Proximo')
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

    case '2':
        print('==================================\nDescida com Best Improvement')
        inicio_contagem_tempo = time.time() # Inicia contagem de tempo da construção da solução
        s = []
        s = construcao.constroi_guloso_vizinho_mais_proximo(n, s, d)
        fo_const = utils.calcula_fo(n, s, d)
        s, fo = descida.descida_best_improvement(n, s, d)
        fim_contagem_tempo = time.time() # Encerra contagem de tempo da construção
        print(f'\nForam gastos {round(fim_contagem_tempo - inicio_contagem_tempo, 4)} segundos na construção dessa solução')
        print(f"\nSolução:\n- Construção: Gulosa do Vizinho mais Proximo (custo={round(fo_const, 3)}) e\n- Refino: Descida com Best Improvement (custo={round(fo, 3)}):")
        utils.imprime_rota(s, n)
        print(f"\n\nFuncao objetivo = {round(fo, 2)}")

    case '3':
        print('==================================\nDescida randomica')
        inicio_contagem_tempo = time.time() # Inicia contagem de tempo da construção da solução
        s = []
        s = construcao.constroi_guloso_vizinho_mais_proximo(n, s, d)
        fo_const = utils.calcula_fo(n, s, d)
        s, fo = descida.descida_random_improvement(n, s, d)
        fim_contagem_tempo = time.time() # Encerra contagem de tempo da construção
        print(f'\nForam gastos {round(fim_contagem_tempo - inicio_contagem_tempo, 4)} segundos na construção dessa solução')
        print(f"\nSolução:\n- Construção: Gulosa do Vizinho mais Proximo (custo={round(fo_const, 3)}) e\n- Refino: Descida randomica (custo={round(fo, 3)}):")
        utils.imprime_rota(s, n)
        print(f"\n\nFuncao objetivo = {round(fo, 2)}")

    case '4':
        print('==================================\nDescida com Primeiro de Melhora (First Improvement)')
        inicio_contagem_tempo = time.time() # Inicia contagem de tempo da construção da solução
        s = []
        s = construcao.constroi_guloso_vizinho_mais_proximo(n, s, d)
        fo_const = utils.calcula_fo(n, s, d)
        s, fo = descida.descida_first_improvement(n, s, d)
        fim_contagem_tempo = time.time() # Encerra contagem de tempo da construção
        print(f'\nForam gastos {round(fim_contagem_tempo - inicio_contagem_tempo, 4)} segundos na construção dessa solução')
        print(f"\nSolução:\n- Construção: Gulosa do Vizinho mais Proximo (custo={round(fo_const, 3)}) e\n- Refino: Descida com Primeiro de Melhora (First Improvement) (custo={round(fo, 3)}):")
        utils.imprime_rota(s, n)
        print(f"\n\nFuncao objetivo = {round(fo, 2)}")
        
    case _:
        print("Opção ainda não implementada.")


print("\nFim\n==================================")
