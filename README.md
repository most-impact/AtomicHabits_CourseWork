# Atomic Habits - Course Work

*Приложение для формирования полезных привычек по методике Джеймса Клира*

## Описание проекта

Этот проект представляет собой курсовую работу, посвященную применению принципов из книги "Атомные привычки" Джеймса Клира для формирования полезных привычек и избавления от вредных. Проект реализован как веб-приложение с использованием современных технологий.

**Основные возможности:**
- Трекер привычек с визуализацией прогресса
- Система вознаграждений за выполнение привычек
- Аналитика и статистика
- Персонализированные рекомендации

## 🛠 Технологический стек

### Frontend
- **React.js** (v18)
- **TypeScript**
- **Redux Toolkit** (состояние приложения)
- **Material-UI (MUI)** (UI компоненты)
- **React Hook Form + Yup** (формы и валидация)
- **Chart.js** (визуализация статистики)

### Backend
- **Node.js** (v16+)
- **Express.js**
- **MongoDB** (база данных)
- **Mongoose** (ODM)
- **JWT** (аутентификация)
- **Bcrypt** (хеширование паролей)

### Инфраструктура
- **Docker** (контейнеризация)
- **GitHub Actions** (CI/CD)
- **Nginx** (обратный прокси)

## 🚀 Запуск проекта

### Локальная разработка

1. **Клонируйте репозиторий:**
```bash
git clone https://github.com/most-impact/AtomicHabits_CourseWork.git
cd AtomicHabits_CourseWork
```

2. **Установите зависимости для клиента и сервера:**
```bash
# Для клиента
cd client
npm install

# Для сервера
cd ../server
npm install
```

3. **Настройте переменные окружения:**

- Создайте файл .env в папке server на основе .env.example
- Укажите ваши настройки MongoDB и секретный ключ JWT:
   ```bash
  MONGO_URI=mongodb://localhost:27017/atomic_habits
  JWT_SECRET=your_strong_secret_here
  PORT=5000
  ```
  
4. **Запустите приложение:**

```bash
# В одном терминале (сервер)
cd server
npm run dev

# В другом терминале (клиент)
cd ../client
npm start
```

### Развертывание на сервере

1. **Установите на сервер:**

```bash
git clone https://github.com/most-impact/AtomicHabits_CourseWork.git
cd AtomicHabits_CourseWork
```

2. **Установите зависимости и настройте окружение как в локальной установке.**
3. **Для production-сборки:**

```bash
# Клиент
cd client
npm run build

# Сервер (с PM2 для процесса)
cd ../server
npm install -g pm2
pm2 start server.js --name "atomic-habits-api"
```

4. **Настройте Nginx как reverse proxy:**

```bash
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    location /api {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
    }
}
```

## CI/CD Pipeline
Проект использует GitHub Actions для автоматического развертывания. Пример конфигурации .github/workflows/deploy.yml:

```bash
name: Deploy to Production

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    
    - name: Install dependencies
      run: |
        cd client && npm install
        cd ../server && npm install
        
    - name: Run tests
      run: |
        cd client && npm test
        cd ../server && npm test
        
    - name: Deploy to server
      uses: appleboy/ssh-action@master
      with:
        host: ${{ secrets.SERVER_IP }}
        username: ${{ secrets.SERVER_USER }}
        key: ${{ secrets.SSH_PRIVATE_KEY }}
        script: |
          cd /var/www/AtomicHabits_CourseWork
          git pull origin main
          cd client && npm run build
          pm2 restart all
```
