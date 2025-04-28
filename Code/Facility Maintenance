class FacilityMaintenance:
    """Represents a facility maintenance request in the mall."""

    def __init__(self, request_id: int, tenant_id: int, maintenance_type: str,
                 request_date: str, status: str = "pending", resolution_date: str = ""):
        self.request_id = request_id
        self.tenant_id = tenant_id
        self.maintenance_type = maintenance_type
        self.request_date = request_date
        self.status = status
        self.resolution_date = resolution_date
        self.assigned_personnel = None

    def assign_personnel(self, worker_name: str) -> str:
        self.assigned_personnel = worker_name
        return f"Maintenance task assigned to {worker_name}"

    def set_request_id(self, request_id: int) -> None:
        self.request_id = request_id

    def get_request_id(self) -> int:
        return self.request_id

    def set_tenant_id(self, tenant_id: int) -> None:
        self.tenant_id = tenant_id

    def get_tenant_id(self) -> int:
        return self.tenant_id

    def set_maintenance_type(self, type: str) -> None:
        self.maintenance_type = type

    def get_maintenance_type(self) -> str:
        return self.maintenance_type

    def set_request_date(self, date: str) -> None:
        self.request_date = date

    def get_request_date(self) -> str:
        return self.request_date

    def set_status(self, status: str) -> None:
        self.status = status

    def get_status(self) -> str:
        return self.status

    def set_resolution_date(self, date: str) -> None:
        self.resolution_date = date

    def get_resolution_date(self) -> str:
        return self.resolution_date

def export_all_requests(requests_lists, filename):
    with open(filename, "w") as file:
        for request in requests_lists:
            file.write(f"Request ID: {request.get_request_id()}\n")
            file.write(f"Tenant ID: {request.get_tenant_id()}\n")
            file.write(f"Maintenance Type: {request.get_maintenance_type()}\n")
            file.write(f"Request Date: {request.get_request_date()}\n")
            file.write(f"Status: {request.get_status()}\n")
            file.write(f"Resolution Date: {request.get_resolution_date()}\n")
            assigned = request.get_assigned_personnel if request.get_assigned_personnel else "None"
            file.write(f"Assigned Personnel: {assigned}\n")
            file.write("-" * 40 + "\n")

