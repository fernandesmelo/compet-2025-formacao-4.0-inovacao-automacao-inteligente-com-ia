# Previsão de Atraso em Entregas de Pizza com Aprendizado de Máquina
Este projeto é um exemplo de aprendizado de máquina para prever se uma entrega de pizza vai atrasar ou não, [usando um conjunto de dados de vendas de pizza realista e estruturado que abrange o período de 2024 a 2025.](https://www.kaggle.com/datasets/akshaygaikwad448/pizza-delivery-data-with-enhanced-features) Ele lê uma tabela com informações de pedidos de pizza (como tamanho, tipo, distância, horário, etc.), analisa esses dados, treina dois modelos de computador para "aprender" padrões, e depois salva o melhor modelo para uso futuro.

### O que faz cada arquivo?
1. main.py
* **É o arquivo principal do projeto. Ele:**
Carrega e prepara os dados dos pedidos de pizza.
Gera gráficos para mostrar como são os dados.
Divide os dados em duas partes: uma para treinar o computador e outra para testar se ele aprendeu bem.
Treina dois modelos de aprendizado de máquina diferentes.
Avalia qual modelo aprendeu melhor.
Salva o melhor modelo em um arquivo para ser usado depois.

2. data_preprocessing.py
* **Cuida da preparação dos dados. Ele:**
Lê o arquivo de dados (CSV).
Seleciona apenas as colunas importantes.
Converte informações de texto em números (porque o computador entende melhor assim).
Preenche valores que estão faltando.
Separa os dados em "entradas" (o que sabemos sobre o pedido) e "saída" (se atrasou ou não).

3. model_training.py
* **É responsável por treinar os modelos. Ele:**
Cria dois tipos de modelos de aprendizado de máquina (Random Forest e SVC).
Ensina esses modelos usando os dados de treino.
Devolve os modelos treinados para serem avaliados.

4. model_evaluation.py
* **Serve para avaliar os modelos. Ele:**
Testa os modelos com dados que eles nunca viram antes.
Mostra qual modelo acertou mais previsões (acurácia).
Devolve as notas de cada modelo.

5. utils.py
* **Tem funções para gerar gráficos. Ele:**
Cria gráficos de barra, pizza e dispersão para ajudar a visualizar os dados e entender melhor o que está acontecendo.

6. preencher_is_delayed.py
* É um script auxiliar para preencher a coluna "Is Delayed" no arquivo de dados, marcando se o pedido atrasou ou não, baseado no tempo de atraso.

7. ver_colunas.py
* É um script simples para mostrar os nomes das colunas do arquivo de dados, ajudando na preparação do código.

8. model/
* É uma pasta onde o projeto salva o melhor modelo treinado para ser usado depois, sem precisar treinar tudo de novo.
