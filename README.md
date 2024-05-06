# Kanastra Challenge



Este repositório contém a solução para o Hiring Challenge Kanastra, foram implementadas as seguintes funcionalidades:

### Frontend 
- Desenvolvido com *React.JS*, apresentando uma mensagem "Hello Kanastra!" na rota principal.
(localizado na pasta *frontend*)

### Backend 
- implementado utilizando Django (Python), oferecendo um endpoint */charges* que aceita requisições POST com um contrato de payload específico. Os dados enviados são processados e salvos em um banco de dados *PostgreSQL*.

- Uma vez que uma das instruções era considerar as possibilidades de escabilidade da aplicação, optei pela utilização do Django e do PostgreSQL.

### Docker
Todos os serviços do projeto (frontend, backend e banco de dados) estão configurados para serem executados em containers Docker, utilizando docker-compose.

## Como executar

Dentro da raiz do projeto, execute no terminal os comandos na seguinte ordem:

+ 1 - `docker compose up -d db`
+ 2 - `docker compose build teste_kanastra`
+ 3 - `docker compose up teste_kanastra`

Após a construção e inicialização dos containers, a aplicação poderá ser acessada em **http://localhost:8000.**

O endpoint `charges` aceitará requisições do tipo POST com os requisitos informados no documento do desafio

Embora não fosse um dos requisitos obrigatórios do projeto, há também um endpoint `read` o qual aceita requisições do tipo GET. O intuito dessa rota é facilitar a visualização das informações presentes no banco de dados.

### requirements.txt e django.sh
Esses arquivos foram criados para serem referenciados no arquivo *Dockerfile*, com intuito de facilitar a construção da imagem. 

Python 3.8+
Django 5.0.4
Django Rest Framework 3.15.1
psycopg2-binary 2.9.9