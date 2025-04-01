from datetime import datetime

from pydantic.dataclasses import dataclass


@dataclass
class DailySales:
    Retailer_code:int
    Product_number:int
    Order_method_code:int
    Date:datetime
    Quantity:int
    Unit_price:float
    Unit_sale_price:float

    def __eq__(self, other):
        return self.Retailer_code==other.Retailer_code and self.Product_number==other.Product_number and self.Order_method_code==other.Order_method_code and self.Date==other.Date and self.Quantity==other.Quantity
    def __hash__(self):
        return hash(self)
    def __str__(self):
        pass