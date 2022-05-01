# CRUD
 ## O que é um CRUD ? 
 - CRUD é a acroôimo da primeira letra (da sigla em inglês) de 4 funções básicas de um sistema que trabalha com manipulação de banco de dados:

✅ C: Create (criar) - criar um novo registro <br />
👁 R: Read (ler) - ler (exibir) as informações de um registro <br />
♻️ U: Update (atualizar) - atualizar os dados do registro <br />
❌ D: Delete (apagar) - apagar um registro <br />

PImagine que você quer fazer uma simples agenda ou um complexo sistema de gerenciamento de dados de alunos de uma universidade, <br />
será preciso utilizar as 4 ações para manipular as tabelas de banco de dados de seu sistema.<br /> <br />

Na criação de um sistema será necessário criar : <br /> - Tabelas (modelos) de bancos de dados.<br />
                                                 - Funções (controles) que farão a atualização do banco de dados.<br />
                                                 - Interface (o que será visto) que será a frente da aplicação e terá interação e manipulação do usúario.<br />

Em sistemas mais elaborados os dados de um CRUD podem ser manipulados por APIS. 

## Esse projeto irá utilizar, Python, Django e SqlLite. 

## Criando o servidor. 

- criando um ambiente virtual : 
        - cd pastadoseuprojeto 
            - nomedasuapasta -m venv venv 
             - cd venv/Scripts
                - activate (ou .\activate) -- aqui você irá ativar o seu 
                    - instale o Django 

- Para instalar o Django - pip install Django 
- Django-admin startproject coloqueaquionomedoseuprojeto  . 
    - foi criada a sua pasta nela , terá vários arquivos , como setting (parte de configuração), wsgi ( enviar pro ar ), urls ( rotas do nosso site )

criado o projeto, vamos criar o app com comando - python manage.py startapp nomedoseuapp 

###  Após fazer todos os nossos caminhos criados, para verificar se o servidor está rodando adequadamente: 
  - em projetos, settings , em installed app insira o nome do seu app (isso é pára que o projeto entenda que o app faz parte dele )
  - agora em urls,  crie um import para o nosso app ( from app.views import home , coloque o path abaixo xom o caminho para a home (path('",home)))
  - crie a home em views (def home(request):)
  - vamos criar um import , para visualizar (from django.http import HttpResponse )
  - e na nossa def vamos dar um return HttpResponse("Hello World")
  ### - para visualiozar use o comando python manage.py runserver
  - pegue o caminho que no Starting development server at e coloque no seu navegador 
  - o que deve aparecer será nosso Hello World. 

  Passo 1 - 

  Templates : elemntos de marcação para fazer formulários e outros. (layout)
    o diretorio com o nome templates já é reconhecido pelo Django 

vamos no views e vamos referenciar nosso template 
 - from django.shortcuts import render
    na função que já havia criado 
     return render(request, 'index.html') (criar um index.html )


  

