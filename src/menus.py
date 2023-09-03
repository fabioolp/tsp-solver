def menu_principal():
    print("""
      *******************  Menu Principal  *************************
      ATENCAO: Necessario gerar solucao inicial antes de refinar
                     1. Gere solucao inicial            <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                     2. Descida com Best Improvement    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                     3. Descida randomica               <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                     4. Descida com Primeiro de Melhora (First Improvement)   <<<<<<<<<<
                     5. Multi-Start
                     6. Simulated Annealing
                     7. Busca Tabu
                     8. ILS
                     9. GRASP
                    10. VND
                    11. VNS
                    12. Algoritmos Geneticos
                    13. LAHC        
                    14. Algoritmos Memeticos
                    15. Colonia de Formigas
                     0. Sair
      """)

def menu_solucao_inicial():
    print("""
          ************  Geração da Solução Inicial  ****************
                     1. Gulosa (Vizinho mais proximo)                 <<<<<<<<<<<<<<<<<
                     2. Parcialmente gulosa (Vizinho mais proximo)
                     3. Gulosa (Insercao Mais Barata)
                     4. Parcialmente gulosa (Insercao Mais Barata)
                     5. Aleatoria         <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
          """)