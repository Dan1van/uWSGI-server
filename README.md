# uWSGI-server


uWSGI-server — простой wsgi-фреймворк, разработанный на языке программирования Python.

## Установка

Склонируйте git-репозиторий и установите зависимости.

```bash
git clone https://github.com/Dan1van/uWSGI-server.git
pip install -r requirements.txt
```

Настройте файл конфигурации **uwsgi.ini**, установив полный путь до фреймворка в chdir:

```ini
[uwsgi]
# socket [addr:port]
http = 127.0.0.1:8081

# base app directory
# chdir = full/path
chdir = !YOUR PATH!

# WSGI module and callable
# module = [wsgi_module_name:application_callable_name]
module = wsgi:application

# master = [master process (true or false)]
master = true

# processes = [number of processes]
processes = 5
```

В файле **urls.yaml** можно изменить страницы, выдаваемые фреймворком:

```yaml
/ : {
  path: 'templates/main_page.html',
  status: '200 OK',
  headers: [
    ['Content-type', 'text/html'],
  ]
}

/catalog : {
  path: 'templates/catalog.html',
  status: '200 OK',
  headers: [
    ['Content-type', 'text/html'],
  ]
}

404_error_page: {
  path: 'templates/404error.html',
  status: '404 NOT FOUND',
  headers: [
    ['Content-type', 'text/html'],
  ]
}
```

## Использование
Введите в консоли:
```bash
uwsgi uwsgi.ini
```

Сервер запущен!

# English


uWSGI-server — it's a simple WSGI-framework, developed using Python.

## Installation

Clone the repository and install all requirements:


```bash
git clone https://github.com/Dan1van/uWSGI-server.git
pip install -r requirements.txt
```

Configure **uwsgi.ini** and set the full path to the uWSGI-server in chdir:

```ini
[uwsgi]
# socket [addr:port]
http = 127.0.0.1:8081

# base app directory
# chdir = full/path
chdir = !YOUR PATH!

# WSGI module and callable
# module = [wsgi_module_name:application_callable_name]
module = wsgi:application

# master = [master process (true or false)]
master = true

# processes = [number of processes]
processes = 5
```

You can change pages of the website in **urls.yaml** file:

```yaml
/ : {
  path: 'templates/main_page.html',
  status: '200 OK',
  headers: [
    ['Content-type', 'text/html'],
  ]
}

/catalog : {
  path: 'templates/catalog.html',
  status: '200 OK',
  headers: [
    ['Content-type', 'text/html'],
  ]
}

404_error_page: {
  path: 'templates/404error.html',
  status: '404 NOT FOUND',
  headers: [
    ['Content-type', 'text/html'],
  ]
}
```

## Usage

In console:

```bash
uwsgi uwsgi.ini
```

PROFIT!
