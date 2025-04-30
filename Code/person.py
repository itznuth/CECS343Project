class Person:
    """Base class representing a person with basic contact information.

    Attributes:
        name (str): The person's name.
        contact_information (str): Contact details.
    """

    def __init__(self, name: str = "", contact_information: str = ""):
        self.name = name
        self.contact_information = contact_information

    def set_name(self, name: str) -> None:
        if not name.strip():
            raise ValueError("Name cannot be empty")
        self.name = name

    def set_contact_information(self, contact: str) -> None:
        if not contact.strip():
            raise ValueError("Contact information cannot be empty")
        self.contact_information = contact

    def __str__(self):
        return f"{self.name} | Contact: {self.contact_information}"
