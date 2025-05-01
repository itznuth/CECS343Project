from investor import Investor
from manager import Manager
from facilitymaintenance import FacilityMaintenance
from financialreporting import FinancialReporting
from store import Store
from rentalpayment import RentalPayment
from tenant import Tenant
from security import Security
import datetime

class DataManager:
    def __init__(self, stores, investors, managers, maintenance_requests,
                 tenants, rental_payments, financial_reports, security_logs):
        self.stores = stores
        self.investors = investors
        self.managers = managers
        self.maintenance_requests = maintenance_requests
        self.tenants = tenants
        self.rental_payments = rental_payments
        self.financial_reports = financial_reports
        self.security_logs = security_logs

    # Store Management
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

    def update_store(self):
        try:
            number = int(input("Enter store number to update: "))
            for store in self.stores:
                if store.number == number:
                    print(f"\nCurrent Store Details:")
                    print(f"Number: {store.number}")
                    print(f"Floor: {store.floor}")
                    print(f"Rent: {store.rent_amount}")

                    new_number = input("\nEnter new store number (press Enter to keep current): ")
                    new_floor = input("Enter new floor (press Enter to keep current): ")
                    new_rent = input("Enter new rent amount (press Enter to keep current): ")

                    store.number = int(new_number) if new_number else store.number
                    store.floor = int(new_floor) if new_floor else store.floor
                    store.rent_amount = float(new_rent) if new_rent else store.rent_amount

                    print(f"\nStore updated successfully!")
                    return
            print("Store not found.")
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

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

    def view_stores(self):
        if not self.stores:
            print("No stores available.")
            return
        for store in self.stores:
            print(store.get_store_info())

    # Investor Management
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
                print(f"\nCurrent Investor Details:")
                print(f"Name: {investor.name}")
                print(f"Contact: {investor.contact_information}")

                new_name = input("\nEnter new name (press Enter to keep current): ")
                new_contact = input("Enter new contact info (press Enter to keep current): ")

                investor.name = new_name if new_name else investor.name
                investor.contact_information = new_contact if new_contact else investor.contact_information

                print(f"\nInvestor updated successfully!")
                print(f"New Name: {investor.name}")
                print(f"New Contact: {investor.contact_information}")
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

    def view_investors(self):
        if not self.investors:
            print("No investors available.")
            return
        for investor in self.investors:
            print(f"Name: {investor.name}")
            print(f"Contact: {investor.contact_information}\n")

    # Manager Management
    def add_manager(self):
        print("\nAdd New Manager")
        name = input("Enter manager name: ")
        try:
            emp_id = int(input("Enter employee ID: "))
            contact = input("Enter contact information: ")
            department = input("Enter department: ")
            self.managers.append(Manager(name, emp_id, contact, department))
            print(f"Manager {name} added successfully!")
        except ValueError:
            print("Invalid Employee ID.")

    def update_manager(self):
        try:
            emp_id = int(input("Enter manager employee ID to update: "))
            for manager in self.managers:
                if manager.employee_id == emp_id:
                    print(f"\nCurrent Manager Details:")
                    print(f"Name: {manager.name}")
                    print(f"ID: {manager.employee_id}")
                    print(f"Contact: {manager.contact_information}")
                    print(f"Department: {manager.department}")

                    new_name = input("\nEnter new name (press Enter to keep current): ")
                    new_emp_id = input("Enter new employee ID (press Enter to keep current): ")
                    new_contact = input("Enter new contact (press Enter to keep current): ")
                    new_dept = input("Enter new department (press Enter to keep current): ")

                    manager.name = new_name if new_name else manager.name
                    manager.employee_id = int(new_emp_id) if new_emp_id else manager.employee_id
                    manager.contact_information = new_contact if new_contact else manager.contact_information
                    manager.department = new_dept if new_dept else manager.department

                    print(f"\nManager updated successfully!")
                    return
            print("Manager not found.")
        except ValueError:
            print("Invalid Employee ID.")

    def delete_manager(self):
        try:
            emp_id = int(input("Enter manager employee ID to delete: "))
            for manager in self.managers:
                if manager.employee_id == emp_id:
                    self.managers.remove(manager)
                    print(f"Manager {emp_id} deleted.")
                    return
            print("Manager not found.")
        except ValueError:
            print("Invalid Employee ID.")

    def view_managers(self):
        if not self.managers:
            print("No managers available.")
            return
        for manager in self.managers:
            print(f"Name: {manager.name}")
            print(f"ID: {manager.employee_id}")
            print(f"Department: {manager.department}")
            print(f"Contact: {manager.contact_information}\n")

    # Maintenance Management
    def create_maintenance_request(self):
        print("\nCreate Maintenance Request")
        try:
            req_id = int(input("Enter request ID: "))
            tenant_id = int(input("Enter tenant ID: "))
            maint_type = input("Enter maintenance type: ")
            date = input("Enter request date (YYYY-MM-DD): ")
            self.maintenance_requests.append(
                FacilityMaintenance(
                    request_id=req_id,
                    tenant_id=tenant_id,
                    maintenance_type=maint_type,
                    request_date=date
                )
            )
            print(f"Maintenance request {req_id} created successfully!")
        except ValueError:
            print("Invalid request ID.")

    def update_maintenance_request(self):
        try:
            req_id = int(input("Enter request ID to update: "))
            for req in self.maintenance_requests:
                if req.request_id == req_id:
                    print(f"\nCurrent Request Details:")
                    print(f"ID: {req.request_id}")
                    print(f"Tenant ID: {req.tenant_id}")
                    print(f"Type: {req.maintenance_type}")
                    print(f"Date: {req.request_date}")

                    new_req_id = input("\nEnter new request ID (press Enter to keep current): ")
                    new_tenant_id = input("Enter new tenant ID (press Enter to keep current): ")
                    new_type = input("Enter new maintenance type (press Enter to keep current): ")
                    new_date = input("Enter new date (YYYY-MM-DD, press Enter to keep current): ")

                    req.request_id = int(new_req_id) if new_req_id else req.request_id
                    req.tenant_id = int(new_tenant_id) if new_tenant_id else req.tenant_id
                    req.maintenance_type = new_type if new_type else req.maintenance_type
                    req.request_date = new_date if new_date else req.request_date

                    print(f"\nRequest updated successfully!")
                    return
            print("Maintenance request not found.")
        except ValueError:
            print("Invalid request ID.")

    def delete_maintenance_request(self):
        try:
            req_id = int(input("Enter request ID to delete: "))
            for req in self.maintenance_requests:
                if req.request_id == req_id: 
                    self.maintenance_requests.remove(req)
                    print(f"Request {req_id} deleted.")
                    return
            print("Request not found.")
        except ValueError:
            print("Invalid request ID.")

    def view_maintenance_requests(self):
        if not self.maintenance_requests:
            print("No maintenance requests available.")
            return
        for req in self.maintenance_requests:
            print(f"Request ID: {req.request_id}")
            print(f"Tenant ID: {req.tenant_id}")
            print(f"Type: {req.maintenance_type}")
            print(f"Date: {req.request_date}")
            print(f"Status: {req.status}\n")

    # Tenant Management
    def add_tenant(self):
        print("\nAdd New Tenant")
        try:
            name = input("Enter tenant name: ")
            space_number = int(input("Enter store number: "))

            # Check if store exists and is vacant
            store = next((s for s in self.stores if s.number == space_number), None)
            if not store:
                print(f"Error: Store #{space_number} does not exist!")
                return
            if store.tenant != "Vacant":
                print(f"Error: Store #{space_number} is already occupied by {store.tenant}!")
                return

            start_date = input("Enter lease start date (YYYY-MM-DD): ")
            end_date = input("Enter lease end date (YYYY-MM-DD): ")
            contact = input("Enter contact information: ")

            self.tenants.append(Tenant(
                name=name,
                space_number=space_number,
                lease_start_date=start_date,
                lease_end_date=end_date,
                contact_information=contact
            ))

            # Update store tenant status
            store.set_tenant(name)
            print(f"Tenant {name} added successfully to Store #{space_number}!")
        except ValueError:
            print("Invalid input.")

    def update_tenant(self):
        name = input("Enter tenant name to update: ")
        for tenant in self.tenants:
            if tenant.name == name:
                print(f"\nCurrent Tenant Details:")
                print(f"Name: {tenant.name}")
                print(f"Store: {tenant.space_number}")
                print(f"Lease Start: {tenant.lease_start_date}")
                print(f"Lease End: {tenant.lease_end_date}")
                print(f"Contact: {tenant.contact_information}")

                try:
                    new_name = input("\nEnter new name (press Enter to keep current): ")
                    new_space = input("Enter new store number (press Enter to keep current): ")
                    new_start = input("Enter new lease start date (YYYY-MM-DD, press Enter to keep current): ")
                    new_end = input("Enter new lease end date (YYYY-MM-DD, press Enter to keep current): ")
                    new_contact = input("Enter new contact (press Enter to keep current): ")

                    old_store_number = tenant.space_number

                    # Find current store
                    old_store = next((s for s in self.stores if s.number == old_store_number), None)

                    if new_space:  # If changing stores
                        new_space_number = int(new_space)
                        new_store = next((s for s in self.stores if s.number == new_space_number), None)

                        if not new_store:
                            print(f"Error: Store #{new_space_number} doesn't exist!")
                            return
                        if new_store.tenant != "Vacant":
                            print(f"Error: Store #{new_space_number} is already occupied by {new_store.tenant}!")
                            return

                        # Update tenant's store number
                        tenant.space_number = new_space_number

                        # Update store tenant statuses
                        if old_store:
                            old_store.set_tenant("Vacant")
                        new_store.set_tenant(new_name if new_name else tenant.name)

                    # Update other fields
                    if new_name:
                        tenant.name = new_name
                        # Update store tenant name if not changing stores
                        if not new_space and old_store:
                            old_store.set_tenant(new_name)
                    if new_start:
                        tenant.lease_start_date = new_start
                    if new_end:
                        tenant.lease_end_date = new_end
                    if new_contact:
                        tenant.contact_information = new_contact

                    print(f"\nTenant updated successfully!")
                except ValueError:
                    print("Invalid input.")
                return
        print("Tenant not found.")

    def delete_tenant(self):
        """Deletes a tenant from the system by name."""
        if not self.tenants:
            print("No tenants available to delete.")
            return

        print("\nCurrent Tenants:")
        for i, tenant in enumerate(self.tenants, 1):
            print(f"{i}. {tenant.name} (Store: {tenant.space_number})")

        try:
            choice = int(input("\nEnter the number of the tenant to delete: "))
            if 1 <= choice <= len(self.tenants):
                deleted_tenant = self.tenants.pop(choice - 1)
                # Mark store as vacant
                for store in self.stores:
                    if store.number == deleted_tenant.space_number:
                        store.set_tenant("Vacant")
                print(f"\nTenant '{deleted_tenant.name}' deleted successfully!")
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def view_tenants(self):
        if not self.tenants:
            print("No tenants available.")
            return
        for tenant in self.tenants:
            print(f"Name: {tenant.name}")
            print(f"Store: {tenant.space_number}")  
            print(f"Lease: {tenant.lease_start_date} to {tenant.lease_end_date}")
            print(f"Contact: {tenant.contact_information}\n")

    # Rental Payment Management
    def record_rental_payment(self):
        try:
            print("\nRecord Rental Payment")
            amount = float(input("Enter payment amount: "))
            date = input("Enter payment date (YYYY-MM-DD): ")
            unit = int(input("Enter rental unit number: "))
            status = input("Enter payment status (completed/pending/overdue): ")
            self.rental_payments.append(RentalPayment(amount, date, unit, status))
            print(f"Payment of ${amount:,.2f} for unit {unit} recorded successfully!")
        except ValueError as e:
            print(f"Invalid input: {e}")

    def update_rental_payment(self):
        try:
            unit = int(input("Enter rental unit number to update: "))
            for payment in self.rental_payments:
                if payment.unit == unit:
                    print(f"\nCurrent Payment Details:")
                    print(f"Unit: {payment.unit}")
                    print(f"Amount: ${payment.amount:,.2f}")
                    print(f"Date: {payment.date}")
                    print(f"Status: {payment.status}")

                    new_unit = input("\nEnter new rental unit number (press Enter to keep current): ")
                    new_amount = input("Enter new amount (press Enter to keep current): ")
                    new_date = input("Enter new date (YYYY-MM-DD, press Enter to keep current): ")
                    new_status = input("Enter new status (completed/pending/overdue, press Enter to keep current): ")

                    payment.unit = int(new_unit) if new_unit else payment.unit
                    payment.amount = float(new_amount) if new_amount else payment.amount
                    payment.date = new_date if new_date else payment.date
                    payment.status = new_status if new_status else payment.status

                    print(f"\nPayment updated successfully!")
                    return
            print("Rental payment not found.")
        except ValueError as e:
            print(f"Invalid input: {e}")

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

    def view_rental_payments(self):
        if not self.rental_payments:
            print("No rental payments available.")
            return
        for payment in self.rental_payments:
            print(f"Unit: {payment.unit}")
            print(f"Amount: ${payment.amount:,.2f}")
            print(f"Date: {payment.date}")
            print(f"Status: {payment.status}\n")

    # Financial Reporting
    def generate_financial_report(self):
        print("\nGenerate Financial Report")
        try:
            revenue = float(input("Enter total revenue: "))
            sales = float(input("Enter total sales: "))
            date = input("Enter report date (YYYY-MM-DD): ")
            report = FinancialReporting(total_revenue=revenue, total_sales=sales, sales_date=date)
            self.financial_reports.append(report)
            print(f"Financial report generated successfully!")
        except ValueError:
            print("Invalid input.")

    def update_financial_report(self):
        date = input("Enter the date of the report to update (YYYY-MM-DD): ")
        for report in self.financial_reports:
            if report.sales_date == date:
                try:
                    print(f"\nCurrent Report Details:")
                    print(f"Date: {report.sales_date}")
                    print(f"Revenue: ${report.total_revenue:,.2f}")  
                    print(f"Sales: ${report.total_sales:,.2f}")     

                    new_revenue = input("\nEnter new total revenue (press Enter to keep current): ")
                    new_sales = input("Enter new total sales (press Enter to keep current): ")
                    new_date = input("Enter new report date (YYYY-MM-DD, press Enter to keep current): ")

                    report.total_revenue = float(new_revenue) if new_revenue else report.total_revenue
                    report.total_sales = float(new_sales) if new_sales else report.total_sales
                    report.sales_date = new_date if new_date else report.sales_date

                    print(f"\nFinancial report updated successfully!")
                except ValueError:
                    print("Invalid input.")
                return
        print(f"No financial report found for {date}.")

    def delete_financial_report(self):
        date = input("Enter the date of the report to delete (YYYY-MM-DD): ")
        for report in self.financial_reports:
            if report.sales_date == date:
                self.financial_reports.remove(report)
                print(f"Financial report on {date} deleted.")
                return
        print(f"No financial report found for {date}.")

    def view_financial_reports(self):
        if not self.financial_reports:
            print("No financial reports available.")
            return
        for report in self.financial_reports:
            print(f"Date: {report.sales_date}")
            print(f"Revenue: ${report.total_revenue:,.2f}")  
            print(f"Sales: ${report.total_sales:,.2f}\n")    

    # Security Incident Management
    def export_security_incidents(self, filename: str) -> None:
        """Exports all security incidents from all locations to a file"""
        try:
            with open(filename, 'w') as file:
                file.write("=== SECURITY INCIDENTS REPORT ===\n")
                file.write(f"Generated: {datetime.datetime.now()}\n")
                file.write("=" * 50 + "\n\n")

                for security in self.security_logs:
                    file.write(f"Location: {security.get_location()}\n")
                    file.write(f"Total Incidents: {len(security.incident_log)}\n")
                    for i, incident in enumerate(security.incident_log, 1):
                        file.write(f"  {i}. {incident}\n")
                    file.write("\n")

                total_incidents = sum(len(s.incident_log) for s in self.security_logs)
                file.write("=" * 50 + "\n")
                file.write(f"TOTAL INCIDENTS ACROSS ALL LOCATIONS: {total_incidents}\n")

            print(f"Security incidents report saved to {filename}")
        except Exception as e:
            print(f"Error exporting security incidents: {e}")
            
    # Security Management
    def add_security(self):
        print("\nAdd Security Log")
        location = input("Enter security location: ")
        incident = input("Enter incident details: ")
        security = Security(location)
        security.log_incident(incident)
        self.security_logs.append(security)
        print(f"Security incident at '{location}' logged.")

    def add_security_report(self):
        print("\nAdd Security Report")
        location = input("Enter the location of the security to add report to: ")
        for sec in self.security_logs:
            if sec.get_location() == location:
                report = input("Enter detailed report: ")
                sec.add_report(report)
                print("Report added to security entry.")
                return
        print(f"No security found at {location}")

    def delete_security_report(self):
        print("\nDelete Security Report")
        location = input("Enter the location of the security to delete: ")
        for sec in self.security_logs:
            if sec.get_location() == location:
                if not sec.reports:
                    print("No reports to delete.")
                    return
                print("\nCurrent Reports:")
                for idx, report in enumerate(sec.reports, start=1):
                    print(f"{idx}. {report}")
                try:
                    index = int(input("Enter the report number to delete: ")) - 1
                    if 0 <= index < len(sec.reports):
                        deleted = sec.reports.pop(index)
                        print(f"Report deleted: {deleted}")
                    else:
                        print("Invalid report number.")
                except ValueError:
                    print("Invalid input.")
                return
        print(f"No security found at {location}")

    def view_security_logs(self):
        if not self.security_logs:
            print("No security logs available.")
            return
        for security in self.security_logs:
            print(f"Location: {security.get_location()}")
            print(f"Total Incidents: {len(security.incident_log)}")
            print(f"Total Reports: {len(security.reports)}")
            if security.incident_log:
                print("\nRecent Incidents:")
                for incident in security.incident_log[-3:]:
                    print(f"- {incident}")
            print()

    def export_stores(self, filename):
        try:
            with open(filename, 'w') as file:
                file.write("=== STORES REPORT ===\n")
                file.write(f"Generated: {datetime.datetime.now()}\n")
                file.write(f"Total Stores: {len(self.stores)}\n\n")
                for store in self.stores:
                    file.write(store.get_store_info())
                total_rent = sum(store.rent_amount for store in self.stores)
                file.write(f"\nTOTAL RENT: ${total_rent:,.2f}\n")
            print(f"Report saved to {filename}")
        except Exception as e:
            print(f"Error exporting stores: {e}")
