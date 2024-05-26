## Análise Interativa de Cervejas
Este projeto Dash oferece uma análise visual e interativa de um conjunto de dados de cervejas e cervejarias. Explore as relações entre diferentes características das cervejas, como teor alcoólico (ABV), amargor (IBU), cor (SRM) e muito mais.

## Demostração

![](https://i.imgur.com/H2Fdp8W.png)

## Funcionalidades
 - **Filtragem por Estilo:** Selecione um estilo de cerveja específico para focar sua análise.
 - **Visualização Personalizada:** Escolha entre gráficos de dispersão e de barras para visualizar os dados.
 - **Eixos Flexíveis:** Selecione os atributos que deseja comparar nos eixos X e Y do gráfico.
 - **Dados Detalhados:** Passe o mouse sobre os pontos do gráfico para ver informações detalhadas sobre cada cerveja, como nome e estilo.

## Pré-requisitos

 - **Python:** Certifique-se de ter o Python instalado em seu sistema.
 - **Bibliotecas:** Instale as bibliotecas necessárias usando o comando:
   ```bash
   pip install pandas plotly dash

 - **Use o código com cuidado.**
    ```bash
       content_copy

 - **Dados:** Tenha os arquivos beers.csv e breweries.csv no mesmo diretório do script Python.

## Como Usar

 - **Clone o Repositório:**
   ```bash
   git clone https://github.com/seu-usuario/analise-cervejas.git
   cd analise-cervejas
   
 - **Execute o Aplicativo:**
    ```bash
    python app.py

 - **Acesse no Navegador:**
Abra seu navegador e acesse http://127.0.0.1:8050/.

## Dados

O projeto utiliza dois arquivos CSV:

  - **beers.csv:** Contém informações sobre as cervejas, incluindo nome, estilo, teor alcoólico, amargor, cor, etc.
  - **breweries.csv:** Contém informações sobre as cervejarias, como nome e localização.

**Certifique-se de que esses arquivos estejam formatados corretamente e que as colunas relevantes estejam presentes.**

## Personalização

Sinta-se à vontade para modificar o código para adicionar mais funcionalidades, gráficos ou filtros. Você pode explorar outras bibliotecas de visualização, como Seaborn ou Bokeh, para criar gráficos ainda mais personalizados.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar pull requests com melhorias, correções de bugs ou novas funcionalidades.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
