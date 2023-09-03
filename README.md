# Problema do Caixeiro Viajante em Python

Este repositório contém implementações didáticas do Problema do Caixeiro Viajante (TSP) em Python, usando diversas heurísticas. O objetivo principal é demonstrar e explicar as heurísticas.

## Conteúdo do Repositório

1. **Notebooks Explicativos:** Existem vários Jupyter Notebooks que explicam diferentes heurísticas para resolver o TSP. Cada notebook inclui uma explicação detalhada, código Python e exemplos de aplicação. Os notebooks disponíveis são:

   - [Notebook 1: Algoritmo de Força Bruta](notebooks/Brute_Force_TSP.ipynb)
   - [Notebook 2: Algoritmo de Vizinho Mais Próximo](notebooks/Nearest_Neighbor_TSP.ipynb)
   - [Notebook 3: Algoritmo de Inserção Mais Próxima](notebooks/Nearest_Insertion_TSP.ipynb)
   - [Notebook 4: Algoritmo Genético](notebooks/Genetic_Algorithm_TSP.ipynb)
   - [Notebook 5: Recozimento Simulado](notebooks/Simulated_Annealing_TSP.ipynb)

2. **Bases de Dados:** O diretório `datasets` contém conjuntos de dados que podem ser usados como exemplos para resolver o TSP. Os arquivos estão no formato apropriado para leitura nas implementações.

3. **Código Python Interativo:** O arquivo `tsp_solver.py` contém uma implementação interativa do TSP em Python. O usuário pode escolher entre várias heurísticas para resolver o problema e fornecer a base de dados de entrada.

## Como Usar

Para executar a implementação interativa, execute o arquivo `tsp_solver.py`. Você será apresentado a um menu com opções para escolher o método de resolução e fornecer a base de dados. Certifique-se de ter as bibliotecas necessárias instaladas (pode usar `pip install -r requirements.txt` para instalá-las).

Para aprender sobre as heurísticas e como elas funcionam, consulte os Jupyter Notebooks na pasta `notebooks`. Cada notebook contém uma explicação detalhada e exemplos práticos.

## Contribuições

Sinta-se à vontade para contribuir para este repositório, adicionando novas heurísticas, otimizando o código ou melhorando as explicações. Se você encontrar um problema ou tiver sugestões, abra uma issue.
