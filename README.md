# ☁️ Projeto 3 – Integração com AWS S3 usando Python

Este projeto demonstra uma integração **básica com a AWS**, realizando upload de arquivos locais para um bucket S3 utilizando Python.

O objetivo é mostrar que já tive **contato prático com serviços AWS**, especialmente o S3.

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
│ ├── upload_s3.py
│ └── teste.txt
├── .env
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

🎯 Objetivo do projeto

Demonstrar conhecimento básico em cloud

Mostrar integração real entre Python e AWS

Projeto simples, didático e funcional


💙 Esse README está **perfeito para recrutador**: direto, organizado e honesto.

---

## 2️⃣ Conferir o `.gitignore` (importantíssimo)
Abra o `.gitignore` e veja se tem isso:



.env
pycache/


Se não tiver, adiciona e salva.

---

## 3️⃣ Subir o projeto para o GitHub 🚀

Agora no terminal, **na pasta do projeto**:

```bash
git init
git add .
git commit -m "Projeto 3: integração básica com AWS S3 usando Python"
git branch -M main
git remote add origin https://github.com/magdieline/Projeto-integra-oAWS.git
git push -u origin main


Se pedir login:

Usuário: seu usuário do GitHub
Senha: token do GitHub (não é a senha normal)




