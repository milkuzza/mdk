"""
Модуль содержит класс Operation для представления финансовой операции
"""

from datetime import datetime
from decimal import Decimal
from typing import Optional


class Operation:
    """Класс для представления финансовой операции"""
    
    def __init__(
        self, 
        amount: Decimal,
        operation_type: str,
        category: str,
        description: str = "",
        date: Optional[datetime] = None,
        operation_id: Optional[int] = None
    ):
        self.id = operation_id
        self.amount = amount
        self.type = operation_type  # 'income' или 'expense'
        self.category = category
        self.description = description
        self.date = date or datetime.now()
    
    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d')} {self.type}: {self.amount} ({self.category})"
