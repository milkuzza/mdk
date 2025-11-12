"""
Главный класс приложения Personal Finance Manager
"""

import tkinter as tk
from tkinter import messagebox


class FinanceApp:
    """Главный класс приложения для управления личными финансами"""
    
    def __init__(self):
        self.root = None
    
    def run(self):
        """Запуск приложения"""
        try:
            self.root = tk.Tk()
            self.root.title("Personal Finance Manager")
            self.root.geometry("800x600")
            
            # Временная заглушка для демонстрации
            label = tk.Label(self.root, text="Personal Finance Manager", font=("Arial", 16))
            label.pack(pady=50)
            
            self.root.mainloop()
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка запуска приложения: {str(e)}")
