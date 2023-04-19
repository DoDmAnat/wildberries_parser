Цель задания: создать сервис на FastAPI, который будет взаимодействовать с сайтом
https://www.wildberries.ru/. Необходимо реализовать 4 конечные точки для работы с
номенклатурой.
Требования:
1. Используйте FastAPI для разработки сервиса.(+)
2. Используйте парсинг данных с сайта https://www.wildberries.ru/ с использованием библиотеки
requests.(+)
3. Реализуйте 4 конечные точки:(+)
- Добавить номенклатуру: пользователь указывает nm_id, сервис парсит данные с сайта
www.wildberries.ru и сохраняет их в базу данных PostgreSQL
- Получить товар по номенклатуре
- Получить все товары
- Удалить товар по номенклатуре
4. Товар должен содержать следующие поля:(+)
• nm_id
• name
• brand
• brand_id
• site_brand_id
• supplier_id
• sale
• price
• sale_price
• rating
• feedbacks
• colors
5. Используйте Docker для развертывания сервиса.(+)
6. Используйте SQLAlchemy для работы с базой данных PostgreSQL.(+)
Дополнительное задание:
1. Реализуйте задачу в Celery для обновления карточек товаров, которые хранятся в базе данных.(+)
2. Настройте подключение CORS для сервиса.
3. Дополнительное поле в таблице (quantity - количество товара в наличии). Обновление остатков.

## **Запуск проекта**

Выполните следующие команды в терминале:

1. Клонировать проект из репозитория

```
git clone https://github.com/DoDmAnat/wildberries_parser
```

2. Перейти в папку проекта и создать файл «.env», добавив в него переменные окружения.

```
cd wildberries_parser
```

```
touch .env
```

```
DB_HOST=db
DB_PORT=1221
DB_USER=postgres
DB_PASS=postgres
DB_NAME=postgres

POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

REDIS_HOST=redis
REDIS_PORT=5370
```

3. Выполнить команду запуска docker-compose в «фоновом режиме»

```
docker-compose up -d --build
```

4. Открыть эндпоинт

```
localhost:9999/docs
```

4 конечные точки:

- добавить товар по номенклатуре

```bash

POST - '/products/{nm_id}/'

```
- получить товар из базы по номенклатуре

```bash

GET - '/products/{nm_id}/'

```

- удалить товар по номенклатуре

```bash

DELETE - '/products/{nm_id}/'

```
-  получить все товары из базы

```bash

GET - '/products/{nm_id}/'

```
