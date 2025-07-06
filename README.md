# KORAL - Biblioteca de Análise de Dados Modular

KORAL é uma biblioteca Python didática e modular criada para facilitar operações comuns de análise de dados.  
Ela foi desenvolvida como um exercício de organização de código, reutilização de funções e boas práticas em Python.

## Funcionalidades

- Leitura de arquivos CSV e Excel
- Limpeza de dados ausentes
- Resumo estatístico descritivo
- Visualização com gráficos de barra, linha e histograma
- Exportação de resultados para CSV, JSON e Excel

## Organização do Código

coral/
├── coral/
│ ├── io.py # Leitura e exportação de dados
│ ├── core.py # Processamento e análise básica
│ ├── viz.py # Visualização com matplotlib/seaborn
│ └── init.py
├── exemplo.csv # Arquivo de dados para teste
├── test_script.py # Script de uso da biblioteca

## Requisitos

pip install pandas matplotlib seaborn openpyxl

## Exemplo de uso

from coral.io import read_csv, export_csv
from coral.core import clean_data, summary_stats
from coral.viz import plot_bar

df = read_csv('exemplo.csv')
df_limpo = clean_data(df)
summary_stats(df_limpo)
plot_bar(df_limpo, x='Categoria', y='Valor')
export_csv(df_limpo, 'resultado.csv')

## Contribuição

Este projeto é educacional e pode ser expandido com novos módulos ou funções.
Sinta-se à vontade para adaptar ao seu próprio aprendizado.

Desenvolvido por Arthur Pereira como exercício prático de estruturação de biblioteca Python.


