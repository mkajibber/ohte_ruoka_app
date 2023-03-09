from tkinter import Tk, ttk, constants

class UI:
    def __init__(self, root):
        self._root = root
        self._username_label = None
        self._username_label = None
        self._username_entry = None
        self._password_entry = None
        self._heading_label = None
        self._button = None


    def _handle_button_click(self):
        entry_value = {
            "username": self._username_entry.get(),
            "password": self._password_entry.get()

        }
        print(f"Value of entry is: {entry_value}")


    def start(self):

        self._heading_label = ttk.Label(master=self._root, text="Login")

        self._username_label = ttk.Label(master=self._root, text="Username")
        self._username_entry = ttk.Entry(master=self._root)

        self._password_label = ttk.Label(master=self._root, text="Password")
        self._password_entry = ttk.Entry(master=self._root)

        self._button = ttk.Button(
            master=self._root,
            text="Button",
            command=self._handle_button_click
        )

        # vasempaan laitaan
        self._heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W)

        self._username_label.grid(row=1, column=0)
        # vasempaan ja oikeaan laitaan
        self._username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W))

        self._password_label.grid(row=2, column=0)
        # vasempaan ja oikeaan laitaan
        self._password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W))

        # vasempaan ja oikeaan laitaan
        self._button.grid(row=3, column=0, columnspan=2, sticky=(constants.E, constants.W))

        # konfiguroidaan toisen sarakkeen painoksi 1
        self._root.grid_columnconfigure(1, weight=1)

        # väljyyttä komponenttiasetteluun
        self._heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        self._username_label.grid(padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._password_label.grid(padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        # toisen kolumnin venyttäminen horisontaalisti minimileveyteen
        self._root.grid_columnconfigure(1, weight=1, minsize=300)






window = Tk()
window.title("Harjoitustyö, OhTe k23")

ui = UI(window)
ui.start()

window.mainloop()
