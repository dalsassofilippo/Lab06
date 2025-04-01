from database.DAO import DAO

class Model:
    def __init__(self):
        pass

    def getBrand(self):
        return DAO.getBrand()

    def getYear(self):
        return DAO.getYear()

    def getRetailer(self):
        return DAO.getRetailer()

    def getTopSales(self,a,b,r):
        return DAO.getTopSales(a,b,r)

    def analizeSales(self,a,b,r):
        return DAO.analizeSales(a,b,r)