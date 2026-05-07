import json
import os

# Lista simulando vagas vindas de API
vagas = [
    {
        "empresa": "Tech Solutions",
        "cargo": "Backend Python Jr",
        "salario": 4500,
        "local": "Remoto"
    },
    {
        "empresa": "CodeX",
        "cargo": "QA Júnior",
        "salario": 3500,
        "local": "São Paulo"
    },
    {
        "empresa": "DevMaster",
        "cargo": "Desenvolvedor Java Júnior",
        "salario": 5000,
        "local": "Híbrido"
    }
]

# Garante que a pasta data existe
os.makedirs("data", exist_ok=True)

# Salva os dados em JSON
with open("data/vagas_raw.json", "w", encoding="utf-8") as arquivo:
    json.dump(vagas, arquivo, indent=4, ensure_ascii=False)

print("Dados extraídos com sucesso!")