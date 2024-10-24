# Desafio Django FullCycle 
Este repositório contém um aplicativo de Blog em django para realizar o desafio da semana FullClycle

## 🛠 Tecnologias Utilizadas

- **🟢 Django**
- **🔗 SQLITE**
- **🐳 Docker**

## 🐳 Configuração com Docker

Para rodar o app em docker e so rodar o seguinte comando 

1. Use o seguinte comando iniciar Docker:
  ```bash
    docker-compose up -d
  ```

## 🚀 Configuração Inicial Local

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/projeto-enchentes-backend.git
   ```
2. Use comando docker para subir Django 
   
3. Inicie o servidor:
   ```bash
    docker exec -it <ID_CONTAINER> bash
   ```
    * Apos executar esse comand, voce entra na pasta app dentro do container e execute:
    ```bash
     export PIPENV_VENV_IN_PROJECT=1
     pipenv shell
     pipenv install django
     
   ```