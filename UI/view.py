import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._retailer = None
        self._brand = None
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._year = None
        self._btn_topSales = None
        self._btn_analizeSales = None
        self._txt_result = None
        self._txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)

        #ROW 1
        # text field for the name
        self._year = ft.Dropdown(
            label="anno",
            width=200,
            options=[ft.dropdown.Option("Nessun filtro")]
        )
        self._controller.fillYear()

        self._brand = ft.Dropdown(
            label="brand",
            width=200,
            options=[ft.dropdown.Option("Nessun filtro")]
        )
        self._controller.fillBrand()

        self._retailer = ft.Dropdown(
            label="retailer",
            width=300,
            options=[ft.dropdown.Option("Nessun filtro")]
        )
        self._controller.fillRetailer()

        row1 = ft.Row([self._year,self._brand,self._retailer],
                      alignment=ft.MainAxisAlignment.CENTER)

        # button for the "hello" reply
        self._btn_topSales = ft.ElevatedButton(text="Top vendite", on_click=self._controller.handleTopSales)
        self._btn_analizeSales = ft.ElevatedButton(text="Analizza vendite", on_click=self._controller.handleAnalizeSales)

        row2 = ft.Row([self._btn_topSales,self._btn_analizeSales],
                      alignment=ft.MainAxisAlignment.CENTER)

        # List View where the reply is printed
        self._txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        self._page.add(self._title,row1,row2,self._txt_result)

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

