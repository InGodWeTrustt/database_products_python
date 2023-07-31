import tkinter as tk
from package.app import App
from package.constants import APP_CONFIG

app = App(**APP_CONFIG)
app.mainloop()