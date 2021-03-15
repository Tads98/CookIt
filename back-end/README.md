# Tutorial - Rodar Projeto

    1. Entre na sua branch: git checkout 'sua branch'
    2. Atualize as alterações da última branch para a sua: git pull origin 'ultima branch alterada'
    3. Instale a versão mais recente do pip: python -m pip install --upgrade pip
    4. Instale o Django: pip install django
    5. Instale o pillow: python -m pip install Pillow
    6. Instale o crispy forms: pip install django-crispy-forms
    7. Verificar se o servidor está funcionando: python manage.py runserver

# Observações

## Semânticas
        1. O nome de um app deve ser baseado em seu models, ou seja, os dados que vai armazenar.

## Técnicas
        1. Se estiver no Linux e der erro no arquivo Settings ao rodar o servidor, tente: alias python="python3.7"
        2. Se tentar entrar na virtualvenv no Windows e der erro de segurança:
            2.1 Entre no Windows Power Shell como Adm e execute: Set-ExecutionPolicy Unrestricted -Force
        3. Se for necessário criar uma virtual-venv: python3.7 -m venv venv
        4. Se a branch estiver remota, para mover para local: git checkout -t origin/nomeDaBranch
        5. Para trazer uma branch remota para local: git checkout -t origin/nomedaBranch
        6. Para deletar todas as linhas do banco de dados em django: rm db.sqlite3
        7. Para tentar instalar requirements-dev.txt:pip install wheel, pip install -r requirements.txt
            7.1: Se não conseguir, instale: sudo apt-get install python-matplotlib no Linux, ou python -m pip install -U pip setuptools e python -m pip install matplotlib. Volte a tentar o passo 7.
        8. Para pode usar 'AutoSlugField' é necessário instalar: pip install django-extensions
