# TO-DO Tasks: API Sync

## Instruções para executar a API

Entre em `m10-p1` crie um virtual environment, ative e instale as bibliotecas necessárias:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Crie as tabelas caso elas não exitam ainda:

```python
python create_table.py
```

Após isso, execute a API:

```
python3 main.py
```

A documentação Swagger da API estará disponível em http://127.0.0.1:5000/docs/

## Arvore de arquivos

```
m10-p1
├── static
│   └── swagger.json
├── api_insomnia.json
├── create_tables.py
├── main.py
├── README.md
├── requirements.txt
├── sqlite.db

```

### Descrição dos arquivos

- static/swagger.json: Arquivo JSON usado para gerar o Swagger, utilizado na documentação da API.
- insomnia.json: Coleção de Insomnia contendo configurações para testar a API.
- create_tables.py: Script executado para criar as tabelas no banco de dados SQLite.
- main.py: Arquivo principal responsável pela execução da API.
- README.md: Este arquivo contendo informações sobre o projeto.
- requirements.txt: Lista das bibliotecas necessárias para o funcionamento do sistema.
- sqlite.db: Banco de dados SQLite utilizado para armazenar as informações do sistema.
