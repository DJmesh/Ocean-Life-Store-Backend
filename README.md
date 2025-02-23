# 🌊 Ocean Life Store - Frontend

Este projeto faz parte da disciplina de **Desenvolvimento Web** e tem como objetivo criar um **e-commerce sustentável** focado na preservação dos oceanos e proteção da vida marinha. Ele está alinhado com a **ODS 14 - Vida na Água**, promovendo conscientização e incentivando práticas responsáveis.

---
## 🚀 Tecnologias Utilizadas

- **Frontend**: [Next.js](https://nextjs.org/) com [TypeScript](https://www.typescriptlang.org/)
- **Estilização**: [Tailwind CSS](https://tailwindcss.com/)
- **Backend**: [Django REST Framework](https://www.django-rest-framework.org/)
- **Gerenciamento de Estado**: (Pode ser adicionado posteriormente, ex: Redux, Zustand)
- **Deploy**: (Pode ser configurado para Vercel, Netlify ou Docker)
- **Banco de Dados**: (A definir, possivelmente PostgreSQL)

- **Python 3.10+**
- **Django 5.x**
- **Django REST Framework**
- **Django CORS Headers**
- **Django Simple JWT (Autenticação JWT)**
- **drf-yasg (Swagger para documentação da API)**
- **SQLite (Banco de dados padrão)**
- **Docker (Futuramente)**

---
## Estrutura do Projeto

```bash
OCEAN-LIFE-STORE-BACKEND/
│── app/                     # Configuração principal do Django
│   ├── settings.py           # Configurações globais do projeto
│   ├── urls.py               # Rotas principais do sistema
│   ├── wsgi.py               # Arquivo WSGI para deploy
│   ├── asgi.py               # Arquivo ASGI para aplicações assíncronas
│   ├── __init__.py           # Arquivo de inicialização do app
│
│── core/                     # Aplicação base (pode conter configurações compartilhadas)
│   ├── models/               # Modelos globais do projeto
│   ├── admin.py              # Configuração do Django Admin
│
│── user/                     # Aplicação para autenticação e perfis de usuário
│   ├── models/               # Modelos de usuários e perfis
│   ├── serializers/          # Serializers para conversão de dados (Signup, Signin)
│   ├── views/                # Lógica das requisições (Signup, Signin, User)
│   ├── urls.py               # Rotas para usuários e autenticação
│   ├── migrations/           # Migrações do banco de dados
│
│── venv/                     # Ambiente virtual do projeto (não precisa commitar)
│── manage.py                 # Arquivo principal para comandos do Django
│── db.sqlite3                # Banco de dados SQLite (modo desenvolvimento)
│── requirements.txt          # Dependências do projeto
│── README.md                 # Documentação do backend
│── .gitignore                # Arquivos a serem ignorados pelo Git

```

### Principais Pastas

1. **app**: Aplicação Django principal contendo as configurações, roteamento e WSGI.
   - `settings.py`: Contém todas as configurações do Django, incluindo DRF e JWT.
   - `urls.py`: Arquivo de roteamento que define os pontos de entrada para todas as views e APIs.

2. **core**: Contém os elementos fundamentais do serviço backend.
   - `admin`: Configurações de admin do Django para gerenciar os modelos.
   - `models`: Modelos de dados que mapeiam para as tabelas do banco de dados.

3. **social_media**: Aplicação separada para lidar com a lógica relacionada às redes sociais.
   - `models`: Define os modelos como `Post`, `Like` e `Comment`.
   - `serializers`: Converte instâncias de modelos para JSON e vice-versa.
   - `views`: Endpoints para acessar dados de redes sociais (operações CRUD para posts, likes e comentários).

4. **user**: Contém a lógica para autenticação, sessões e gerenciamento de contas.
   - `models`: Gerencia contas de usuários, sessões e dados de assinatura.
   - `serializers`: Define como os dados de usuários são serializados para a API.
   - `views`: Implementa a lógica para cadastro, login e autenticação baseada em JWT.

5. **db.sqlite3**: O banco de dados SQLite usado para desenvolvimento e testes.

6. **requirements.txt**: Lista dos pacotes Python necessários para o funcionamento do projeto.

## Instruções de Configuração
### 📥 Como Instalar e Rodar o Backend
Instalar o Python
Caso ainda não tenha o Python 3.10+, baixe e instale através do link:
🔗 [Download Python](https://www.python.org/downloads/)

Após instalar, verifique a versão com:
```bash
python --version
```
### Criar e Ativar o Ambiente Virtual
Para isolar as dependências do projeto, crie um ambiente virtual:
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar no Windows
venv\Scripts\activate

# Ativar no Linux/Mac
source venv/bin/activate
```

### 1. Instalar Dependências

Certifique-se de ter Python 3.x instalado em seu sistema. Em seguida, instale os pacotes necessários executando:

```bash
pip install -r requirements.txt
```

### 2. Migrar Banco de Dados

Aplique as migrações para criar as tabelas necessárias no banco de dados SQLite:

```bash
python manage.py makemigrations user
```

```bash
python manage.py makemigrations core
```

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate user
```

```bash
python manage.py migrate core
```

```bash
python manage.py migrate
```

### 3. Executar o Servidor de Desenvolvimento

Para iniciar o servidor de desenvolvimento, execute o seguinte comando:

```bash
python manage.py runserver
```

### 4. Acessar o Painel de Administração

O painel de administração do Django está disponível em:

```bash
http://127.0.0.1:8000/admin/
```

Você precisará criar um superusuário para acessar o painel de administração:

```bash
python manage.py createsuperuser
```

### 5. Swagger UI (Documentação da API)

```bash
http://127.0.0.1:8000/api/schema/swagger/
```

### 6. Geração de Token JWT e Autenticação

O backend usa JWT (JSON Web Token) para autenticação. Para autenticar os usuários, os seguintes endpoints são usados:

- Geração de Token: /api/token/
- Atualização de Token: /api/token/refresh/

Após obter o token JWT, você pode usá-lo para autenticar as solicitações da API, incluindo-o no cabeçalho Authorization da seguinte forma:

```bash
Authorization: Bearer <your_token>
```

## Lógica de Autenticação

O backend utiliza o `rest_framework_simplejwt` para gerenciar a autenticação por meio de tokens JWT. O processo envolve:

1. Cadastro de Usuário:
- Os usuários podem criar uma conta usando a API de cadastro, que armazena as credenciais de forma segura no banco de dados.

2. Login de Usuário:
- Os usuários podem fazer login fornecendo suas credenciais para receber um token JWT. Esse token é então usado para autenticar as solicitações do usuário.

3. Atualização do Token:
- Quando o token expira, o usuário pode solicitar um novo token usando o endpoint de atualização, sem a necessidade de fazer login novamente.

A configuração do JWT está definida no arquivo `settings.py` sob a chave `SIMPLE_JWT`:

```bash
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
}
```

## Arquitetura do Sistema

1. Frontend:
- Responsável pela interface do usuário.
- Consome os serviços da API fornecidos pelo backend.

2. Backend:
- Responsável por fornecer a lógica de negócios, incluindo a autenticação JWT, criação e atualização de conteúdo, e gestão de interações sociais.
- Expõe endpoints da API REST que são consumidos pelo frontend.

## Banco de Dados:

- Armazena todas as informações necessárias, como dados do usuário, posts, comentários, curtidas e sessões de usuário.

## Tecnologias e Bibliotecas Usadas:

- Django: Framework backend para fornecer APIs RESTful.
- Django REST Framework (DRF): Biblioteca para criar APIs com facilidade e escalabilidade.
- JWT (JSON Web Token): Sistema de autenticação sem estado.
- SQLite: Banco de dados padrão para desenvolvimento.
- CORS: Configurado para permitir solicitações do frontend.
- Swagger: Documentação da API para facilitar a integração e o uso da API pelos desenvolvedores do frontend.

## Como o JWT Funciona:

1. Autenticação: 
- Quando o usuário faz login, o backend gera um token JWT com base nas credenciais fornecidas. Esse token é então enviado de volta ao cliente.

2. Autorização: 
- O token JWT é armazenado no lado do cliente e deve ser enviado com cada solicitação subsequente ao backend para provar que o usuário está autenticado. Isso é feito enviando o token no cabeçalho Authorization.

3. Validade: 
- O token tem uma validade limitada (exemplo: 5 minutos para o token de acesso), mas o usuário pode obter um novo token usando o refresh_token, sem precisar fazer login novamente.

## 🔍 Acessando a Documentação da API

A API possui documentação interativa via Swagger e Redoc:

- **Swagger UI** → http://127.0.0.1:8000/api/schema/swagger/
- **Redoc UI** → http://127.0.0.1:8000/api/schema/redoc/
