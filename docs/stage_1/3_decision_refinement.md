# Task 3 - Decision and Refinement

## Project

**Hotel Girasol Stock Flow**

## Final Decision

The selected Portfolio Project MVP is:

# Hotel Girasol Stock Flow

The project was selected because it addresses a real inventory problem while remaining technically realistic for an individual developer.

It also provides opportunities to apply:

* Python
* Flask
* Backend development
* Database design
* SQL
* Authentication
* HTML
* CSS
* JavaScript
* Testing
* Git

## Problem Statement

Hotel Girasol currently depends heavily on manual inventory verification.

A complete inventory check can take approximately **40 minutes**.

There is also limited immediate traceability when products move from inventory to hotel operations.

When an employee delivers a product, the system should be able to maintain information about:

* Employee
* Product
* Quantity
* Hotel room
* Date
* Time

Hotel Girasol Stock Flow aims to maintain this information digitally and reduce unnecessary repeated inventory verification.

The application will not completely eliminate physical inventory checks.

Physical verification will still be performed when necessary.

## Target Users

### Hotel Employees

Employees will record product movements and deliveries.

### Supervisors

Supervisors will be able to review current inventory information and transaction history.

### Hotel Management

Management will have better visibility into inventory activity and low-stock products.

---

# Core Inventory Workflow

A basic product delivery will follow:

**Employee → Product → Quantity → Room → Date → Time**

Example:

An employee delivers two units of a product to Room 204.

The application records:

* Employee responsible
* Product
* Quantity: 2
* Room: 204
* Current date
* Current time

The inventory quantity is reduced accordingly.

The transaction is then stored in the historical record.

---

# MVP Features

## 1. Authentication

Employees must log in before accessing inventory functionality.

## 2. Employee Identification

Every transaction will be associated with the authenticated employee.

## 3. Product Inventory

Authorized users can view products and current recorded quantities.

## 4. Product Management

Authorized users can create and update product information.

## 5. Delivery Registration

Employees can register products delivered to hotel rooms.

## 6. Quantity Tracking

Every transaction records the amount of product involved.

## 7. Room Tracking

Deliveries can be associated with a hotel room.

## 8. Automatic Timestamp

The application automatically records transaction date and time.

## 9. Automatic Inventory Update

A valid delivery automatically reduces the corresponding inventory quantity.

## 10. Restocking

Authorized users can register products added back into inventory.

## 11. Low-Stock Identification

Products below a defined threshold are identified as low stock.

## 12. Transaction History

Authorized users can review previous inventory transactions.

A transaction will include:

* Employee
* Product
* Quantity
* Transaction type
* Room when applicable
* Date
* Time

---

# MVP Boundaries

The initial MVP will focus on:

* Authentication
* Employees
* Products
* Inventory quantities
* Room deliveries
* Restocking
* Low-stock detection
* Transaction history

The following are not required for the first MVP:

* Advanced analytics
* Machine-learning predictions
* Complex dashboards
* Barcode scanning
* QR scanning
* Multi-hotel support
* Automated purchasing

These features may be considered after the core system is stable.

---

# Expected Outcome

Hotel Girasol Stock Flow is expected to provide:

* Faster access to inventory information
* Better transaction traceability
* Reduced unnecessary manual counting
* Better employee accountability
* Easier identification of low-stock products
* Historical inventory information
* Better visibility into product movement

## Measurable Goal

The existing inventory process can take approximately **40 minutes**.

The project will investigate whether the software-assisted workflow can reduce inventory verification time to approximately **15 minutes**.

This is a target and not a guaranteed result.

It will be measured after a functional version of the system has been developed.

---

# Technology Stack

## Python

Used for:

* Application logic
* Inventory calculations
* Validation
* Backend development

## Flask

Used as the web application framework.

## PostgreSQL

Used to permanently store:

* Users
* Employees
* Products
* Inventory
* Rooms
* Transactions

## SQLAlchemy

Used to communicate between the Python application and PostgreSQL.

## Flask-Login

Used for authentication and user sessions.

## HTML

Used to structure application pages.

## CSS

Used for application styling.

## JavaScript

Used for client-side interactions and dynamic interface behavior.

## Jinja2

Used by Flask to render server-side HTML templates.

## pytest

Used to test important backend and inventory functionality.

## Git and GitHub

Used for source control and project history.

---

# Main Challenges

## Inventory Accuracy

Digital inventory must remain synchronized with actual physical inventory.

## Transaction Validation

The application must prevent invalid quantities and inventory from becoming negative.

## Authentication

Only authorized users should be able to access inventory functionality.

## Data Consistency

Product quantities and transaction history must remain consistent.

## Usability

Recording a transaction should be fast and simple.

## Scope

Advanced features must not delay completion of the MVP.

---

# Task 3 Conclusion

Hotel Girasol Stock Flow has been refined into a realistic MVP.

The core objective is:

**Record product movements accurately and use that information to reduce unnecessary manual inventory work.**