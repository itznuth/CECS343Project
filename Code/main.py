import datetime
from investor import Investor
from manager import Manager
from person import Person
from customer import Customer
from facilitymaintenance import FacilityMaintenance
from financialreporting import FinancialReporting
from security import Security
from securitymanagement import SecurityManagement
from store import Store
from rentalpayment import RentalPayment
from tenant import Tenant
from visitortracking import VisitorTracking
from rentalpayment import (
    RentalPayment,
    search_by_unit,
    filter_by_status,
    filter_by_date_range,
    update_rental_payment,
    delete_rental_payment
)

# In-memory storage
payments = []
maintenance_requests = []

# Simulated user credentials
users = {
    "admin1": {"password": "adminpass", "role": "admin"},
    "tenant1": {"password": "tenantpass", "role": "tenant"},
    "manager1": {"password": "managerpass", "role": "manager"},
}


class MallManagementSystem:
    def __init__(self):
        self.stores = []
        self.investors = []
        self.customers = []
        self.managers = []
        self.maintenance_requests = []
        self.security_logs = []
        self.tenants = []
        self.rental_payments = []
        self.visitor_tracking = VisitorTracking()

    def add_store(self):
        number = int(input("Enter store number: "))
        floor = int(input("Enter floor number: "))
        rent = float(input("Enter monthly rent amount: "))
        self.stores.append(Store(number, floor, rent))
        print(f"Store {number} added.")

    def add_investor(self):
        name = input("Investor name: ")
        contact = input("Contact info: ")
        self.investors.append(Investor(name, contact))
        print(f"Investor {name} added.")

    def add_customer(self):
        name = input("Customer name: ")
        self.customers.append(Customer(name))
        print(f"Customer {name} added.")

    def add_manager(self):
        name = input("Manager name: ")
        emp_id = int(input("Employee ID: "))
        contact = input("Contact info: ")
        self.managers.append(Manager(name, emp_id, contact))
        print(f"Manager {name} added.")

    def create_maintenance_request(self):
        req_id = int(input("Request ID: "))
        tenant_id = int(input("Tenant ID: "))
        maint_type = input("Maintenance type: ")
        date = input("Request date (YYYY-MM-DD): ")
        self.maintenance_requests.append(FacilityMaintenance(req_id, tenant_id, maint_type, date))
        print(f"Maintenance request {req_id} created.")

    def log_security_incident(self):
        location = input("Incident location: ")
        details = input("Incident details: ")
        security = SecurityManagement(location)
        security.log_incident(details)
        self.security_logs.append(security)
        print("Incident logged.")

    def generate_financial_report(self):
        revenue = float(input("Total revenue: "))
        sales = float(input("Total sales: "))
        date = input("Report date (YYYY-MM-DD): ")
        report = FinancialReporting(revenue, sales, date)
        print(f"\nFinancial Report - {date}")
        print(f"Revenue: ${report.get_revenue():,.2f}")
        print(f"Sales: ${report.get_sales():,.2f}")

    def add_tenant(self):
        name = input("Tenant name: ")
        space_num = int(input("Store number: "))
        start_date = input("Lease start (YYYY-MM-DD): ")
        end_date = input("Lease end (YYYY-MM-DD): ")
        contact = input("Contact info: ")
        self.tenants.append(Tenant(name, space_num, start_date, end_date, contact))
        print(f"Tenant {name} added.")

    def record_rental_payment(self):
        amount = float(input("Payment amount: "))
        date = input("Payment date (YYYY-MM-DD): ")
        unit = int(input("Rental unit #: "))
        status = input("Status (completed/pending/overdue): ")
        self.rental_payments.append(RentalPayment(amount, date, unit, status))
        print(f"Payment for unit {unit} recorded.")

    def track_visitor(self):
        action = input("(I)ncrement or (D)ecrement visitor count? ").upper()
        if action == "I":
            time = input("Entry time (HH:MM): ")
            self.visitor_tracking.increment_visitor_count(time)
            print("Visitor incremented.")
        elif action == "D":
            self.visitor_tracking.decrement_visitor_count()
            print("Visitor decremented.")
        else:
            print("Invalid input.")
        print(f"Total visitors: {self.visitor_tracking.get_total_visitors()}")

    def export_stores_to_file(self, filename: str = "stores_report.txt") -> None:
        try:
            with open(filename, 'w') as file:
                file.write("=== MALL STORES REPORT ===\n")
                file.write(f"Generated: {datetime.datetime.now()}\n")
                file.write(f"Total Stores: {len(self.stores)}\n\n")
                for store in self.stores:
                    file.write(store.get_store_info())
                total_rent = sum(store.get_rent_amount() for store in self.stores)
                file.write(f"\nTOTAL RENT: ${total_rent:,.2f}\n")
            print(f"Report saved to {filename}")
        except Exception as e:
            print(f"Error: {e}")


