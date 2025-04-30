class Manager:
    """Represents a manager responsible for overseeing mall operations.

    Attributes:
        name (str): The full name of the manager
        employee_id (int): Unique identifier for the manager
        contact_information (str): Contact details (email/phone)
        department (str): Department the manager oversees
        access_level (int): Security access level (1-3)
    """

    def __init__(self, name: str, employee_id: int, contact_information: str, 
                 department: str = "General", access_level: int = 1):
        """Initialize a Manager instance with required details."""
        self.name = name
        self.employee_id = employee_id
        self.contact_information = contact_information
        self.department = department
        self.access_level = access_level

    def get_name(self) -> str:
        """Returns the manager's name."""
        return self.name

    def get_employee_id(self) -> int:
        """Returns the manager's employee ID."""
        return self.employee_id

    def get_contact_information(self) -> str:
        """Returns the manager's contact information."""
        return self.contact_information

    def get_department(self) -> str:
        """Returns the manager's department."""
        return self.department

    def get_access_level(self) -> int:
        """Returns the manager's access level (1-3)."""
        return self.access_level

    def set_name(self, name: str) -> None:
        """Sets the manager's name."""
        if not name.strip():
            raise ValueError("Name cannot be empty")
        self.name = name

    def set_employee_id(self, employee_id: int) -> None:
        """Sets the manager's employee ID with validation."""
        if not isinstance(employee_id, int) or employee_id <= 0:
            raise ValueError("Employee ID must be a positive integer")
        self.employee_id = employee_id

    def set_contact_information(self, contact_info: str) -> None:
        """Sets the manager's contact information."""
        if not contact_info.strip():
            raise ValueError("Contact information cannot be empty")
        self.contact_information = contact_info

    def set_department(self, department: str) -> None:
        """Sets the manager's department."""
        if not department.strip():
            raise ValueError("Department cannot be empty")
        self.department = department

    def set_access_level(self, access_level: int) -> None:
        """Sets the access level with validation (1-3)."""
        if access_level not in (1, 2, 3):
            raise ValueError("Access level must be 1, 2, or 3")
        self.access_level = access_level

    def approve_maintenance(self, request_id: str) -> str:
        """Approves a maintenance request.

        Args:
            request_id: ID of the maintenance request to approve

        Returns:
            Confirmation message
        """
        return f"Maintenance request {request_id} approved by {self.name}"

    def generate_performance_report(self) -> str:
        """Generates a performance report for the manager's department.

        Returns:
            Formatted report string
        """
        return (f"Performance Report for {self.department}\n"
                f"Manager: {self.name}\n"
                f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d')}")

    def __str__(self) -> str:
        """String representation of the Manager."""
        return (f"Manager Information:\n"
                f"Name: {self.name}\n"
                f"Employee ID: {self.employee_id}\n"
                f"Department: {self.department}\n"
                f"Contact: {self.contact_information}\n"
                f"Access Level: {self.access_level}")

    def to_dict(self) -> dict:
        """Converts manager data to dictionary for serialization."""
        return {
            'name': self.name,
            'employee_id': self.employee_id,
            'contact_information': self.contact_information,
            'department': self.department,
            'access_level': self.access_level
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Creates a Manager instance from a dictionary."""
        return cls(
            name=data['name'],
            employee_id=data['employee_id'],
            contact_information=data['contact_information'],
            department=data.get('department', 'General'),
            access_level=data.get('access_level', 1)
        )
