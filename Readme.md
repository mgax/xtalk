# xtalk – realtime chat

## Setup

```shell
pip install -e '.[dev]'
export SECRET_KEY="some-random-secret-key"
./manage.py migrate
./manage.py runserver
```

## Upgrade Tailwind

```shell
curl -L 'https://cdn.tailwindcss.com?plugins=forms,typography' -o xtalk/static/tailwind.js
```

## Upgrade htmx

```shell
curl -L 'https://unpkg.com/htmx.org@2' -o xtalk/static/htmx.js
```