def login():
    username = input("Username: ")
    password = input("Password: ")
    user = users.get(username)
    if user and user["password"] == password:
        print(f"Login successful ({user['role']})")
        return user["role"]
    else:
        print("Invalid login.")
        return None


def tenant_menu():
    while True:
        print("\nTenant Menu")
        print("1. Add Rental Payment")
        print("2. Search Payment by Unit")
        print("3. Update Payment")
        print("4. Delete Payment")
        print("5. Exit")
        choice = input("Choose: ")
        if choice == "1":
            try:
                amount = float(input("Amount: "))
                date = input("Date (YYYY-MM-DD): ")
                unit = int(input("Unit #: "))
                status = input("Status: ")
                payments.append(RentalPayment(amount, date, unit, status))
                print("Payment added.")
            except:
                print("Invalid input.")
        elif choice == "2":
            unit = int(input("Enter unit #: "))
            results = search_by_unit(payments, unit)
            print("Results:", results)
        elif choice == "3":
            unit = int(input("Unit to update: "))
            new_status = input("New status: ")
            if update_rental_payment(payments, unit, new_status=new_status):
                print("Updated.")
            else:
                print("Not found.")
        elif choice == "4":
            unit = int(input("Unit to delete: "))
            if delete_rental_payment(payments, unit):
                print("Deleted.")
            else:
                print("Not found.")
        elif choice == "5":
            break
        else:
            print("Invalid option.")


def manager_menu():
    print("\nManager Menu")
    print("1. View Maintenance")
    print("2. Export Logs")
    print("3. Exit")
    # Add manager functionalities here


def admin_menu():
    system = MallManagementSystem()
    while True:
        print("\nAdmin Menu")
        print("1. Manage Stores")
        print("2. Manage Investors")
        print("3. Manage Customers")
        print("4. Manage Managers")
        print("5. Maintenance Requests")
        print("6. Security Incidents")
        print("7. Financial Reports")
        print("8. Manage Tenants")
        print("9. Rental Payments")
        print("10. Visitor Tracking")
        print("11. Export Stores Report")
        print("12. Exit")
        choice = input("Choose: ")
        if choice == "1":
            system.add_store()
        elif choice == "2":
            system.add_investor()
        elif choice == "3":
            system.add_customer()
        elif choice == "4":
            system.add_manager()
        elif choice == "5":
            system.create_maintenance_request()
        elif choice == "6":
            system.log_security_incident()
        elif choice == "7":
            system.generate_financial_report()
        elif choice == "8":
            system.add_tenant()
        elif choice == "9":
            system.record_rental_payment()
        elif choice == "10":
            system.track_visitor()
        elif choice == "11":
            filename = input("Enter filename (press Enter for default): ")
            if not filename:
                filename = "stores_report.txt"
            system.export_stores_to_file(filename)
        elif choice == "12":
            break
        else:
            print("Invalid option.")


def run_interface(role):
    if role == "tenant":
        tenant_menu()
    elif role == "manager":
        manager_menu()
    elif role == "admin":
        admin_menu()
    else:
        print("Access denied.")


if __name__ == "__main__":
    role = login()
    if role:
        run_interface(role)
