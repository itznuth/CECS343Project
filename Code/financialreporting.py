class FinancialReporting:
    """Represents financial reporting for the mall."""

    def __init__(self, total_revenue: float, total_sales: float, sales_date: str):
        self.total_revenue = total_revenue  
        self.total_sales = total_sales      
        self.sales_date = sales_date        

    def get_sales_date(self) -> str:
        return self.sales_date

    def get_revenue(self) -> float:
        return self.total_revenue

    def get_sales(self) -> float:
        return self.total_sales
