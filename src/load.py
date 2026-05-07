import sqlite3


def salvar_dados(df):
    conn = sqlite3.connect("data/vagas.db")

    df.to_sql("vagas", conn, if_exists="replace", index=False)

    conn.close()