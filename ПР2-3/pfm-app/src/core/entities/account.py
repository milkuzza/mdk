"""
Модуль содержит класс Account для представления счета
"""

from decimal import Decimal


class Account:
    """Класс для представления финансового счета"""
    
    def __init__(self, name: str, initial_balance: Decimal = Decimal('0'), account_id: int = None):
        self.id = account_id
        self.name = name
        self.balance = initial_balance
    
    def __str__(self):
        return f"{self.name}: {self.balance}"
