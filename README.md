## Video
https://youtu.be/wagjz9EjKEE?si=HnhCWd9B0rtj-NPP

## Title

bank_project

## Description

Zaki Bank is a Python program that simulates a simple bank management system. The goal of this project is to practice Python, Object-Oriented Programming (OOP), functions, classes, input validation, and working with multiple files.

The program has two main types of users: customers and employees. A customer can manage their bank account, while an employee can perform different tasks depending on their job.

## Customer Features

Customers can:

- Deposit money into their account.
- Withdraw money.
- Transfer money to another customer.
- Open a new account.
- Borrow money.
- Pay their debts.
- See their account information.
- Change their personal information.
- See the services provided by the bank.

The program checks the information entered by the user before accepting it. For example, it checks account numbers, phone numbers, passwords, dates, balances, and other data.

## Employee Features

Employees have different roles and responsibilities. The employee section provides access to:

- Accounting operations.
- Creating a new worker.
- The management office.

Different employees can have different jobs, such as manager, accountant, cashier, and security.

## Object-Oriented Programming

I used classes to organize the main data in the program.

The `Client` class represents a bank customer. It stores information such as the customer's name, date of birth, account number, phone number, balance, password, and debts.

The `Workers` class represents a bank employee. It stores information such as the employee's name, ID, salary, phone number, job, and password.

I used methods and properties to control how this information is created and changed.

## Project Structure

The project is divided into different Python files:

- `bank_project.py` is the main file. It connects the different parts of the program and controls the main flow.
- `client.py` contains the `Client` class and customer operations.
- `workers.py` contains the `Workers` class and employee operations.
- `design.py` contains menus, messages, services, and rules.

I separated the program into different files because putting everything in one file would make the project harder to read and manage.

## Validation and Security

Input validation is an important part of the project. I used conditions, properties, regular expressions, and loops to check user input.

For example, the program checks whether a phone number has the correct format and whether an account number has the required length.

The program also uses passwords and limits incorrect password attempts. This is only a simulation and is not intended to be used as a real banking system.

## Sample Data

The project contains sample customers and workers so that the program can be tested without creating all the data manually.

## How to Run

Make sure Python is installed. Then run:

`python bank_project.py`

The program will display the main menu and ask the user whether they want to use the customer or employee section.

## Design Decisions

I chose a bank management system because it allowed me to combine many Python concepts in one project. Instead of creating a small program with only a few operations, I wanted to build a larger system where different parts interact with each other.

This project helped me practice functions, classes, objects, properties, validation, loops, conditions, and organizing a Python program into multiple files."
