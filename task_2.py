import json
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import requests


class DataFetcher:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()

    def fetch_data(self, _id):
        """ Вытягивает данные из JSONplaceholder

        Args:
            _id (int): ID

        Returns:
            dict or None: Возвращает словарь данных или None, если запрос не удался
        """
        response = requests.get(
            f'https://jsonplaceholder.typicode.com/posts/{_id}', timeout=60)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def save_to_file(self, data, filename):
        """ Сохранение данных в json файл

        Args:
            data (dict): Данные для сохранения
            filename (str): Имя файла
        """
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(data, f)

    def get_id_from_user(self):
        """Запрашивает у пользователя ввод ID"""
        return simpledialog.askstring("Input", "Введите ID:", parent=self.root)

    def show_success_message(self, filename):
        """Отображает сообщение об успешном сохранении данных"""
        messagebox.showinfo("Успех", f"Данные сохранены в файл {filename}")

    def show_error_message(self):
        """ Отображает сообщение об ошибке """
        messagebox.showinfo("Ошибка", "Не удалось получить данные")

    def main(self):
        _id = self.get_id_from_user()
        data = self.fetch_data(_id)

        if data is not None:
            filename = f'post_{_id}.json'
            self.save_to_file(data, filename)
            self.show_success_message(filename)
        else:
            self.show_error_message()

        self.root.mainloop()


if __name__ == "__main__":
    data_fetcher = DataFetcher()
    data_fetcher.main()
