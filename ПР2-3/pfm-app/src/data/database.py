"""
Модуль для управления подключением к базе данных SQLite
"""

import sqlite3
import os
from typing import Optional


class Database:
    """Класс для управления подключением к базе данных"""
    
    def __init__(self, db_path: str = "data/finance.db"):
        self.db_path = db_path
        self.connection: Optional[sqlite3.Connection] = None
    
    def connect(self):
        """Создание соединения с базой данных"""
        # Создаем папку data если её нет
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row  # Доступ к колонкам по имени
        return self.connection
    
    def close(self):
        """Закрытие соединения с базой данных"""
        if self.connection:
            self.connection.close()
            self.connection = None
    
    def execute_script(self, script_path: str):
        """Выполнение SQL скрипта из файла"""
        if not self.connection:
            self.connect()
        
        with open(script_path, 'r', encoding='utf-8') as file:
            script = file.read()
            self.connection.executescript(script)
