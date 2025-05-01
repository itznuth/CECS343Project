class Security:
    """Represents security management with incident tracking and reporting.

    Attributes:
        location (str): The location of security personnel or system.
        incident_log (list): Record of security incidents.
        reports (list): Detailed security reports.
    """

    def __init__(self, location: str = "Unknown"):
        self.location = location
        self.incident_log = []
        self.reports = []

    def log_incident(self, incident_details: str) -> None:
        """Records a security incident."""
        if not incident_details.strip():
            print("Error: Incident details cannot be empty")
            return False  
        self.incident_log.append(incident_details)
        return True  

    def add_report(self, report: str) -> None:
        """Adds a detailed security report."""
        if not report.strip():
            raise ValueError("Report content cannot be empty")
        self.reports.append(report)

    def delete_report(self, index: int) -> None:
        """Deletes a report by index."""
        if index < 0 or index >= len(self.reports):
            raise IndexError("Invalid report index")
        del self.reports[index]

    def set_location(self, location: str) -> None:
        """Sets the security location."""
        if not location.strip():
            raise ValueError("Location cannot be empty")
        self.location = location

    def get_location(self) -> str:
        """Returns the current location."""
        return self.location

    def export_incidents(self, filename: str) -> None:
        """Exports all security incidents to a file."""
        try:
            with open(filename, 'w') as file: 
                file.write(f"=== Security Incidents at {self.location} ===\n")
                file.write(f"Report Generated: {datetime.datetime.now()}\n")
                file.write("=" * 40 + "\n")
                for i, incident in enumerate(self.incident_log, 1):
                    file.write(f"{i}. {incident}\n")
                file.write("=" * 40 + "\n")
                file.write(f"Total Incidents: {len(self.incident_log)}\n")
            print(f"All incidents exported to '{filename}'")
        except Exception as e:
            print(f"Error exporting incidents: {e}")

    def __str__(self):
        return (f"Security Location: {self.location}\n"
                f"Total Incidents: {len(self.incident_log)}\n"
                f"Total Reports: {len(self.reports)}")
