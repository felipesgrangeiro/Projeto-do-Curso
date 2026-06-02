# Projeto-do-Curso# Dashboard de veículos usados

Este projeto é um aplicativo web desenvolvido com Streamlit para explorar dados de anúncios de veículos usados.

O aplicativo permite visualizar informações do conjunto de dados `vehicles_us.csv` por meio de gráficos interativos criados com Plotly Express.

## Funcionalidades

- Exibição de um cabeçalho com o título do dashboard;
- Criação de um histograma da coluna `odometer`, mostrando a distribuição da quilometragem dos veículos;
- Criação de um gráfico de dispersão entre `odometer` e `price`, mostrando a relação entre quilometragem e preço;
- Interação com o usuário por meio de botões ou caixas de seleção.

## Tecnologias utilizadas

- Python
- Pandas
- Plotly Express
- Streamlit

## Como executar o projeto localmente

Para executar o aplicativo, use o comando:

```bash
streamlit run app.py
