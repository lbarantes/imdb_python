# IMDb Top 250 Filmes - Scrapper

Este projeto é um script em Python que utiliza Selenium para realizar web scraping no site da IMDb e extrair informações sobre os 250 melhores filmes de acordo com a classificação do site. Os dados extraídos incluem a posição, o nome do filme e sua nota, e são salvos em um arquivo Excel.  

## ⚒️ Funcionalidades  

1. **Raspagem de Dados**  
   - O script acessa a página dos 250 melhores filmes no site IMDb.  
   - Localiza e extrai as seguintes informações para cada filme:  
     - **Posição**: A posição do filme no ranking.  
     - **Nome**: O título do filme.  
     - **Nota**: A nota atribuída ao filme no IMDb.  

2. **Armazenamento dos Dados**  
   - Os dados coletados são organizados em um DataFrame utilizando a biblioteca Pandas.  
   - São exportados para um arquivo Excel chamado `Top250Movies.xlsx`.  

## 💻 Tecnologias Utilizadas  

- **Selenium**: Automação de navegação no site da IMDb e coleta de dados.  
- **Pandas**: Manipulação de dados e criação do arquivo Excel.
