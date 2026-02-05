import os
import boto3
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

BUCKET_NAME = os.getenv("BUCKET_NAME")

def upload_arquivo(nome_arquivo):
    try:
        s3.upload_file(nome_arquivo, BUCKET_NAME, nome_arquivo)
        print("✅ Arquivo enviado com sucesso!")
    except Exception as erro:
        print("❌ Erro ao enviar arquivo:", erro)


if __name__ == "__main__":
    arquivo = input("Digite o nome do arquivo para upload: ")
    upload_arquivo(arquivo)
