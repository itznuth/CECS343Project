class Tenant:
    """Represents a tenant in the mall management system.

    Args:
        name (str): The name of the tenant
        space_number (int): The store number occupied by the tenant
        lease_start_date (str): Start date of lease (YYYY-MM-DD)
        lease_end_date (str): End date of lease (YYYY-MM-DD)
        contact_information (str): Contact details for the tenant
    """

    def __init__(self, name: str, space_number: int, lease_start_date: str,
                 lease_end_date: str, contact_information: str):
        self.name = name
        self.space_number = space_number
        self.lease_start_date = lease_start_date
        self.lease_end_date = lease_end_date
        self.contact_information = contact_information

    def __str__(self):
        return (f"Tenant: {self.name}\n"
                f"Store: {self.space_number}\n"
                f"Lease: {self.lease_start_date} to {self.lease_end_date}\n"
                f"Contact: {self.contact_information}")

    def set_name(self, name: str) -> None:
        """Sets the name of the tenant."""
        self.name = name

    def set_store_number(self, store_number: int) -> None:
        """Assigns the store number of the tenant."""
        self.space_number = store_number

    def set_lease_start_date(self, lease_start_date: str) -> None:
        """Sets the start date of the tenant's lease."""
        self.lease_start_date = lease_start_date

    def set_lease_end_date(self, lease_end_date: str) -> None:
        """Sets the end date of the tenant's lease."""
        self.lease_end_date = lease_end_date

    def set_contact_information(self, contact_information: str) -> None:
        """Sets the tenant's contact information."""
        self.contact_information = contact_information

    def get_lease_start_date(self) -> str:
        """Retrieves the lease start date."""
        return self.lease_start_date

    def get_lease_end_date(self) -> str:
        """Retrieves the lease end date."""
        return self.lease_end_date

    def get_contact_information(self) -> str:
        """Returns the contact information of the tenant."""
        return self.contact_information

    def get_name(self) -> str:
        """Returns the name of the tenant."""
        return self.name

    def get_store_number(self) -> int:
        """Returns the store number of the tenant."""
        return self.space_number
