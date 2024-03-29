# Docker-Compose
Сама структура:
docker-compose.yml
|_ services:
|_ _ flask_app (1 контейнер):
|_ _ _ приложение Flask
|_ _ _ _ Dockerfile
|_ _ _ _ _ requirements.txt (библиотеки)
|_ _ _ _ _ templates:
|_ _ _ index.html
|_ _ _ _ result.html
|_ _ db (2 контейнер):
|_ _ _ init.sql (база данных)

Запустить docker compose можно с помощью команды sudo docker-compose up
Если изменяли какой-нибудь контейнер, то необходимо обновить с помощью команды sudo docker-compose up --build.

Полезные команды:
* sudo touch (название) - создание файлов в каталоге.
* mkdir (название) - создание каталога.
* cd (название каталога) - переход в каталог.
* cd .. - выйти из каталога.
* ls - просмотр всех файлов.
