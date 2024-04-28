import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Carregar os DataFrames
beers_df = pd.read_csv('c:\\Users\\arthu\\Downloads\\Analise de dados - cerveja\\beers.csv')  
breweries_df = pd.read_csv('c:\\Users\\arthu\\Downloads\\Analise de dados - cerveja\\breweries.csv')

# Converter a coluna 'brewery_id' do DataFrame beers_df para o tipo object
beers_df['brewery_id'] = beers_df['brewery_id'].astype('object')

# Combinar os DataFrames usando a coluna 'name' como chave
df = pd.merge(beers_df, breweries_df, how='left', left_on='brewery_id', right_on='name')

# Filtrar entradas vazias na coluna 'style'
filtered_styles = df['style'].dropna().unique()

# Inicializar o aplicativo Dash
app = dash.Dash(__name__)

# Layout do aplicativo
app.layout = html.Div([
    html.H1("Análise de Cervejas"),
    html.Div([
        html.Label("Selecione um estilo de cerveja:"),
        dcc.Dropdown(
            id='style-dropdown',
            options=[{'label': style, 'value': style} for style in filtered_styles],
            value=filtered_styles[0]  # Selecionar o primeiro estilo por padrão
        )
    ]),
    html.Div([
        html.Label("Selecione um tipo de gráfico:"),
        dcc.Dropdown(
            id='chart-type-dropdown',
            options=[
                {'label': 'Gráfico de Dispersão', 'value': 'scatter'},
                {'label': 'Gráfico de Barras', 'value': 'bar'}
            ],
            value='scatter'  # Selecionar o gráfico de dispersão por padrão
        )
    ]),
    html.Div([
        html.Label("Selecione um item para o eixo X:"),
        dcc.Dropdown(
            id='x-axis-dropdown',
            options=[{'label': 'Beer Name: Nome da cerveja.', 'value': 'name_x'},
                     {'label': 'Beer Style: Estilo da cerveja.', 'value': 'style'},
                     {'label': 'Brewery Name: Nome da cervejaria.', 'value': 'name_y'},
                     {'label': 'ABV: Teor alcoólico da cerveja.', 'value': 'abv'},
                     {'label': 'IBU: Unidade Internacional de Amargor.', 'value': 'ibu'},
                     {'label': 'Color: Cor da cerveja em unidades SRM.', 'value': 'color'},
                     {'label': 'Availability: Disponibilidade da cerveja.', 'value': 'availability'},
                     {'label': 'Location: Localização da cervejaria.', 'value': 'city'},
                     {'label': 'Brewery ID: Identificação única da cervejaria.', 'value': 'brewery_id'},
                     {'label': 'Beer ID: Identificação única da cerveja.', 'value': 'id_x'}],
            value='abv'  # Selecionar 'abv' por padrão
        )
    ]),
    html.Div([
        html.Label("Selecione um item para o eixo Y:"),
        dcc.Dropdown(
            id='y-axis-dropdown',
            options=[{'label': 'Beer Name: Nome da cerveja.', 'value': 'name_x'},
                     {'label': 'Beer Style: Estilo da cerveja.', 'value': 'style'},
                     {'label': 'Brewery Name: Nome da cervejaria.', 'value': 'name_y'},
                     {'label': 'ABV: Teor alcoólico da cerveja.', 'value': 'abv'},
                     {'label': 'IBU: Unidade Internacional de Amargor.', 'value': 'ibu'},
                     {'label': 'Color: Cor da cerveja em unidades SRM.', 'value': 'color'},
                     {'label': 'Availability: Disponibilidade da cerveja.', 'value': 'availability'},
                     {'label': 'Location: Localização da cervejaria.', 'value': 'city'},
                     {'label': 'Brewery ID: Identificação única da cervejaria.', 'value': 'brewery_id'},
                     {'label': 'Beer ID: Identificação única da cerveja.', 'value': 'id_x'}],
            value='ibu'  # Selecionar 'ibu' por padrão
        )
    ]),
    dcc.Graph(id='interactive-plot')
])

# Callback para atualizar o gráfico interativo com base nas seleções do usuário
@app.callback(
    Output('interactive-plot', 'figure'),
    [
        Input('style-dropdown', 'value'),
        Input('chart-type-dropdown', 'value'),
        Input('x-axis-dropdown', 'value'),
        Input('y-axis-dropdown', 'value')
    ]
)
def update_plot(selected_style, chart_type, x_axis, y_axis):
    filtered_df = df[df['style'] == selected_style]
    
    # Verificar se o DataFrame está vazio
    if filtered_df.empty:
        # Se estiver vazio, retorna um gráfico vazio com um título informativo
        fig = go.Figure()
        fig.update_layout(title=f"Nenhum dado disponível para o estilo de cerveja selecionado: {selected_style}")
        return fig
    
    # Verificar se os tipos de gráfico selecionados são válidos
    if chart_type == 'scatter':
        # Criar um gráfico de dispersão
        fig = px.scatter(filtered_df, x=x_axis, y=y_axis, color='style', hover_name='name_x',
                         title=f"{y_axis.capitalize()} vs. {x_axis.capitalize()} para o Estilo de Cerveja: {selected_style}")
    elif chart_type == 'bar':
        # Criar um gráfico de barras
        fig = px.bar(filtered_df, x=x_axis, y=y_axis, color='style', hover_name='name_x',
                     title=f"{y_axis.capitalize()} vs. {x_axis.capitalize()} para o Estilo de Cerveja: {selected_style}")
    
    return fig

# Executar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
