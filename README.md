# Python Backend Developer Portfolio | FastAPI & Architecture Showcase

Привет! 
Это мой основной репозиторий-портфолио. Здесь собраны мои бэкенд-проекты, демонстрирующие навыки работы с FastAPI, PostgreSQL, Docker, а также глубокое понимание различных архитектурных паттернов.

---

## Технологический стек
* Языки: Python 3.10+, SQL
* Фреймворки: FastAPI, Pydantic, SQLAlchemy 2.0, Alembic
* Базы данных: PostgreSQL, Redis
* Инфраструктура: Docker, Docker Compose, Celery, Prometheus
* Архитектура и подходы: REST API, JWT Authentication, Clean Architecture, Onion Architecture, Modular Design, Dependency Injection, WebSockets.

---

## Навигация по проектам

### 1. FastAPI Shop (./src/fastapi_shop) — Основной проект (E-commerce API)
Полноценный асинхронный бэкенд для маркетплейса, полностью готовый к деплою.
* Ролевая модель: Разделение прав доступа (Admin, Seller, Buyer) с помощью безопасной JWT-авторизации (access/refresh токены).
* Умный поиск: Реализован продвинутый полнотекстовый поиск средствами PostgreSQL (TSVECTOR + ts_rank_cd).
* Бизнес-логика: Корзина товаров, транзакционное оформление заказов с контролем складских остатков, система отзывов с автоматическим пересчетом рейтинга.
* Инфраструктура: Полная контейнеризация (отдельные docker-compose для dev и prod сред).

### 2. Исследование архитектурных паттернов (Blog API)
Я реализовал один и тот же проект (API для блога) в пяти различных архитектурных парадигмах, чтобы на практике изучить изоляцию бизнес-логики и фреймворков:
* Monolith Architecture (./src/blog_monolit_arch) — Базовый подход (всё в одном).
* Layered Architecture (./src/blog_layer_arch) — Классическое разделение на слои (Routers -> Services -> Repositories).
* Modular Architecture (./src/blog_modul_arch) — Разделение приложения на независимые бизнес-модули (модуль постов, модуль категорий).
* Clean Architecture (./src/blog_clean_arch) — Чистая архитектура (Domain, Application, Infrastructure, Presentation) с жестким правилом зависимостей.
* Onion Architecture (./src/blog_onion_arch) — Луковая архитектура с инверсией зависимостей.

### 3. Микросервисы и Инфраструктура (./src/mini_projects_and_tasks)
Сборник небольших проектов для отработки специфических задач уровня Middle-разработчика:
* Celery & Redis: Настройка воркеров для выполнения фоновых и отложенных задач.
* Prometheus: Интеграция сбора метрик приложения для мониторинга.
* WebSockets: Реализация чата в реальном времени.
* Rate Limiting: Защита API от DDoS и спам-запросов (с использованием Redis).
* Docker / Dockerfile: Оптимизация сборки образов.

### 3. Алгоритмы (./src/algorithms)

### 4. мои способности(./src/my_ability)
---

## Как запустить основной проект (FastAPI Shop)

1. Клонируйте репозиторий:
   ```bash
   git clone [https://github.com/ВАШ_ЮЗЕРНЕЙМ/ВАШ_РЕПОЗИТОРИЙ.git](https://github.com/ВАШ_ЮЗЕРНЕЙМ/ВАШ_РЕПОЗИТОРИЙ.git)
   cd ВАШ_РЕПОЗИТОРИЙ/src/fastapi_shop
Создайте файл .env на основе примера (если требуется) и настройте переменные окружения.

Запустите проект через Docker Compose:

Bash
docker-compose up --build
Документация API (Swagger) будет доступна по адресу: http://localhost:8000/docs