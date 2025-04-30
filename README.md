# Mall Complex Management

A Console-based management system for shopping malls.

This project allows users to easily manage and organize important records through a simple and intuitive web interface.

## Features

-**Store Management**

  -Add and manage store number, floor, and rent

  -Export all store data to a text file

-**Investor Management**

  -Register investors and store their contact information

-**Customer Management**

  -Add new customers to the system

-**Manager Management**

  -Register mall managers with employee ID and contact details

-**Facility Maintenance**

  -Create maintenance requests

  -Export maintenance request logs to a text file

-**Security Management**

  -Log and manage security incidents

  -Export security logs to a text file

-**Financial Reporting**

  -Generate financial reports using revenue and sales data

-**Tenant Management**

  -Add tenants and manage lease terms and store assignments

-**Rental Payment Management**

  -Record rental payments and track their status 

  -Export rental payment records to a text file

-**Visitor Tracking**

  -Track mall visitor count (increment/decrement)

  -Log entry times for visitor tracking

-**Report Exporting**

  -Export various records (stores, maintenance, security, payments) to text files






## File Structure
```plaintext
CECS343Project/
├── README.md
├── code/
│       └── main.py
│       ├── store.py
│       ├── investor.py
│       ├── customer.py
│       ├── manager.py
│       ├── tenant.py
│       ├── rentalpayment.py
│       ├── facilitymaintenance.py
│       ├── financialreporting.py
│       ├── security.py
│       ├── securitymanagement.py
│       └── visitortracking.py
```


## How to Run
1. Open your terminal,clone the repository and navigate to the project directory:
```bash
git clone https://github.com/itznuth/CECS343Project.git
cd CECS343Project/code

2. Run the main Python file:
 ```bash
 python3 main.py
```
4. You will first see a login prompt:
```text
=== Mall Management System ===
1. Login
2. Exit
Choose: 
```

4. After logging in, follow the interactive menu to use various features:
```text
ADMIN DASHBOARD
1. Manage Stores
2. Manage Investors
3. Manage Managers
...
10. Export Data
11. Logout
Choose: 
```
<Example actions: Manage Tenants ->7>

5. After choosing a number, follow the interactive menu to use various features:
```text
ADMIN DASHBOARD
TENANT MANAGEMENT
1. Add Tenant
2. Update Tenant
...
5. Back
Choose: 
```

<Example actions: View All Tenants ->4>
```text
ALL TENANTS:
Name: Fashion Store
Store: 101
Lease: 2023-01-01 to 2024-01-01
Contact: contact@fashion.com
```




## Tech Stack
-**Language**: Python 3  
- **Execution Environment**: Console-based CLI  
- **Data Handling**: File I/O  
- **Date Handling**: Built-in `datetime` module  
- **Structure**: Class-based modular design (each feature in a separate `.py` file)

## Author
Anthony Nuth

Daeun Han

Ediz Cavus

Wardah Abuhadba

Priscilla Romero
