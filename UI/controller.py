import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleTopSales(self, e):
        self._view._txt_result.clean()
        anno=self._view._year.value
        if anno=="Nessun filtro":
            anno=None
            self._view.update_page()
        brand = self._view._brand.value
        if brand == "Nessun filtro":
            brand = None
            self._view.update_page()
        retailer = self._view._retailer.value
        if retailer == "Nessun filtro":
            retailer = None
            self._view.update_page()
        vendite=self._model.getTopSales(anno,brand,retailer)

        if len(vendite)==0:
            self._view.create_alert("Nessun risultato trovato")
            self._view.update_page()
            return

        self._view._txt_result.controls.append(ft.Text("Top 5 Vendite:"))
        for row in vendite:
            self._view._txt_result.controls.append(ft.Text(f"Data: {row[0]}; Ricavo: {row[3]:.2f}€; Retailer: {row[2]};  Product: {row[1]}"))

        self._view.update_page()

    def handleAnalizeSales(self,e):
        self._view._txt_result.clean()
        anno = self._view._year.value
        if anno == "Nessun filtro":
            anno = None
            self._view.update_page()
        brand = self._view._brand.value
        if brand == "Nessun filtro":
            brand = None
            self._view.update_page()
        retailer = self._view._retailer.value
        if retailer == "Nessun filtro":
            retailer = None
            self._view.update_page()
        vendita = self._model.analizeSales(anno, brand, retailer)

        print(vendita)

        if vendita[0] is None:
            self._view.create_alert("Nessun risultato trovato")
            self._view.update_page()
            return

        self._view._txt_result.controls.append(ft.Text("Analisi vendite:"))
        self._view._txt_result.controls.append(ft.Text(f"Giro d'affari totale: {vendita[0]:,.2f}€"))
        self._view._txt_result.controls.append(ft.Text(f"Numero di vendite: {vendita[1]}"))
        self._view._txt_result.controls.append(ft.Text(f"Numero di retailer coinvolti: {vendita[2]}"))
        self._view._txt_result.controls.append(ft.Text(f"Numero di prodotti coinvolti: {vendita[3]}"))

        self._view.update_page()

    def fillBrand(self):
        for p in self._model.getBrand():
            self._view._brand.options.append(ft.dropdown.Option(p))

    def fillYear(self):
        for y in self._model.getYear():
            self._view._year.options.append(ft.dropdown.Option(y))

    def fillRetailer(self):
        for r in self._model.getRetailer():
            self._view._retailer.options.append((ft.dropdown.Option(key= r.Retailer_code,
                                                text=r.Retailer_name,
                                                data=r, on_click=self.read_retailer)))

    def read_retailer(self, e): \
        self._retailer = e.control.data