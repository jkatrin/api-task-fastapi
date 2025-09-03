🚀 API RESTful de Gerenciamento de Usuários
Este projeto demonstra a criação de uma API RESTful completa, utilizando Python e MySQL, com uma infraestrutura robusta e automatizada. Ele segue as boas práticas de desenvolvimento e DevOps, incluindo containerização com Docker, gerenciamento de infraestrutura como código (IaC) com Terraform e automação de CI/CD com GitHub Actions.

🌟 Visão Geral
O objetivo principal deste projeto é criar uma API simples para gerenciar usuários, mas com foco especial na sua implantação e automação. A aplicação permite realizar operações básicas (CRUD): criar, ler, atualizar e deletar usuários.

A arquitetura do projeto é dividida em várias etapas:

API em Python: Uma API RESTful que recebe e envia dados no formato JSON.

Banco de Dados MySQL: Um banco de dados relacional para persistir as informações dos usuários.

Containerização com Docker: A aplicação e o banco de dados são empacotados em contêineres para garantir um ambiente de desenvolvimento e produção consistente.

Automação de Infraestrutura com Terraform: Criação de uma instância AWS EC2 de forma programática.

CI/CD com GitHub Actions: Automação do build, teste e deploy do projeto, garantindo atualizações contínuas e automáticas.

🛠️ Tecnologias Utilizadas
Linguagem de Programação: Python

Frameworks Web: Flask ou FastAPI (mencione qual você está usando)

Banco de Dados: MySQL

Containerização: Docker e Docker Compose

Infraestrutura como Código (IaC): Terraform

Provedor de Nuvem: AWS (Amazon Web Services)

CI/CD: GitHub Actions

📦 Como Rodar o Projeto Localmente
Siga os passos abaixo para executar a API e o banco de dados na sua máquina usando Docker Compose. Certifique-se de ter o Docker instalado.

Clone o Repositório:

Bash

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Inicie os Contêineres:
O Docker Compose irá construir a imagem da sua API, iniciar o contêiner do banco de dados MySQL e conectá-los.

Bash

docker-compose up --build
Acesse a API:
Após os contêineres estarem em execução, a API estará acessível em http://localhost:5000.

🚧 Status do Projeto
Este projeto está em desenvolvimento contínuo. Atualmente, o foco é a etapa de containerização com Docker e Docker Compose.

Status atual:

✔️ Dockerfile criado.

✔️ docker-compose.yml configurado para orquestrar a API e o banco de dados.

✔️ Imagens Docker criadas com sucesso.

Próximos passos:

Corrigir o problema de dependência: Atualmente, a API está encerrando inesperadamente ao tentar conectar com o contêiner do MySQL. Estou investigando e trabalhando para resolver esse problema de conexão entre os serviços.

Publicar a imagem no DockerHub.

Implementar o provisionamento da infraestrutura com Terraform.

Configurar os pipelines de CI/CD com GitHub Actions
