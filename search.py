import pandas as pd


def search_query(search_text: str):
    df = pd.read_csv('kirillgeniyvsearussi_improved.csv')

    mask = df.apply(lambda row: row.astype(str).str.contains(search_text, case=False, regex=False)).any(axis=1)

    result = df[mask][:1000]

    return result.to_dict(orient='records')
