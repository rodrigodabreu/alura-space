#

### Iniciando o ambiente virtual

Para iniciar o ambiente virtual, basta executar o comando:

```
python -m venv .venv
```

### Ativando o ambiente virtual

Para ativar o ambiente virtual, basta executar o comando:

```
source .venv/bin/activate
```

### Instalando o Django

Para instalar o Django, basta executar o comando:

```
pip install django
```

### Iniciando o projeto com Django

O comando para iniciar o projeto é:

```
django-admin startproject <nome_do_projeto> .
```

Com o intuito de se manter as melhore práticas no projeto, o nome do projeto utilizado foi setup
ficando o comando da seguinte forma:

```
django-admin startproject setup .
```

### Executando o projeto

Para executar o projeto, basta executar o comando:

```
python manage.py runserver
```
