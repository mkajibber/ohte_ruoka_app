
from tkinter import Tk, ttk, constants



class CreateUserView:
    def __init__(self, root):
        self._root = root
        self._name_label = None
        self._username_label = None
        self._password_label = None
        self._username_entry = None
        self._password_entry = None
        self._name_entry = None
        self._heading_label = None
        self._hide_password_checkbutton = None
        self._password_show_status = False


    def _handle_hide_password_checkbutton_click(self):
        if self._password_show_status:
            self._password_show_status = False
            self._password_entry.configure(show="*")

        else:
            self._password_show_status = True
            self._password_entry.configure(show="")


    def _handle_button_click(self):
        entry_value = {
            "name": self._name_entry.get(),
            "username": self._username_entry.get(),
            "password": self._password_entry.get()

        }
        print(f"Create new user with credentials: {entry_value}")

    def start(self):
        self._heading_label = ttk.Label(master=self._root, text="Create new user")
        self._name_label = ttk.Label(master=self._root, text="Name")
        self._name_entry = ttk.Entry(master=self._root)
        self._username_label = ttk.Label(master=self._root, text="Username")
        self._username_entry = ttk.Entry(master=self._root)
        self._password_label = ttk.Label(master=self._root, text="Password")
        self._password_entry = ttk.Entry(master=self._root, show='*')

        self._button = ttk.Button(
            master=self._root,
            text="Create user",
            command=self._handle_button_click
        )

        self._hide_password_checkbutton = ttk.Checkbutton(
            master=self._root,
            text="Show password",
            command=self._handle_hide_password_checkbutton_click
        )

        # asettelu
        self._heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
        self._name_label.grid(row=1, column=0, padx=5, pady=5)
        self._name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=(constants.E, constants.W))
        self._username_label.grid(row=2, column=0, padx=5, pady=5)
        self._username_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._password_label.grid(row=3, column=0, padx=5, pady=5)
        self._password_entry.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._hide_password_checkbutton.grid(row=4, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._button.grid(row=5, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        # toisen kolumnin venyttäminen horisontaalisti minimileveyteen
        self._root.grid_columnconfigure(1, weight=1, minsize=300)






class LoginView:
    def __init__(self, root):
        self._root = root
        self._username_label = None
        self._username_label = None
        self._username_entry = None
        self._password_entry = None
        self._heading_label = None
        self._button = None
        self._hide_password_checkbutton = None
        self._password_show_status = False


    def _handle_hide_password_checkbutton_click(self):
        if self._password_show_status:
            self._password_show_status = False
            self._password_entry.configure(show="*")

        else:
            self._password_show_status = True
            self._password_entry.configure(show="")


    def _handle_button_click(self):
        entry_value = {
            "username": self._username_entry.get(),
            "password": self._password_entry.get()

        }
        print(f"Login user with credentials: {entry_value}")


    def start(self):
        self._heading_label = ttk.Label(master=self._root, text="Login")
        self._username_label = ttk.Label(master=self._root, text="Username")
        self._username_entry = ttk.Entry(master=self._root)
        self._password_label = ttk.Label(master=self._root, text="Password")
        self._password_entry = ttk.Entry(master=self._root, show="*")

        self._button = ttk.Button(
            master=self._root,
            text="Button",
            command=self._handle_button_click
        )

        self._hide_password_checkbutton = ttk.Checkbutton(
            master=self._root,
            text="Show password",
            command=self._handle_hide_password_checkbutton_click
        )

        # vasempaan laitaan
        self._heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W)

        self._username_label.grid(row=1, column=0)
        # vasempaan ja oikeaan laitaan
        self._username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W))

        self._password_label.grid(row=2, column=0)
        # vasempaan ja oikeaan laitaan
        self._password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W))

        # vasemaan ja oikeaan laitaan
        self._hide_password_checkbutton.grid(row=3, column=1, sticky=(constants.E, constants.W))

        # vasempaan ja oikeaan laitaan
        self._button.grid(row=4, column=0, columnspan=2, sticky=(constants.E, constants.W))

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