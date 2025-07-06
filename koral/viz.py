import matplotlib.pyplot as plt
import seaborn as sns

def plot_bar(df, x, y):
    """
    Gera gráfico de barras simples.
    """
    plt.figure(figsize=(8,5))
    sns.barplot(data=df, x=x, y=y)
    plt.title(f'Gráfico de Barras: {y} por {x}')
    plt.show()

def plot_line(df, x, y):
    """
    Gera gráfico de linha simples.
    """
    plt.figure(figsize=(8,5))
    sns.lineplot(data=df, x=x, y=y)
    plt.title(f'Gráfico de Linha: {y} por {x}')
    plt.show()

def plot_histogram(df, column):
    """
    Gera histograma da coluna escolhida.
    """
    plt.figure(figsize=(8,5))
    sns.histplot(df[column], bins=20)
    plt.title(f'Histograma: {column}')
    plt.show()
