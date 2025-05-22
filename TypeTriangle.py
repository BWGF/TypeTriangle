import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
import math

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def calculate_triangle():
    global triangle_count, not_triangle_count, calculate_count, triangle_types
    calculate_count += 1
    try:
        a = entry_a.get()
        b = entry_b.get()
        c = entry_c.get()
        if not is_number(a) or not is_number(b) or not is_number(c):
            raise ValueError("Введите числа")
        a, b, c = float(a), float(b), float(c)
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Стороны должны быть больше нуля")
        if a + b <= c or a + c <= b or b + c <= a:
            not_triangle_count += 1
            result = "Фигура не является треугольником"
            triangle_type = "не треугольник"
        elif math.isclose(a, b, rel_tol=1e-9) and math.isclose(b, c, rel_tol=1e-9):
            triangle_type = "равносторонний"
            result = "Фигура является равносторонним треугольником"
        elif math.isclose(a, b, rel_tol=1e-9) or math.isclose(a, c, rel_tol=1e-9) or math.isclose(b, c, rel_tol=1e-9):
            triangle_type = "равнобедренный"
            result = "Фигура является равнобедренным треугольником"
        elif math.isclose(pow(a, 2) + pow(b, 2), pow(c, 2), rel_tol=1e-9) or \
             math.isclose(pow(a, 2) + pow(c, 2), pow(b, 2), rel_tol=1e-9) or \
             math.isclose(pow(b, 2) + pow(c, 2), pow(a, 2), rel_tol=1e-9):
            triangle_type = "прямоугольный"
            result = "Фигура является прямоугольным треугольником"
        else:
            triangle_type = "разносторонний"
            result = "Фигура является разносторонним треугольником"

        if triangle_type != "не треугольник":
            if triangle_type not in triangle_types:
                triangle_types.add(triangle_type)
                triangle_count += 1

        result_label.config(text=f"Результат: {result}")
        update_counts()
    except ValueError as e:
        messagebox.showerror("Ошибка ввода", str(e))

def update_counts():
    triangle_count_label.config(text=f"Треугольников: {triangle_count}")
    not_triangle_count_label.config(text=f"Не треугольников: {not_triangle_count}")
    calculate_count_label.config(text=f"Расчетов: {calculate_count}")

root = tk.Tk()
root.title("Треугольник")
root.geometry("400x400")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (400 / 2)
y = (screen_height / 2) - (400 / 2)
root.geometry(f"+{int(x)}+{int(y)}")

font_style = font.Font(size=13)

entry_a = tk.Entry(root)
entry_b = tk.Entry(root)
entry_c = tk.Entry(root)
result_label = tk.Label(root, text="Результат: ")
calculate_button = tk.Button(root, text="Рассчитать", command=calculate_triangle)
label_a = tk.Label(root, text="Сторона a: ", font=font_style)
label_b = tk.Label(root, text="Сторона b: ", font=font_style)
label_c = tk.Label(root, text="Сторона c: ", font=font_style)

label_a.place(relx=0.3, rely=0.1, anchor="e")
entry_a.place(relx=0.45, rely=0.1, anchor="center")
label_b.place(relx=0.3, rely=0.2, anchor="e")
entry_b.place(relx=0.45, rely=0.2, anchor="center")
label_c.place(relx=0.3, rely=0.3, anchor="e")
entry_c.place(relx=0.45, rely=0.3, anchor="center")
calculate_button.place(relx=0.5, rely=0.4, anchor="center")
result_label.place(relx=0.5, rely=0.5, anchor="center")

triangle_count = 0
not_triangle_count = 0
calculate_count = 0
triangle_types = set()

triangle_count_label = tk.Label(root, text=f"Треугольников: {triangle_count}")
not_triangle_count_label = tk.Label(root, text=f"Не треугольников: {not_triangle_count}")
calculate_count_label = tk.Label(root, text=f"Расчетов: {calculate_count}")

triangle_count_label.place(relx=0.5, rely=0.6, anchor="center")
not_triangle_count_label.place(relx=0.5, rely=0.7, anchor="center")
calculate_count_label.place(relx=0.5, rely=0.8, anchor="center")

root.mainloop()