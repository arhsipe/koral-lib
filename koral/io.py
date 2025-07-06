import pandas as pd

def read_csv(path):
    """
    Lê um arquivo CSV e retorna um DataFrame.
    """
    try:
        df = pd.read_csv(path)
        print(f"Arquivo CSV lido com sucesso: {path}")
        return df
    except Exception as e:
        print(f"Erro ao ler CSV: {e}")
        return None

def read_excel(path):
    """
    Lê um arquivo Excel (.xls ou .xlsx) e retorna um DataFrame.
    """
    try:
        df = pd.read_excel(path)
        print(f"Arquivo Excel lido com sucesso: {path}")
        return df
    except Exception as e:
        print(f"Erro ao ler Excel: {e}")
        return None

def export_csv(df, path, include_index=False):
    """
    Exporta DataFrame para arquivo CSV.
    """
    try:
        df.to_csv(path, index=include_index)
        print(f"Arquivo CSV exportado com sucesso: {path}")
    except Exception as e:
        print(f"Erro ao exportar CSV: {e}")

def export_json(df, path, orient='records', lines=True):
    """
    Exporta DataFrame para arquivo JSON.
    Parâmetros:
        orient: formato da saída (default 'records')
        lines: se True, cada registro é uma linha separada (default True)
    """
    try:
        df.to_json(path, orient=orient, lines=lines)
        print(f"Arquivo JSON exportado com sucesso: {path}")
    except Exception as e:
        print(f"Erro ao exportar JSON: {e}")

def export_excel(df, path, sheet_name='Sheet1'):
    """
    Exporta DataFrame para arquivo Excel (.xlsx).
    """
    try:
        df.to_excel(path, sheet_name=sheet_name, index=False)
        print(f"Arquivo Excel exportado com sucesso: {path}")
    except Exception as e:
        print(f"Erro ao exportar Excel: {e}")