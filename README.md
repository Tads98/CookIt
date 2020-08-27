# Tutorial - Rodar Projeto

    1. Entre na sua branch: git checkout 'sua branch'
    2. Atualize as alterações da última branch para a sua: git pull origin 'ultima branch alterada'
    3. Instale a versão mais recente do pip: python -m pip install --upgrade pip
    4. Instale o Django: pip install django
    5. Instale o pillow: python -m pip install Pillow
    6. Verificar se o servidor está funcionando: python manage.py runserver

# Observações

    1. Se estiver no Linux e der erro no arquivo Settings ao rodar o servidor, tente: alias python="python3.7"
    2. Se tentar entrar na virtualvenv no Windows e der erro de segurança:
        2.1 Entre no Windows Power Shell como Adm e execute: Set-ExecutionPolicy Unrestricted -Force 