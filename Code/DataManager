from investor import Investor
from manager import Manager
from person import Person
from customer import Customer
from facilitymaintenance import FacilityMaintenance
from financialreporting import FinancialReporting
from store import Store
from rentalpayment import RentalPayment
from tenant import Tenant
from security import Security

class DataManager:
    def __init__(self, stores, investors, customers, managers,
                 maintenance_requests, tenants, rental_payments, financial_reports, security_logs):
        self.stores = stores
        self.investors = investors
        self.customers = customers
        self.managers = managers
        self.maintenance_requests = maintenance_requests
        self.tenants = tenants
        self.rental_payments = rental_payments
        self.financial_reports = financial_reports
        self.security_logs = security_logs


    def add_store(self):
        print("\nAdd New Store")
        try:
            number = int(input("Enter store number: "))
            floor = int(input("Enter floor number: "))
            rent = float(input("Enter monthly rent amount: "))
            self.stores.append(Store(number, floor, rent))
            print(f"Store {number} added successfully!")
        except ValueError:
            print("Invalid input! Please try again.")


    def delete_store(self):
        try:
            number = int(input("Enter store number to delete: "))
            for store in self.stores:
                if store.number == number:
                    self.stores.remove(store)
                    print(f"Store {number} deleted.")
                    return
            print("Store not found.")
        except ValueError:
            print("Invalid input! Please try again.")

    def update_store(self):
        try:
            number = int(input("Enter store number to update: "))
            for store in self.stores:
                if store.number == number:
                    new_number = int(input("Enter new store number: "))
                    new_floor = int(input("Enter new floor: "))
                    new_rent = float(input("Enter new rent: "))
                    store.number = new_number
                    store.floor = new_floor
                    store.rent = new_rent
                    print(f"Store {number} updated to number {new_number}.")
                    return
            print("Store not found.")
        except ValueError:
            print("Invalid input! Please try again.")



    def add_security(self):
        print("\nAdd Security Log")
        location = input("Enter security location: ")
        incident = input("Enter incident details: ")
        security = Security(location)
        security.log_incident(incident)
        self.security_logs.append(security)
        print(f"Security incident at '{location}' logged.")

    def delete_security(self):
        print("\nDelete Security Personnel")
        location = input("Enter location of the security personnel to delete: ")
        for sec in self.security_logs:
            if sec.get_location() == location:
                self.security_logs.remove(sec)
                print(f"Security personnel at '{location}' removed.")
                return

    def add_security_report(self):
        print("\nAdd Security Report")
        location = input("Enter the location of the security to add report to: ")

        for sec in self.security_logs:
            if sec.get_location() == location:
                report = input("Enter detailed report: ")
                sec.add_report(report)
                print("Report added to security entry.")
                return

    def delete_security_report(self):
        print("\nDelete Security Report")
        location = input("Enter the location of the security to delete: ")
        for sec in self.security_logs:
            if sec.get_location() == location:
                if not sec.reports:
                    print("⚠️ No reports to delete.")
                    return
                print("\nCurrent Reports:")
                for idx, report in enumerate(sec.reports, start = 1):
                    print(f"{idx}. {report}")
                try:
                    index = int(input("Enter the report number to delete: ")) - 1
                    if 0 <= index < len(sec.reports):
                        deleted = sec.reports.pop(index)
                        print(f"🗑️ Report deleted: {deleted}")
                    else:
                        print("Invalid report number.")
                except ValueError:
                    print("Invalid input.")
                return


    def add_investor(self):
        print("\nAdd New Investor")
        name = input("Enter investor name: ")
        contact = input("Enter contact information: ")
        self.investors.append(Investor(name, contact))
        print(f"Investor {name} added successfully!")


    def update_investor(self):
        name = input("Enter investor name to update: ")
        for investor in self.investors:
            if investor.name == name:
                new_name = input("Enter new name: ")
                new_contact = input("Enter new contact info: ")
                investor.name = new_name
                investor.contact = new_contact
                print(f"Investor {name} updated to {new_name}.")
                return
        print("Investor not found.")


    def delete_investor(self):
        name = input("Enter investor name to delete: ")
        for investor in self.investors:
            if investor.name == name:
                self.investors.remove(investor)
                print(f"Investor {name} deleted.")
                return
        print("Investor not found.")


    def add_customer(self):
        print("\nAdd New Customer")
        name = input("Enter customer name: ")
        self.customers.append(Customer(name))
        print(f"Customer {name} added successfully!")


    def delete_customer(self):
        name = input("Enter customer name to delete: ")
        for customer in self.customers:
            if customer.name == name:
                self.customers.remove(customer)
                print(f"Customer {name} deleted.")
                return
        print("Customer not found.")


    def update_customer(self):
        name = input("Enter customer name to update: ")
        for customer in self.customers:
            if customer.name == name:
                new_name = input("Enter new name: ")
                customer.name = new_name
                print(f"Customer {name} updated to {new_name}.")
                return
        print("Customer not found.")


    def add_manager(self):
        print("\nAdd New Manager")
        name = input("Enter manager name: ")
        try:
            emp_id = int(input("Enter employee ID: "))
            contact = input("Enter contact information: ")
            self.managers.append(Manager(name, emp_id, contact))
            print(f"Manager {name} added successfully!")
        except ValueError:
            print("Invalid Employee ID.")


    def delete_manager(self):
        try:
            emp_id = int(input("Enter manager employee ID to delete: "))
        except ValueError:
            print("Invalid Employee ID.")
            return
        for manager in self.managers:
            if manager.emp_id == emp_id:
                self.managers.remove(manager)
                print(f"Manager {emp_id} deleted.")
                return
        print("Manager not found.")


    def update_manager(self):
        try:
            emp_id = int(input("Enter manager employee ID to update: "))
        except ValueError:
            print("Invalid Employee ID.")
            return
        for manager in self.managers:
            if manager.emp_id == emp_id:
                new_name = input("Enter new name: ")
                try:
                    new_emp_id = int(input("Enter new employee ID: "))
                except ValueError:
                    print("Invalid new Employee ID.")
                new_contact = input("Enter new contact: ")
                manager.name = new_name
                manager.emp_id = new_emp_id
                manager.contact = new_contact
                print(f"Manager {emp_id} updated to {new_name} with ID {new_emp_id}.")
                return
        print("Manager not found.")


    def create_maintenance_request(self):
        print("\nCreate Maintenance Request")
        try:
            req_id = int(input("Enter request ID: "))
            tenant_id = int(input("Enter tenant ID: "))
            maint_type = input("Enter maintenance type: ")
            date = input("Enter request date (YYYY-MM-DD): ")
            self.maintenance_requests.append(
                FacilityMaintenance(req_id, tenant_id, maint_type, date)
            )
            print(f"Maintenance request {req_id} created successfully!")
        except ValueError:
            print("Invalid request ID.")


    def delete_maintenance_request(self):
        try:
            req_id = int(input("Enter request ID to delete: "))
            for req in self.maintenance_requests:
                if req.req_id == req_id:
                    self.maintenance_requests.remove(req)
                    print(f"Request {req_id} deleted.")
                    return
            print("Request not found.")
        except ValueError:
            print("Invalid request ID.")



    def update_maintenance_request(self):
        try:
            req_id = int(input("Enter request ID to update: "))
            for req in self.maintenance_requests:
                if req.req_id == req_id:
                    new_req_id = int(input("Enter new request ID: "))
                    new_tenant_id = int(input("Enter new tenant ID: "))
                    new_type = input("Enter new maintenance type: ")
                    new_date = input("Enter new date (YYYY-MM-DD): ")
                    req.req_id = new_req_id
                    req.tenant_id = new_tenant_id
                    req.maint_type = new_type
                    req.date = new_date
                    print(f"Request {req_id} updated to {new_req_id}.")
                    return
            print("Maintenance request not found.")
        except ValueError:
            print("Invalid request ID.")


    def generate_financial_report(self):
        print("\nGenerate Financial Report")
        try:
            revenue = float(input("Enter total revenue: "))
            sales = float(input("Enter total sales: "))
            date = input("Enter report date (YYYY-MM-DD): ")
            report = FinancialReporting(revenue, sales, date)
            self.financial_reports.append(report)
            print(f"Financial report generated successfully!")
            return
        except ValueError:
            print("Invalid input.")


    def delete_financial_report(self):
        date = input("Enter the date of the report to delete (YYYY-MM-DD): ")
        for report in self.financial_reports:
            if report.date == date:
                self.financial_reports.remove(report)
                print(f"Financial report on {date} deleted.")
                return
        print(f"No financial report found for {date}.")


    def update_financial_report(self):
        date = input("Enter the date of the report to update (YYYY-MM-DD): ")
        for report in self.financial_reports:
            if report.date == date:
                try:
                    new_revenue = float(input("Enter new total revenue: "))
                    new_sales = float(input("Enter new total sales: "))
                    new_date = input("Enter new report date (YYYY-MM-DD): ")
                    report.revenue = new_revenue
                    report.sales = new_sales
                    report.date = new_date
                    print(f"Financial report on {date} updated to new date {new_date}.")
                except ValueError:
                    print("Invalid input.")
                return
        print(f"No financial report found for {date}.")


    def add_tenant(self):
        print("\nAdd New Tenant")
        try:
            name = input("Enter tenant name: ")
            space_num = int(input("Enter store number: "))
            start_date = input("Enter lease start date (YYYY-MM-DD): ")
            end_date = input("Enter lease end date (YYYY-MM-DD): ")
            contact = input("Enter contact information: ")
            self.tenants.append(Tenant(name, space_num, start_date, end_date, contact))
            print(f"Tenant {name} added successfully!")
        except ValueError:
            print("Invalid input.")


    def delete_tenant(self):
        name = input("Enter tenant name to delete: ")
        for tenant in self.tenants:
            if tenant.name == name:
                self.tenants.remove(tenant)
                print(f"Tenant {name} deleted.")
                return
        print("Tenant not found.")


    def update_tenant(self):
        name = input("Enter tenant name to update: ")
        for tenant in self.tenants:
            if tenant.name == name:
                try:
                    new_name = input("Enter new name: ")
                    new_space = int(input("Enter new store number: "))
                    new_start = input("Enter new lease start date (YYYY-MM-DD): ")
                    new_end = input("Enter new lease end date (YYYY-MM-DD): ")
                    new_contact = input("Enter new contact: ")
                    tenant.name = new_name
                    tenant.space_num = new_space
                    tenant.start_date = new_start
                    tenant.end_date = new_end
                    tenant.contact = new_contact
                    print(f"Tenant {name} updated to {new_name}.")
                except ValueError:
                    print("Invalid input.")
                return
        print("Tenant not found.")


    def record_rental_payment(self):
        try:
            print("\nRecord Rental Payment")
            amount = float(input("Enter payment amount: "))
            date = input("Enter payment date (YYYY-MM-DD): ")
            unit = int(input("Enter rental unit number: "))
            status = input("Enter payment status (completed/pending/overdue): ")
            self.rental_payments.append(RentalPayment(amount, date, unit, status))
            print(f"Payment of ${amount:,.2f} for unit {unit} recorded successfully!")
        except ValueError:
            print("Invalid input.")


    def delete_rental_payment(self):
        try:
            unit = int(input("Enter unit number to delete payment for: "))
            for payment in self.rental_payments:
                if payment.unit == unit:
                    self.rental_payments.remove(payment)
                    print(f"Payment for unit {unit} deleted.")
                    return
            print("Payment not found.")
        except ValueError:
            print("Invalid input.")


    def update_rental_payment(self):
        try:
            unit = int(input("Enter rental unit number to update: "))
            for payment in self.rental_payments:
                if payment.unit == unit:
                    new_unit = int(input("Enter new rental unit number: "))
                    new_amount = float(input("Enter new amount: "))
                    new_date = input("Enter new date (YYYY-MM-DD): ")
                    new_status = input("Enter new status (completed/pending/overdue): ")
                    payment.unit = new_unit
                    payment.amount = new_amount
                    payment.date = new_date
                    payment.status = new_status
                    print(f"Payment for unit {unit} updated to unit {new_unit}.")
                    return
            print("Rental payment not found.")
        except ValueError:
            print("Invalid input.")
