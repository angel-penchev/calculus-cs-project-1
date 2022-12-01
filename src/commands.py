import customtkinter as tk

DIGIT_ROUNDING = 4


def find_element_at_index(function, start_element, index, answer_textbox: tk.CTkTextbox):
    try:
        index = int(index)
    except ValueError:
        answer_textbox.configure(state=tk.NORMAL)
        answer_textbox.insert(tk.END, "Невалиден индекс!\n")
        answer_textbox.configure(state=tk.DISABLED)
        return

    result = start_element
    current = start_element

    for i in range(1, index):
        result = function(current)
        current = result

    answer_textbox.configure(state=tk.NORMAL)
    answer_textbox.insert(tk.END, "a{} = {}\n".format(index, round(result, DIGIT_ROUNDING)))
    answer_textbox.configure(state=tk.DISABLED)


def find_first_n_elements(function, start_element, n, answer_textbox: tk.CTkTextbox):
    try:
        n = int(n)
    except ValueError:
        answer_textbox.configure(state=tk.NORMAL)
        answer_textbox.insert(tk.END, "Невалидно число за n!\n")
        answer_textbox.configure(state=tk.DISABLED)
        return

    result = start_element
    current = start_element

    for i in range(1, n + 1):
        result = function(current)
        current = result
        find_element_at_index(function, start_element, i, answer_textbox)
