import customtkinter
import customtkinter as tk
from PIL import Image, ImageTk

from src import validators, commands


def main(function, default_start_element):
    start_element = default_start_element

    root = tk.CTk()
    root.geometry("700x600")
    root.title("Допълнение към курса по ДИС - Курсов проект №1")

    frame = tk.CTkFrame(root)
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


    image = Image.open("assets/task_fixed_bg.png")
    render = ImageTk.PhotoImage(image)
    label_image = tk.CTkLabel(
        frame,
        text=". . .",
        image=render,
    )
    image.image = render
    label_image.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    label_start_element = tk.CTkLabel(frame, text="λ = {}\n".format(start_element))
    label_start_element.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    answer_box = tk.CTkTextbox(frame, state=tk.DISABLED)

    set_start_element = tk.CTkFrame(frame)
    set_start_element.pack(padx=10, pady=5, fill=tk.BOTH, expand=False)
    set_start_label = tk.CTkLabel(set_start_element, text="Задаване на стойност за λ")
    set_start_label.pack(side=tk.LEFT, padx=5, pady=5)
    set_start_entry = tk.CTkEntry(set_start_element, placeholder_text="λ = ?")

    def command():
        nonlocal start_element
        try:
            start_element = float(set_start_entry.get())
        except ValueError:
            answer_box.insert(tk.END, "Невалидна стойност за λ!\n")
            return

        label_start_element.configure(text="λ = {}\n".format(start_element))

    set_start_button = tk.CTkButton(
        set_start_element,
        text="▶",
        command=lambda: command()
    )
    set_start_button.pack(side=tk.RIGHT, padx=5, pady=5)
    set_start_entry.pack(side=tk.RIGHT, padx=5, pady=5)

    find_element = tk.CTkFrame(frame)
    find_element.pack(padx=10, pady=5, fill=tk.BOTH, expand=False)
    find_element_label = tk.CTkLabel(find_element, text="Намиране на елемент от редицата")
    find_element_label.pack(padx=5, pady=5, side=tk.LEFT)
    find_element_button = tk.CTkButton(
        master=find_element,
        text="▶",
        command=lambda: commands.find_element_at_index(function, start_element, find_element_entry.get(), answer_box))
    find_element_button.pack(padx=5, pady=5, side=tk.RIGHT)
    find_element_entry = tk.CTkEntry(find_element, placeholder_text="n = ?")
    find_element_entry.pack(padx=5, pady=5, side=tk.RIGHT)

    find_first_n_element = tk.CTkFrame(frame)
    find_first_n_element.pack(padx=10, pady=5, fill=tk.BOTH, expand=False)
    find_first_n_element_label = tk.CTkLabel(find_first_n_element, text="Намиране на първите n елемента от редицата")
    find_first_n_element_label.pack(padx=5, pady=5, side=tk.LEFT)
    find_first_n_entry = tk.CTkEntry(find_first_n_element, placeholder_text="n = ?")
    find_first_n_element_button = tk.CTkButton(
        master=find_first_n_element,
        text="▶",
        command=lambda: commands.find_first_n_elements(function, start_element, find_first_n_entry.get(), answer_box))
    find_first_n_element_button.pack(padx=5, pady=5, side=tk.RIGHT)
    find_first_n_entry.pack(padx=5, pady=5, side=tk.RIGHT)

    find_limit = tk.CTkFrame(frame)
    find_limit.pack(padx=10, pady=5, fill=tk.BOTH, expand=False)
    find_limit_label = tk.CTkLabel(find_limit, text="Намиране на границата на редицата")
    find_limit_label.pack(padx=5, pady=5, side=tk.LEFT)
    find_limit_button = tk.CTkButton(
        master=find_limit,
        text="▶",
        command=lambda: commands.find_limit(function, start_element, answer_box))
    find_limit_button.pack(padx=5, pady=5, side=tk.RIGHT)

    answer_box.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

    root.mainloop()


def order_function(an: float):
    return (2 * an * an - an + 6) / (an - 6)


if __name__ == '__main__':
    customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("dark-blue")

    main(order_function, 0)
