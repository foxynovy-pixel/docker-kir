import os
import redis
from flask import Flask, render_template

app = Flask(__name__)

# Получаем хост Redis из переменной окружения
# По умолчанию используем 'localhost' для локальной разработки
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))

# Добавляем обработку ошибок подключения
try:
    redis_client = redis.Redis(
        host=redis_host, 
        port=redis_port, 
        decode_responses=True,
        socket_connect_timeout=5  # Таймаут подключения 5 секунд
    )
    # Проверяем подключение
    redis_client.ping()
    redis_connected = True
except redis.ConnectionError as e:
    print(f"Warning: Could not connect to Redis at {redis_host}:{redis_port}")
    print(f"Error: {e}")
    redis_connected = False
    # Создаем dummy client для случаев, когда Redis недоступен
    class DummyRedis:
        def incr(self, key):
            return "Redis unavailable"
    redis_client = DummyRedis()

@app.route('/')
def index():
    if redis_connected:
        try:
            counter = redis_client.incr('counter')
        except:
            counter = "Error connecting to Redis"
    else:
        counter = "Redis connection failed"
    
    env = os.getenv('APP_ENV', 'production')
    redis_host_display = os.getenv('REDIS_HOST', 'localhost')
    
    return render_template(
        'index.html', 
        counter=counter, 
        env=env,
        redis_host=redis_host_display,
        redis_connected=redis_connected
    )

@app.route('/health')
def health():
    """Endpoint для проверки здоровья приложения"""
    return {
        'status': 'ok',
        'redis_connected': redis_connected,
        'redis_host': redis_host
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
     