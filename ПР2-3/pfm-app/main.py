#!/usr/bin/env python3
"""
Точка входа в приложение Personal Finance Manager
"""

import sys
import os

# Добавляем src в путь для импортов
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from application.app import FinanceApp


def main():
    """Главная функция приложения"""
    app = FinanceApp()
    app.run()


if __name__ == "__main__":
    main()
