class Security:
    """Represents security management.

    Attributes:
        location (str): Stores the location of security personnel or system.
        incident_log (list): Keeps a record of logged security incidents.

    Methods:
        log_incident(incident_details: str) -> None: Records details of a security incident.
        set_location(location: str) -> None: Assigns a security location.
        get_location() -> str: Retrieves the assigned location.
    """

    def __init__(self, location: str = "Unknown"):
        """Initializes Security with a location and an empty incident log."""
        self.location = location
        self.incident_log = []
        self.reports = []

    def log_incident(self, incident_details: str) -> None:
        """Records details of a security incident."""
        if not incident_details.strip():
            print("Error: Incident details can't be empty.")
            return
        self.incident_log.append(incident_details)
        print("Incident logged successfully.")

    def add_report(self, report: str) -> None:
        """Adds a detailed report to the reports list."""
        if not report.strip():
            print("Error: Report content can't be empty.")
            return
        self.reports.append(report)
        print("Report added successfully.")

    def delete_report(self, index: int) -> bool:
        """Deletes a report by index. Returns True if successful, False otherwise."""
        if index < 0 or index >= len(self.reports):
            print(f"Error: No report found at index {index}.")
            return False
        del self.reports[index]
        print(f"Report at index {index} deleted successfully.")
        return True


    def set_location(self, location: str) -> None:
        """Assigns a security location."""
        self.location = location

    def get_location(self) -> str:
        """Retrieves the assigned location."""
        return self.location

    def __repr__(self):
        return f"Security(location='{self.location}')"

    def export_incidents(self, filename: str) -> None:
        try:
            with open(filename, 'w') as file:
                for i, incident in enumerate(self.incident_log, start=1):
                    file.write(f"Incident {i}: {incident}\n")
            print(f"Incidents successfully exported to '{filename}'.")
    except Exception as e:
            print(f"Error exporting incidents: {e}")

