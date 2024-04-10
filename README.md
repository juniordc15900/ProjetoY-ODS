# ProjetoY-ODS

Criar ambiente virtual

- python3 -m venv .venv-projetoy

Ativar ambiente virtual

* source .venv-projetoy/bin/activate
* .venv-projetoy\Scripts\activate

Instalar dependências

* pip install -r requirements.txt

Adicionar apps (endpoints)

* python manage.py startapp [nome_do_app]

Rodar projeto (necessario estar dentro do diretorio que contem o arquivo manage.py)

* python3 manage.py runserver
