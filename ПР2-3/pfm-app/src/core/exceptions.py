"""
Пользовательские исключения для бизнес-логики приложения
"""


class FinanceAppException(Exception):
    """Базовый класс для исключений приложения"""
    pass


class InvalidAmountException(FinanceAppException):
    """Исключение для некорректной суммы операции"""
    pass


class CategoryNotFoundException(FinanceAppException):
    """Исключение для случаев, когда категория не найдена"""
    pass


class OperationNotFoundException(FinanceAppException):
    """Исключение для случаев, когда операция не найдена"""
    pass
