class SecurityManagement:
    """Represents security management.

    Attributes:
        location (str): Stores the location of the security.
        incident_log (list): Keeps a record of logged security incidents.

    Methods:
        log_incident(incident_details: str) -> None: Records details of a security incident.
        set_location(location: str) -> None: Assigns a security location.
        get_location() -> str: Retrieves the assigned location.
    """

    def __init__(self, location: str = "Unknown"):
        """Initializes SecurityManagement with a location and an empty incident log."""
        self.location = location
        self.incident_log = []

    def log_incident(self, incident_details: str) -> None:
        """Records details of a security incident."""
        if not incident_details.strip():
            print("Error: Incident details can't be empty.")
            return
        self.incident_log.append(incident_details)
        print("Incident logged successfully.")

    def set_location(self, location: str) -> None:
        """Assigns a security location."""
        if not location.strip():
            print("Error: Location can't be empty.")
            return
        self.location = location
        print(f"Location set to: {location}")

    def get_location(self) -> str:
        """Retrieves the assigned location."""
        return f"Current location: {self.location}"
