"""task_2.py"""


import json
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import requests


class Post:
    """Post class"""

    def __init__(self, _id):
        """init method

        Args:
            _id (int): id
        """
        self.id = _id
        self.data = self.fetch_data()
        self.filename = f'post_{_id}.json'
        self.save_to_file()

    def fetch_data(self):
        """fetch data from JSONplaceholder

        Returns:
            response(json): response
        """
        response = requests.get(
            f'https://jsonplaceholder.typicode.com/posts/{self.id}', timeout=60)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def save_to_file(self):
        """save to file"""
        with open(self.filename, 'w', encoding="utf-8") as f:
            json.dump(self.data, f)


class GUI:
    """GUI class"""

    def __init__(self):
        """init method"""
        self.root = tk.Tk()
        self.root.withdraw()
        self.messagebox = messagebox
        self.simpledialog = simpledialog

    def input(self):
        """input method"""
        _id = self.simpledialog.askstring(
            "Input", "Введите ID:", parent=self.root)
        return _id


class App(GUI):
    """Класс, представляющий приложение, наследующий от класса GUI"""

    def main(self):
        """main method"""
        _id = self.input()
        if _id is not None:
            post = Post(_id)
            self.messagebox.showinfo(
                "Успех", f"Данные сохранены в файл {post.filename}")
        else:
            self.messagebox.showinfo(
                "Ошибка", "Не удалось получить данные")
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.main()
