import pandas as pd

def clean_data(df):
    """
    Limpa o DataFrame removendo linhas com valores nulos.
    """
    original_count = len(df)
    df_clean = df.dropna()
    cleaned_count = len(df_clean)
    print(f"Linhas removidas por conter valores nulos: {original_count - cleaned_count}")
    return df_clean

def summary_stats(df):
    """
    Retorna estatísticas descritivas básicas do DataFrame.
    """
    stats = df.describe()
    print("Resumo estatístico:")
    print(stats)
    return stats

def filter_data(df, condition):
    """
    Filtra o DataFrame usando uma condição booleana.
    Exemplo de condição: df['coluna'] > 10
    """
    try:
        filtered = df.loc[condition]
        print(f"Dados filtrados. Linhas restantes: {len(filtered)}")
        return filtered
    except Exception as e:
        print(f"Erro ao filtrar dados: {e}")
        return None
