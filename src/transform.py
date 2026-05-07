import pandas as pd


def transformar_dados():
    df = pd.read_json("data/vagas_raw.json")

    df = df.drop_duplicates()

    df["senioridade"] = df["cargo"].apply(definir_senioridade)
    df["area"] = df["cargo"].apply(definir_area)

    return df


def definir_senioridade(cargo):
    cargo = cargo.lower()

    if "júnior" in cargo or "jr" in cargo:
        return "Júnior"
    elif "pleno" in cargo:
        return "Pleno"
    elif "sênior" in cargo or "senior" in cargo:
        return "Sênior"

    return "Não identificado"


def definir_area(cargo):
    cargo = cargo.lower()

    if "python" in cargo:
        return "Backend Python"
    elif "qa" in cargo:
        return "Quality Assurance"
    elif "java" in cargo:
        return "Backend Java"

    return "Outros"