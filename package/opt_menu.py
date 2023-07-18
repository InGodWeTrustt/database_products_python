import tkinter as tk

class OptMenu:

    def __init__(self, root, row_idx, col_idx):
        self._category_value = tk.StringVar(root)

        # Create the list of options
        category_list = ["Молочные продукты", "Прочее", "Яйца, каша, мясо и рыба", "Уценка", "Овощи", "Фрукты", "Одежда и обувь", "Вода"] 

        # Set the default value of the variable
        self._category_value.set(category_list[0])

        # Create the optionmenu widget and passing the options_list and value_inside to it.
        category_menu = tk.OptionMenu(root, self._category_value, *category_list)
        category_menu.grid(row=row_idx, column=col_idx)
   
    @property
    def category_value(self):
        return self._category_value.get()