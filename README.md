# Backend: listas de tarefas (Django REST Framework)

API de listas de tarefas consumida pelo frontend React em [frontend-react-integration-django](https://github.com/Leonardoongaratto/frontend-react-integration-django). Cada usuário tem suas listas, e cada lista tem itens que podem ser marcados como feitos.

## Rotas

| Rota | Recurso |
| --- | --- |
| `/list/` | Listas do usuário |
| `/item/` | Itens das listas (`done` marca como feito) |
| `/users/`, `/groups/` | Usuários e grupos |
| `/api-token-auth/` | Gera o token de autenticação a partir de usuário e senha |
| `/admin/` | Painel administrativo |

O CORS é liberado com `django-cors-headers` para o frontend conseguir chamar a API.

## Stack

Python · Django · Django REST Framework · django-cors-headers · django-environ · PostgreSQL · Gunicorn

## Como rodar

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

As configurações ficam em `backend/settings/` (`base.py` para desenvolvimento e `heroku.py` para o deploy que existia no Heroku).
