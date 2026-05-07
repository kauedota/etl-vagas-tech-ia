import os

from openai import OpenAI
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# Cliente OpenAI
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def gerar_insight(vaga):

    prompt = f"""
    Analise a seguinte vaga de tecnologia:

    Empresa: {vaga['empresa']}
    Cargo: {vaga['cargo']}
    Salário: R$ {vaga['salario']}
    Local: {vaga['local']}

    Gere:
    1. Um breve resumo da vaga
    2. Principais skills recomendadas
    3. Uma dica para o candidato se destacar

    Responda de forma curta e profissional.
    """

    resposta = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return resposta.choices[0].message.content


# TESTE

vaga_teste = {
    "empresa": "Tech Solutions",
    "cargo": "Backend Python Jr",
    "salario": 4500,
    "local": "Remoto"
}

resultado = gerar_insight(vaga_teste)

print(resultado)