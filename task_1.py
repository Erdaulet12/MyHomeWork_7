"""task_1.py"""

import json
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import requests


def fetch_data(_id):
    """ вытягивает данные из JSONplaceholder

    Args:
        id (int): id

    Returns:
        response(json): responce
    """
    response = requests.get(
        f'https://jsonplaceholder.typicode.com/posts/{_id}', timeout=60)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def save_to_file(data, filename):
    """ Сохранение данных в json файл

    Args:
        data (input): Поле ввода
        filename (str): Файл
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)


def main():
    """main method"""
    root = tk.Tk()
    root.withdraw()

    _id = simpledialog.askstring("Input", "Введите ID:", parent=root)
    data = fetch_data(_id)

    if data is not None:
        filename = f'post_{_id}.json'
        save_to_file(data, filename)
        messagebox.showinfo("Успех", f"Данные сохранены в файл {filename}")
    else:
        messagebox.showinfo("Ошибка", "Не удалось получить данные")

    root.mainloop()


if __name__ == "__main__":
    main()
