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
        try:
            result = function(current)
        except ZeroDivisionError:
            answer_textbox.configure(state=tk.NORMAL)
            answer_textbox.insert(tk.END, "Деление на 0!\n")
            answer_textbox.configure(state=tk.DISABLED)
            return
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
        try:
            result = function(current)
        except ZeroDivisionError:
            answer_textbox.configure(state=tk.NORMAL)
            answer_textbox.insert(tk.END, "Деление на 0!\n")
            answer_textbox.configure(state=tk.DISABLED)
            return
        current = result
        find_element_at_index(function, start_element, i, answer_textbox)


def find_limit(function, start_element, answer_box):
    result = "Граница при λ={}: ".format(start_element)
    if start_element == 6:
        result += "н.р."
    elif start_element < -3 or (- 3 < start_element < -2) or (1.5 < start_element < 2):
        result += "-infinity"
    elif start_element == 3 or start_element == 1.5:
        result += "3"
    elif -2 <= start_element < 1.5:
        result += "-2"
    elif start_element == 2:
        result += "-3"

    answer_box.configure(state=tk.NORMAL)
    answer_box.insert(tk.END, result + '\n')
    answer_box.configure(state=tk.DISABLED)
