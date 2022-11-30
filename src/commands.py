import customtkinter as tk

DIGIT_ROUNDING = 4


def find_element_at_index(function, start_element, index, answer_textbox: tk.CTkTextbox):
    try:
        index = int(index)
    except ValueError:
        answer_textbox.insert(tk.END, "Невалиден индекс!\n")
        return

    result = start_element
    current = start_element

    for i in range(index):
        result = function(current)
        current = result

    answer_textbox.insert(tk.END, "a{} = {}\n".format(index, round(result, DIGIT_ROUNDING)))
