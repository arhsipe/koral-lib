from koral.io import read_csv
from koral.core import clean_data, summary_stats
from koral.viz import plot_bar

def main():
    # Teste leitura CSV
    df = read_csv('exemplo.csv')  # troque para um CSV que você tenha

    if df is None:
        print("Erro na leitura do arquivo, saindo...")
        return

    # Limpar dados
    df_clean = clean_data(df)

    # Mostrar resumo estatístico
    summary_stats(df_clean)

    # Plotar gráfico simples (ajuste colunas conforme seu CSV)
    plot_bar(df_clean, x=df_clean.columns[0], y=df_clean.columns[1])

if __name__ == "__main__":
    main()
