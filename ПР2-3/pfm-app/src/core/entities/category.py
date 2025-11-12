"""
Модуль содержит класс Category для представления категории операций
"""


class Category:
    """Класс для представления категории финансовых операций"""
    
    def __init__(self, name: str, category_id: int = None):
        self.id = category_id
        self.name = name
    
    def __str__(self):
        return self.name
    
    def __eq__(self, other):
        if isinstance(other, Category):
            return self.name == other.name
        return False
