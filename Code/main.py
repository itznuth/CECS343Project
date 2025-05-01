import datetime
from datamanager import DataManager
from security import Security
from manager import Manager
from tenant import Tenant
from investor import Investor
from store import Store
from rentalpayment import RentalPayment, export_payments
from facilitymaintenance import FacilityMaintenance
from financialreporting import FinancialReporting

class MallManagementSystem:
    def __init__(self):
        # Initialize with sample data
        self.data_manager = DataManager(
            stores=[
                Store(1, 1, 5000, "Fashion Store"),  
                Store(2, 1, 7500, "Vacant")          
            ],
            investors=[Investor("Anthony", "anthony@example.com")],
            managers=[Manager("John Smith", 1001, "John", "Operations", 2)],
            maintenance_requests=[],
            tenants=[
                Tenant(
                    name="Fashion Store",
                    space_number=1,  
                    lease_start_date="2023-01-01",
                    lease_end_date="2024-01-01",
                    contact_information="contact@fashion.com"
                )
            ],
            rental_payments=[RentalPayment(5000, "2023-06-01", 1, "completed")],
            financial_reports=[],
            security_logs=[Security("Main Entrance")]
        )
        self.current_user = None
        self.current_tenant = None

    def login(self):
        while True:
            print("\n=== Mall Management System ===")
            print("1. Login")
            print("2. Exit")
            choice = input("Choose: ")

            if choice == "1":
                username = input("Username: ").lower()
                password = input("Password: ")

                # Check admin
                if username == "admin" and password == "admin":
                    self.current_user = "admin"
                    print("\nWelcome Admin!")
                    self.admin_menu()
                    continue

                # Check managers
                for manager in self.data_manager.managers:
                    if (manager.name.lower() == username and 
                        manager.contact_information.lower() == password):
                        self.current_user = "manager"
                        print(f"\nWelcome Manager {manager.name}!")
                        self.manager_menu()
                        break

                # Check tenants
                for tenant in self.data_manager.tenants:
                    if (tenant.name.lower() == username and 
                        tenant.contact_information.lower() == password):
                        self.current_user = "tenant"
                        self.current_tenant = tenant
                        print(f"\nWelcome Tenant {tenant.name}!")
                        self.tenant_dashboard()
                        break

                # Check security
                for security in self.data_manager.security_logs:
                    if (security.get_location().lower() == username and 
                        password == "security"):
                        self.current_user = "security"
                        print(f"\nWelcome Security at {security.get_location()}!")
                        self.security_menu()
                        break

                if not self.current_user:
                    print("Invalid credentials or user not found.")

            elif choice == "2":
                print("Goodbye!")
                exit()
            else:
                print("Invalid option.")

    def admin_menu(self):
        while True:
            print("\nADMIN DASHBOARD")
            print("1. Manage Stores")
            print("2. Manage Investors")
            print("3. Manage Managers")
            print("4. Maintenance Requests")
            print("5. Security Management")
            print("6. Financial Reports")
            print("7. Manage Tenants")
            print("8. Rental Payments")
            print("9. View All Data")
            print("10. Export Data")
            print("11. Logout")

            choice = input("Choose: ")

            if choice == "1":
                self.store_menu()
            elif choice == "2":
                self.investor_menu()
            elif choice == "3":
                self.manager_management_menu()
            elif choice == "4":
                self.maintenance_request_menu()
            elif choice == "5":
                self.security_menu()
            elif choice == "6":
                self.financial_menu()
            elif choice == "7":
                self.tenant_management_menu()
            elif choice == "8":
                self.rental_menu()
            elif choice == "9":
                self.view_all_data()
            elif choice == "10":
                self.export_data_menu()
            elif choice == "11":
                self.current_user = None
                return
            else:
                print("Invalid option.")

    def store_menu(self):
        while True:
            print("\nSTORE MANAGEMENT")
            print("1. Add Store")
            print("2. Update Store")
            print("3. Delete Store")
            print("4. View All Stores")
            print("5. Back")

            choice = input("Choose: ")

            if choice == "1":
                self.data_manager.add_store()
            elif choice == "2":
                self.data_manager.update_store()
            elif choice == "3":
                self.data_manager.delete_store()
            elif choice == "4":
                print("\nALL STORES:")
                self.data_manager.view_stores()
            elif choice == "5":
                return
            else:
                print("Invalid option.")

    def investor_menu(self):
        while True:
            print("\nINVESTOR MANAGEMENT")
            print("1. Add Investor")
            print("2. Update Investor")
            print("3. Delete Investor")
            print("4. View All Investors")
            print("5. Back")

            choice = input("Choose: ")

            if choice == "1":
                self.data_manager.add_investor()
            elif choice == "2":
                self.data_manager.update_investor()
            elif choice == "3":
                self.data_manager.delete_investor()
            elif choice == "4":
                print("\nALL INVESTORS:")
                self.data_manager.view_investors()
            elif choice == "5":
                return
            else:
                print("Invalid option.")

    def manager_management_menu(self):
        while True:
            print("\nMANAGER MANAGEMENT")
            print("1. Add Manager")
            print("2. Update Manager")
            print("3. Delete Manager")
            print("4. View All Managers")
            print("5. Back")

            choice = input("Choose: ")

            if choice == "1":
                self.data_manager.add_manager()
            elif choice == "2":
                self.data_manager.update_manager()
            elif choice == "3":
                self.data_manager.delete_manager()
            elif choice == "4":
                print("\nALL MANAGERS:")
                self.data_manager.view_managers()
            elif choice == "5":
                return
            else:
                print("Invalid option.")

    def maintenance_request_menu(self):
        while True:
            print("\nMAINTENANCE REQUESTS")
            print("1. Create Request")
            print("2. Update Request")
            print("3. Delete Request")
            print("4. View All Requests")
            print("5. Back")

            choice = input("Choose: ")

            if choice == "1":
                self.data_manager.create_maintenance_request()
            elif choice == "2":
                self.data_manager.update_maintenance_request()
            elif choice == "3":
                self.data_manager.delete_maintenance_request()
            elif choice == "4":
                print("\nALL MAINTENANCE REQUESTS:")
                self.data_manager.view_maintenance_requests()
            elif choice == "5":
                return
            else:
                print("Invalid option.")

    def security_menu(self):
        while True:
            print("\nSECURITY MANAGEMENT")
            print("1. Log Incident")
            print("2. Add Security Report")
            print("3. Delete Security Report")
            print("4. View Security Logs")
            print("5. Export Incidents")
            print("6. Back")

            choice = input("Choose: ")

            if choice == "1":
                if not self.data_manager.add_security():
                    print("Failed to log incident. Please try again.")
                self.data_manager.add_security()
            elif choice == "2":
                self.data_manager.add_security_report()
            elif choice == "3":
                self.data_manager.delete_security_report()
            elif choice == "4":
                print("\nSECURITY LOGS:")
                self.data_manager.view_security_logs()
            elif choice == "5":
                filename = input("Enter filename (default: security_incidents.txt): ") or "security_incidents.txt"
                self.data_manager.export_security_incidents(filename)
            elif choice == "6":
                return
            else:
                print("Invalid option.")

    def financial_menu(self):
        while True:
            print("\nFINANCIAL REPORTS")
            print("1. Generate Report")
            print("2. Update Report")
            print("3. Delete Report")
            print("4. View All Reports")
            print("5. Back")

            choice = input("Choose: ")

            if choice == "1":
                self.data_manager.generate_financial_report()
            elif choice == "2":
                self.data_manager.update_financial_report()
            elif choice == "3":
                self.data_manager.delete_financial_report()
            elif choice == "4":
                print("\nFINANCIAL REPORTS:")
                self.data_manager.view_financial_reports()
            elif choice == "5":
                return
            else:
                print("Invalid option.")

    def tenant_management_menu(self):
        while True:
            print("\nTENANT MANAGEMENT")
            print("1. Add Tenant")
            print("2. Update Tenant")
            print("3. Delete Tenant")
            print("4. View All Tenants")
            print("5. Back")

            choice = input("Choose: ")

            if choice == "1":
                self.data_manager.add_tenant()
            elif choice == "2":
                self.data_manager.update_tenant()
            elif choice == "3":
                self.data_manager.delete_tenant()
            elif choice == "4":
                print("\nALL TENANTS:")
                self.data_manager.view_tenants()
            elif choice == "5":
                return
            else:
                print("Invalid option.")

    def rental_menu(self):
        while True:
            print("\nRENTAL PAYMENTS")
            print("1. Record Payment")
            print("2. Update Payment")
            print("3. Delete Payment")
            print("4. View All Payments")
            print("5. Export Payments")
            print("6. Back")

            choice = input("Choose: ")

            if choice == "1":
                self.data_manager.record_rental_payment()
            elif choice == "2":
                self.data_manager.update_rental_payment()
            elif choice == "3":
                self.data_manager.delete_rental_payment()
            elif choice == "4":
                print("\nRENTAL PAYMENTS:")
                self.data_manager.view_rental_payments()
            elif choice == "5":
                filename = input("Enter filename (default: payments.txt): ") or "payments.txt"
                export_payments(self.data_manager.rental_payments, filename)
            elif choice == "6":
                return
            else:
                print("Invalid option.")

    def manager_menu(self):
        while True:
            print("\nMANAGER DASHBOARD")
            print("1. View Stores")
            print("2. View Tenants")
            print("3. View Maintenance Requests")
            print("4. Generate Report")
            print("5. Logout")

            choice = input("Choose: ")

            if choice == "1":
                print("\nALL STORES:")
                self.data_manager.view_stores()
            elif choice == "2":
                print("\nALL TENANTS:")
                self.data_manager.view_tenants()
            elif choice == "3":
                print("\nMAINTENANCE REQUESTS:")
                self.data_manager.view_maintenance_requests()
            elif choice == "4":
                report = self.generate_manager_report()
                print("\n" + report)
            elif choice == "5":
                self.current_user = None
                return
            else:
                print("Invalid option.")

    def tenant_dashboard(self):
        """Restricted dashboard for tenants"""
        while True:
            print(f"\nTENANT DASHBOARD - {self.current_tenant.name}")
            print("1. Make Rental Payment")
            print("2. Update My Information")
            print("3. View My Payment History")
            print("4. Logout")

            choice = input("Choose: ")

            if choice == "1":
                self.make_tenant_payment()
            elif choice == "2":
                self.update_tenant_info()
            elif choice == "3":
                self.view_tenant_payments()
            elif choice == "4":
                self.current_user = None
                self.current_tenant = None
                return
            else:
                print("Invalid option.")

    def make_tenant_payment(self):
        """Handle rental payments for current tenant"""
        try:
            print(f"\nMake Payment for {self.current_tenant.name}")
            amount = float(input("Enter payment amount: "))
            date = input("Enter payment date (YYYY-MM-DD): ")

            self.data_manager.rental_payments.append(
                RentalPayment(
                    amount=amount,
                    date=date,
                    unit=self.current_tenant.space_number,
                    status="completed"
                )
            )
            print(f"Payment of ${amount:,.2f} recorded successfully!")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def update_tenant_info(self):
        """Allow tenants to update their contact info"""
        print("\nUPDATE MY INFORMATION")
        print(f"Current Name: {self.current_tenant.name}")
        print(f"Current Contact: {self.current_tenant.contact_information}")

        new_name = input("Enter new name (press Enter to keep current): ")
        new_contact = input("Enter new contact info (press Enter to keep current): ")

        if new_name:
            self.current_tenant.name = new_name
        if new_contact:
            self.current_tenant.contact_information = new_contact

        print("\nInformation updated successfully!")

    def view_tenant_payments(self):
        """Show payment history for current tenant"""
        payments = [
            p for p in self.data_manager.rental_payments 
            if p.unit == self.current_tenant.space_number
        ]

        if not payments:
            print("\nNo payment history found.")
            return

        print(f"\nPAYMENT HISTORY FOR {self.current_tenant.name}")
        print("=" * 40)
        for payment in payments:
            print(f"Date: {payment.date}")
            print(f"Amount: ${payment.amount:,.2f}")
            print(f"Status: {payment.status}")
            print("-" * 40)

    def security_dashboard(self):
        while True:
            print("\nSECURITY DASHBOARD")
            print("1. Log Incident")
            print("2. Add Security Report")
            print("3. View Security Logs")
            print("4. Export Incidents")
            print("5. Logout")

            choice = input("Choose: ")

            if choice == "1":
                self.data_manager.add_security()
            elif choice == "2":
                self.data_manager.add_security_report()
            elif choice == "3":
                print("\nSECURITY LOGS:")
                self.data_manager.view_security_logs()
            elif choice == "4":
                filename = input("Enter filename (default: incidents.txt): ") or "incidents.txt"
                for security in self.data_manager.security_logs:
                    security.export_incidents(filename)
            elif choice == "5":
                self.current_user = None
                return
            else:
                print("Invalid option.")

    def view_all_data(self):
        print("\n=== SYSTEM DATA OVERVIEW ===")
        print("\nSTORES:")
        self.data_manager.view_stores()

        print("\nTENANTS:")
        self.data_manager.view_tenants()

        print("\nINVESTORS:")
        self.data_manager.view_investors()

        print("\nMANAGERS:")
        self.data_manager.view_managers()

        print("\nSECURITY LOGS:")
        self.data_manager.view_security_logs()

        print("\nFINANCIAL REPORTS:")
        self.data_manager.view_financial_reports()

        print("\nMAINTENANCE REQUESTS:")
        self.data_manager.view_maintenance_requests()

        print("\nRENTAL PAYMENTS:")
        self.data_manager.view_rental_payments()

        input("\nPress Enter to continue...")

    def export_data_menu(self):
        print("\nEXPORT DATA")
        print("1. Export Stores")
        print("2. Export Rental Payments")
        print("3. Export Security Incidents")
        print("4. Back")

        choice = input("Choose: ")

        if choice == "1":
            filename = input("Enter filename (default: stores_export.txt): ") or "stores_export.txt"
            self.data_manager.export_stores(filename)
        elif choice == "2":
            filename = input("Enter filename (default: payments_export.txt): ") or "payments_export.txt"
            export_payments(self.data_manager.rental_payments, filename)
        elif choice == "3":
            if not self.data_manager.security_logs:
                print("No security logs available.")
                return
            for i, security in enumerate(self.data_manager.security_logs):
                print(f"{i+1}. {security.get_location()}")
            choice = input("Select security location to export: ")
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(self.data_manager.security_logs):
                    filename = input("Enter filename: ") or "incidents_export.txt"
                    self.data_manager.security_logs[idx].export_incidents(filename)
            except:
                print("Invalid selection.")
        elif choice == "4":
            return
        else:
            print("Invalid option.")

    def generate_manager_report(self):
        """Generate a summary report for managers"""
        report = "=== MANAGER REPORT ===\n"
        report += f"Generated: {datetime.datetime.now()}\n"
        report += f"Stores: {len(self.data_manager.stores)}\n"
        report += f"Tenants: {len(self.data_manager.tenants)}\n"
        report += f"Open Maintenance Requests: {len([r for r in self.data_manager.maintenance_requests if r.status == 'pending'])}\n"
        return report

if __name__ == "__main__":
    system = MallManagementSystem()
    system.login()
