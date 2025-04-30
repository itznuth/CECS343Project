class Store:
    """Represents a store unit in the mall.

    Attributes:
        number (int): The unique identifier or number of the store.
        floor (int): The floor on which the store is located.
        rent_amount (float): The monthly rent amount for the store.
    """

    def __init__(self, number: int, floor: int, rent_amount: float, tenant: str = "Vacant"):
        self.number = number
        self.floor = floor
        self.rent_amount = rent_amount 
        self.tenant = tenant

    def set_number(self, number: int) -> None:
        """Sets the number of the store."""
        self.number = number

    def set_floor(self, floor: int) -> None:
        """Sets the floor of the store."""
        self.floor = floor

    def set_rent_amount(self, rent_amount: float) -> None:
        """Sets the monthly rent amount of the store."""
        self.rent_amount = rent_amount

    def get_rent_amount(self) -> float:
        """Retrieves the monthly rent amount."""
        return self.rent_amount

    def get_floor(self) -> int:
        """Retrieves the floor on which the store is located."""
        return self.floor

    def get_number(self) -> int:
        """Retrieves the store number."""
        return self.number

    def get_store_info(self) -> str:
        """Returns formatted store information as a string."""
        return (f"Store #{self.number} (Floor {self.floor})\n"
                f"Tenant: {self.tenant}\n"
                f"Monthly Rent: ${self.rent_amount:,.2f}\n"
                f"{'-'*30}\n")
