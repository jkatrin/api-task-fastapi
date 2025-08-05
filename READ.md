## 🚀 Desafio Prático: **Deploy Completo de uma API de Controle de Tarefas com CI/CD e Infraestrutura como Código**

Este desafio tem como objetivo construir uma **API RESTful em Python** que gerencia tarefas de usuários (como um mini Trello), salvando em um banco de dados MySQL, totalmente automatizada com **Docker, Terraform, AWS e GitHub Actions**.

---

### 🎯 Objetivos

* Criar uma API Python que permita **cadastrar, listar, editar e deletar tarefas**.
* Containerizar a aplicação com **Docker**.
* Subir a imagem para o **DockerHub**.
* Provisionar uma **instância EC2 com Terraform na AWS**.
* Automatizar o **deploy com GitHub Actions (CI/CD)**.

---

### 📥 Entradas da API

#### Rota: `POST /tarefas`

```json
{
  "titulo": "Estudar Python",
  "descricao": "Praticar funções e listas",
  "concluida": false
}
```

---

### 📤 Saída esperada

```json
{
  "message": "Tarefa criada com sucesso",
  "id": 1
}
```

---

### 🗃️ Banco de Dados

**Banco**: MySQL
**Tabela**: `tarefas`
**Colunas**:

* `id` (auto increment, chave primária)
* `titulo` (varchar)
* `descricao` (text)
* `concluida` (boolean)
* `data_criacao` (timestamp automático)

---

### 📦 Stack Técnica

* **Python (FastAPI ou Flask)**
* **MySQL**
* **Docker e Docker Compose**
* **Terraform (EC2 AWS)**
* **GitHub Actions (CI/CD)**
* **DockerHub (publicação de imagem)**

---

### 📁 Estrutura do Projeto (Sugerida)

```
task-api/
├── app.py
├── models.py
├── database.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
terraform/
├── main.tf
├── variables.tf
└── modules/
    └── ec2/
        └── main.tf
        └── variables.tf
        └── outputs.tf
.github/
└── workflows/
    └── deploy-app.yml
    └── deploy-infra.yml
README.md
```

---

### 🧪 Funcionalidades da API

* `POST /tarefas`: Cadastra uma nova tarefa
* `GET /tarefas`: Lista todas as tarefas
* `PUT /tarefas/{id}`: Atualiza uma tarefa existente
* `DELETE /tarefas/{id}`: Remove uma tarefa do sistema

---

### ⚙️ Etapas do Desafio

#### 1. Desenvolver a API em Python

* Criar endpoints CRUD para tarefas.
* Validar dados de entrada.
* Conectar com banco MySQL.

#### 2. Containerizar com Docker

* Criar um `Dockerfile` que:

  * Instala dependências
  * Expõe porta da API
  * Roda a aplicação

#### 3. Subir API e MySQL com Docker Compose

* Usar `.env` para variáveis
* Testar localmente antes do deploy

#### 4. Publicar a imagem no DockerHub

* Criar conta
* Fazer build + push da imagem

#### 5. Provisionar uma EC2 com Terraform

* Instalar Docker via `remote-exec`
* Rodar o container com a imagem da API

#### 6. Automatizar com GitHub Actions

* Criar pipeline com os jobs:

  * `build`: Build da imagem Docker
  * `push`: Push no DockerHub
  * `deploy`: Deploy automático na EC2 via SSH

---

### 🔐 GitHub Secrets necessários

| Variável          | Descrição                  |
| ----------------- | -------------------------- |
| `DOCKER_USERNAME` | Usuário do DockerHub       |
| `DOCKER_PASSWORD` | Senha/token do DockerHub   |
| `EC2_HOST`        | IP da EC2                  |
| `EC2_USER`        | Usuário (ex: ubuntu)       |
| `AWS_SSH_KEY`     | Chave SSH privada (base64) |

---

### ✅ Critérios de Entrega

* API funcional com rotas de tarefas (CRUD).
* Banco rodando via Docker Compose.
* Imagem da API publicada no DockerHub.
* Infra criada automaticamente com Terraform.
* CI/CD com deploy automático via GitHub Actions.

---

### 🧠 Extras (opcional)

* Adicionar autenticação com JWT
* Filtrar tarefas por status (`/tarefas?concluida=true`)
* Armazenar variáveis no AWS SSM Parameter Store
* Usar NGINX como proxy reverso

---

Se quiser, posso te ajudar a montar:

* A estrutura inicial do projeto
* O código da API com validações
* O Dockerfile e `docker-compose.yml`
* O Terraform modularizado
* Os workflows do GitHub Actions prontos para uso