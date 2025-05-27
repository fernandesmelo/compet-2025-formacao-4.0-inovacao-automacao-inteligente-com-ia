# Previsão de Atraso em Entregas de Pizza com Aprendizado de Máquina
Este projeto é um exemplo de aprendizado de máquina para prever se uma entrega de pizza vai atrasar ou não, [usando um conjunto de dados de vendas de pizza realista e estruturado que abrange o período de 2024 a 2025.](https://www.kaggle.com/datasets/akshaygaikwad448/pizza-delivery-data-with-enhanced-features) Ele lê uma tabela com informações de pedidos de pizza (como tamanho, tipo, distância, horário, etc.), analisa esses dados, treina dois modelos de computador para "aprender" padrões, e depois salva o melhor modelo para uso futuro.

<img src="https://github.com/user-attachments/assets/fc370637-85bc-4910-96d1-57d63b89ac91" alt="ChatGPT Image 25 de mai de 2025, 12_38_30" width="400"/>

### 📂 O que faz cada arquivo?
**1. main.py**
* _É o arquivo principal do projeto. Ele:_
Carrega e prepara os dados dos pedidos de pizza.
Gera gráficos para mostrar como são os dados.
Divide os dados em duas partes: uma para treinar o computador e outra para testar se ele aprendeu bem.
Treina dois modelos de aprendizado de máquina diferentes.
Avalia qual modelo aprendeu melhor.
Salva o melhor modelo em um arquivo para ser usado depois.

**2. data_preprocessing.py**
* _Cuida da preparação dos dados. Ele:_
Lê o arquivo de dados (CSV).
Seleciona apenas as colunas importantes.
Converte informações de texto em números (porque o computador entende melhor assim).
Preenche valores que estão faltando.
Separa os dados em "entradas" (o que sabemos sobre o pedido) e "saída" (se atrasou ou não).

**3. model_training.py**
* _É responsável por treinar os modelos. Ele:_
Cria dois tipos de modelos de aprendizado de máquina (Random Forest e SVC).
Ensina esses modelos usando os dados de treino.
Devolve os modelos treinados para serem avaliados.

**4. model_evaluation.py**
* _Serve para avaliar os modelos. Ele:_
Testa os modelos com dados que eles nunca viram antes.
Mostra qual modelo acertou mais previsões (acurácia).
Devolve as notas de cada modelo.

**5. utils.py**
* _Tem funções para gerar gráficos. Ele:_
Cria gráficos de barra, pizza e dispersão para ajudar a visualizar os dados e entender melhor o que está acontecendo.

**6. preencher_is_delayed.py**
* É um script auxiliar para preencher a coluna "Is Delayed" no arquivo de dados, marcando se o pedido atrasou ou não, baseado no tempo de atraso.

**7. ver_colunas.py**
* É um script simples para mostrar os nomes das colunas do arquivo de dados, ajudando na preparação do código.

**8. model/**
* É uma pasta onde o projeto salva o melhor modelo treinado para ser usado depois, sem precisar treinar tudo de novo.

## 🛠️ Construído com

<div style="display: inline-block"><br/>
  <img align="center" alt="html5" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> 
</div><br/>

## 👨🏽‍💻 Versão das Tecnologias

* Python 3.12.8
* Bibliotecas:
  * ```pandas```: Manipulação e análise de dados.
  * ```matplotlib```: Visualização de dados.
  * ```scikit-learn```: Aprendizado de máquina.

## ✒️ Autor

* **Laércio Fernandes** - [LinkedIn](https://www.linkedin.com/in/laercio-fernandes/)

## 🚀 Guia de Como Baixar e Rodar o Projeto

### 📦 Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:

- [Git](https://git-scm.com)
- [Python 3.8+](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/)

Além disso, é bom ter um editor como o [VSCode](https://code.visualstudio.com/) para trabalhar com o código.

---

### 🛠️ Como rodar o projeto

Siga os passos abaixo para clonar o repositório e iniciar o projeto localmente:

#### 1. Clone o repositório
```bash
git clone https://github.com/fernandesmelo/compet-2025-formacao-4.0-inovacao-automacao-inteligente-com-ia.git
```
#### 2. Acesse a pasta do projeto
```bash
cd compet-2025-formacao-4.0-inovacao-automacao-inteligente-com-ia
```

#### 3. Crie e ative um ambiente virtual
1. **Clique na versão do Python no canto inferior direito** <br>
No canto inferior direito do VS Code, você verá a versão do Python atualmente selecionada. Clique nela.

2. **Selecione a opção "Create Virtual Environment"** <br>
Na aba de pesquisa que será exibida, procure e clique na opção "Create Virtual Environment".

3. **Escolha o tipo de ambiente virtual** <br>
Quando solicitado, clique na opção "Venv" para criar o ambiente virtual.

4. **Selecione o interpretador Python** <br>
Escolha a versão do Python instalada em sua máquina (recomenda-se Python 3.8 ou superior).

5. **Associe o arquivo requirements.txt** <br>
Após criar o ambiente virtual, o VS Code solicitará que você associe um arquivo de dependências. Selecione o arquivo requirements.txt do projeto.

6. **Confirme e aguarde** <br>
Clique em OK e aguarde enquanto o ambiente virtual é configurado e as dependências listadas no requirements.txt são instaladas automaticamente.

7. **Execute o projeto** <br>
Para rodar o projeto, abra o terminal no VS Code e digite:
```bash
python main.py
```
8. **Pronto!** <br>
Após a configuração, o ambiente virtual estará pronto para uso, e você poderá executar o notebook sem problemas.
