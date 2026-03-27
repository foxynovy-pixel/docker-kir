Это простое веб-приложение на Flask, которое демонстрирует работу с Docker, Redis и Docker Compose. 
Приложение:
Отображает веб-страницу с счётчиком посещений
Каждое обновление страницы увеличивает счётчик в Redis
Сохраняет значение счётчика даже после перезапуска контейнеров благодаря Docker volume
Структура:
docker-practice/
├── app/
│   ├── app.py              # Flask приложение
│   ├── requirements.txt    # Python зависимости
│   └── templates/
│       └── index.html      # HTML шаблон
├── Dockerfile              # Инструкции для сборки образа
├── docker-compose.yml      # Оркестрация сервисов
├── .dockerignore          # Исключения для Docker
└── README.md              # Документация
Cборка приложения:
docker build -t flask-app .
Запуск:
docker run -d -p 5000:5000 -e APP_ENV=dev --name flask-container flask-app
Запуск с Compose:
docker-compose up -d
Команды для проверок:
# 1. Вывести список контейнеров
docker ps
# или все контейнеры (включая остановленные)
docker ps -a
# 2. Вывести список образов
docker images
# 3. Вывести список томов
docker volume ls
# 4. Посмотреть логи сервиса web
docker-compose logs web
# 5. Посмотреть логи сервиса redis
docker-compose logs redis
# 6. Выполнить команду внутри контейнера web
docker exec -it docker-kir-web-1 /bin/bash
# 7. Остановить проект
docker-compose stop
# 8. Удалить неиспользуемые объекты Docker безопасной командой
docker system prune -f
