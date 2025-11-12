-- Скрипт инициализации базы данных для Personal Finance Manager

-- Таблица категорий
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица операций
CREATE TABLE IF NOT EXISTS operations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount DECIMAL(10,2) NOT NULL,
    type TEXT NOT NULL CHECK (type IN ('income', 'expense')),
    category_id INTEGER NOT NULL,
    description TEXT,
    date TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories (id)
);

-- Индексы для оптимизации запросов
CREATE INDEX IF NOT EXISTS idx_operations_date ON operations(date);
CREATE INDEX IF NOT EXISTS idx_operations_type ON operations(type);
CREATE INDEX IF NOT EXISTS idx_operations_category ON operations(category_id);

-- Начальные данные - базовые категории
INSERT OR IGNORE INTO categories (name) VALUES 
    ('Еда'),
    ('Транспорт'),
    ('Развлечения'),
    ('Здоровье'),
    ('Одежда'),
    ('Образование'),
    ('Зарплата'),
    ('Подработка'),
    ('Другое');
