# Tutorial - Rodar Projeto

    1. Entre na sua branch: git checkout 'sua branch'
    2. Atualize as alterações da última branch para a sua: git pull origin 'ultima branch alterada'
    3. Instale a versão mais recente do pip: python -m pip install --upgrade pip
    4. Instale o Django: pip install django
    5. Instale o pillow: python -m pip install Pillow
    6. Verificar se o servidor está funcionando: python manage.py runserver

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
