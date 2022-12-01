import customtkinter
import customtkinter as tk

from src import validators, commands


def main(function, default_start_element):
    start_element = default_start_element

    root = tk.CTk()
    root.geometry("500x500")
    root.title("Допълнение към курса по ДИС - Курсов проект №1")

    frame = tk.CTkFrame(root)
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    label = tk.CTkLabel(frame, text="λ = {}\n".format(start_element))
    label.pack(padx=10, pady=10)

    answer_box = tk.CTkTextbox(frame, text_font=("Roboto", 12))

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

        label.configure(text="λ = {}\n".format(start_element))

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
    find_element_button.pack(padx=5, pady=2, side=tk.RIGHT)
    find_element_entry = tk.CTkEntry(find_element, placeholder_text="n = ?")
    find_element_entry.pack(padx=5, pady=5, side=tk.RIGHT)

    answer_box.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

    root.mainloop()


def order_function(an: float):
    return (2 * an * an - an + 6) / (an - 6)


if __name__ == '__main__':
    customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("dark-blue")

    main(order_function, 0)
