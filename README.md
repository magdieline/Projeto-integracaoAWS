# ☁️ Projeto 3 – Integração com AWS S3 usando Python

Este projeto demonstra uma integração **básica com a AWS**, realizando upload de arquivos locais para um bucket S3 utilizando Python.

O objetivo é mostrar **contato prático com serviços AWS**, especialmente o Amazon S3.

---

## 🚀 Tecnologias utilizadas
- Python 3
- AWS S3
- boto3
- python-dotenv

---

## 📁 Estrutura do projeto
Projeto3-integracaoAWS/
├── app/
│ └── upload_s3.py
├── .gitignore
├── requirements.txt
└── README.md


---

## ⚙️ Configuração do ambiente

### 1. Criar um bucket no S3
Exemplo de nome:

### 2. Criar usuário IAM
- Permissão para S3
- Gerar **Access Key**

### 3. Configurar variáveis de ambiente
Criar um arquivo `.env` (não versionado):


### 2. Criar usuário IAM
- Permissão para S3
- Gerar **Access Key**

### 3. Configurar variáveis de ambiente
Criar um arquivo `.env` (não versionado):


### 2. Criar usuário IAM
- Permissão para S3
- Gerar **Access Key**

### 3. Configurar variáveis de ambiente
Criar um arquivo `.env` (não versionado):

AWS_ACCESS_KEY_ID=SUACHAVE
AWS_SECRET_ACCESS_KEY=SUACHAVESECRETA
AWS_DEFAULT_REGION=us-east-2


---

## 📦 Instalação das dependências
```bash
pip install -r requirements.txt

▶️ Executando o projeto
python app/upload_s3.py


Digite o nome do arquivo para upload, por exemplo:

app/teste.txt

✅ Resultado esperado

Arquivo enviado com sucesso para o bucket S3

Confirmação exibida no terminal

Arquivo visível no console da AWS