# Basic_Bank_Management_System
A console-based Bank Management System using Python and MySQL to manage customer records, bank accounts, deposits, withdrawals, and transactions.



# 🏦 Basic Bank Management System

A console-based banking application developed using **Python and MySQL** to manage customer information, bank accounts, and financial transactions.

## 📌Project Overview

The Basic Bank Management System is a beginner-friendly database project that demonstrates how Python connects with MySQL to perform banking operations and manage structured data efficiently.

The project uses a relational database to organize customer records, account information, and transaction details.

## Project Objectives

- Develop a Python application connected to a MySQL database.
- Store and manage customer and account information.
- Perform database operations using SQL.
- Maintain transaction records.
- Practice database design and Python–MySQL integration.

## 🛠️ Technologies Used

- **Python** — Application logic
- **MySQL** — Relational database management
- **MySQL Workbench** — Database design and SQL execution
- **VS Code** — Development environment
- **MySQL Connector/Python** — Database connectivity

##  Key Features

- Customer record management
- Bank account management
- Deposit and withdrawal operations
- Fund transfers between accounts
- Balance inquiry
- Transaction history
- SQL CRUD operations

*Note: Include only the features implemented and tested in your current version.*

## 🗄️ Database Design

The project uses a MySQL database named `bank_management`.

| Table | Purpose |
|---|---|
| `customers` | Stores customer information |
| `accounts` | Stores account details and balances |
| `transactions` | Records financial transactions |

Primary keys and foreign keys help maintain relationships between the tables.

## 📂 Project Structure

```text
Basic-Bank-Management-System/
├── main.py
├── database/
│   └── bank_management.sql
├── screenshots/
│   ├── application.png
│   └── database.png
├── requirements.txt
├── .gitignore
└── README.md
```

*Adjust the filenames to match your actual project.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Basic-Bank-Management-System
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

- Open MySQL Workbench.
- Create or select the `bank_management` database.
- Execute the SQL script provided in the `database` folder.
- Configure your database connection settings in the Python application.

**Security:** Keep database passwords in environment variables or a local configuration file excluded from Git. Never publish real credentials.

### 5. Run the application

```bash
python main.py
```

##  Screenshots

Add screenshots of your running Python application and MySQL database here.

### Application Output

![Bank Management System Application](screenshots/application.png)

### MySQL Database

![Bank Management System Database](screenshots/database.png)

##  Skills Demonstrated

- Python programming
- SQL queries and database management
- MySQL database connectivity
- Relational database design
- CRUD operations
- Primary keys and foreign keys
- Data integrity and transaction management
- Problem-solving and debugging

## Future Improvements

- Add a graphical user interface.
- Implement secure user authentication.
- Add input validation and error handling.
- Improve transaction safety and rollback handling.
- Generate account statements and transaction reports.

##  Author

**Mohd Jishan Ansari**

Aspiring Data Analyst | Python | SQL | Excel | Power BI

---

⭐ This project is part of my learning journey in Python programming, SQL, and database management.
