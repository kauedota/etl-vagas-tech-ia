from transform import transformar_dados
from load import salvar_dados
from ai_enrichment import gerar_insight


def executar_pipeline():

    print("Iniciando ETL...")

    df = transformar_dados()

    print("Aplicando IA nas vagas...")

    insights = []

    for _, row in df.iterrows():

        vaga = {
            "empresa": row["empresa"],
            "cargo": row["cargo"],
            "salario": row["salario"],
            "local": row["local"]
        }

        insight = gerar_insight(vaga)
        insights.append(insight)

    df["insight_ia"] = insights

    print("Salvando no banco...")

    salvar_dados(df)

    print("Pipeline finalizado com sucesso!")


if __name__ == "__main__":
    executar_pipeline()