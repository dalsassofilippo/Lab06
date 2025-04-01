from pydantic.dataclasses import dataclass


@dataclass
class Methods:
    Order_method_code: int
    Order_method_type: str

    def __eq__(self, other):
        return self.Order_method_code==other.Order_method_code
    def __hash__(self):
        return hash(self.Order_method_code)
    def __str__(self):
        pass