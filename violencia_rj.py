import pandas as pd
import plotly.express as px

# Leitura dos dados do arquivo CSV
violencia = "/content/BaseDPEvolucaoMensalCisp.csv"
dados = pd.read_csv(violencia, encoding="ISO-8859-1", sep=";")

# Dados de entrada
anos = list(range(2003, 2024))
risp = dados['risp'].unique()

# Lista de crimes (nomes das colunas no CSV)
crimes = ['furto_celular', 'roubo_carga', 'furto_veiculos']

# Criar um gráfico separado para cada RISP
for local in risp:
    # Filtrar os dados para o RISP atual
    dados_risp = dados[dados['risp'] == local]

    # Calcular os totais de crimes para cada crime e converter para inteiros
    totais_crimes = dados_risp[crimes].sum().astype(int)

    # Ordenar os totais de crimes em ordem decrescente
    totais_crimes = totais_crimes.sort_values(ascending=False)

    # Criar um DataFrame para o gráfico
    df = pd.DataFrame({'Crime': totais_crimes.index, 'QuantidadeTotal': totais_crimes.values})

    # Criar um gráfico de barras
    fig = px.bar(df, x='Crime', y='QuantidadeTotal', text='QuantidadeTotal', title=f'Crimes mais frequentes em {local}',
                 labels={"QuantidadeTotal": "Quantidade Total de Crimes"})

    # Adicionar rótulos de dados em cada barra
    fig.update_traces(texttemplate='%{text}', textposition='outside')

    # Exibir o gráfico
    fig.show()
