from database.DB_connect import DBConnect
from model.products import Product
from model.retailer import Retailer

class DAO():

    @staticmethod
    def getBrand():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ SELECT DISTINCT g.Product_brand
                      FROM go_products g
                      """
        cursor.execute(query)

        res=[]
        for row in cursor:
            res.append((row["Product_brand"]))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getYear():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ SELECT DISTINCT YEAR(s.Date)
                      FROM go_daily_sales s
                      """
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append((row["YEAR(s.Date)"]))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getRetailer():
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=True)

        query=""" SELECT *
                  FROM go_retailers
                  """
        cursor.execute(query)

        res=[]
        for row in cursor:
            res.append(Retailer(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getTopSales(anno,brand,retailer):
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor()
        query = """
        SELECT 
    s.Date AS year, 
    p.Product_number AS brand, 
    s.Retailer_code AS retailer, 
    (s.Unit_sale_price * s.Quantity) AS revenue
FROM go_daily_sales s
JOIN go_products p ON s.Product_number = p.Product_number
WHERE 
    YEAR(s.Date) = COALESCE(%s, YEAR(s.Date))
    AND p.Product_brand = COALESCE(%s, p.Product_brand)
    AND s.Retailer_code = COALESCE(%s, s.Retailer_code)
ORDER BY revenue DESC
LIMIT 5;
        """

        # Esegui la query con i parametri
        cursor.execute(query, (anno, brand, retailer))
        top_sales = cursor.fetchall()

        cursor.close()
        cnx.close()
        return top_sales

    @staticmethod
    def analizeSales(anno,brand,retailer):
        conn=DBConnect.get_connection()
        cursor = conn.cursor()

        # Query SQL con filtri opzionali
        query = """
        SELECT 
            SUM(s.Unit_sale_price * s.Quantity) AS revenue,  
            COUNT(*) AS total_sales,                         
            COUNT(DISTINCT s.Retailer_code) AS num_retailers,  
            COUNT(DISTINCT s.Product_number) AS num_products    
        FROM go_daily_sales s
        JOIN go_products p ON s.Product_number = p.Product_number
        WHERE 
            YEAR(s.Date) = COALESCE(%s, YEAR(s.Date))
            AND p.Product_brand = COALESCE(%s, p.Product_brand)
            AND s.Retailer_code = COALESCE(%s, s.Retailer_code);
        """

        # Esecuzione della query
        cursor.execute(query, (anno, brand, retailer))
        result = cursor.fetchone()

        # Chiudere la connessione
        cursor.close()
        conn.close()
        return result
