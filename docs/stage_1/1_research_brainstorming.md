# Task 1 - Research and Brainstorming

## Project

**Hotel Girasol Stock Flow**

## Problem Discovery

The Hotel Girasol Stock Flow idea originated from observing the current inventory workflow at Hotel Girasol.

Inventory verification depends heavily on manual counting.

A complete inventory check can take approximately **40 minutes**.

The problem is not only the time required to complete the inventory.

There is also limited immediate visibility into product movements during normal hotel operations.

When an employee takes or delivers a product, useful information includes:

* Employee responsible
* Product
* Quantity
* Hotel room
* Date
* Time

Recording this information digitally could make current inventory information easier to maintain and reduce repeated manual verification.

The main question behind the project became:

**How can software reduce unnecessary manual inventory work while maintaining a reliable record of product movement?**

## Research Areas

The initial project research focused on problems involving:

* Inventory management
* Product tracking
* Employee accountability
* Product delivery tracking
* Operational efficiency
* Data visibility
* Low-stock detection
* Transaction history

Several possible software solutions were considered before selecting the final project.

---

# Idea 1 - Hotel Girasol Stock Flow

Hotel Girasol Stock Flow is a digital inventory management system designed around Hotel Girasol's inventory workflow.

The application would maintain current inventory quantities and record product movements.

A product transaction could contain:

* Employee
* Product
* Quantity
* Room
* Date
* Time

## Main Goal

Reduce unnecessary manual inventory verification while improving inventory traceability.

## Potential Benefits

* Faster access to inventory information
* Fewer unnecessary complete inventory counts
* Better product transaction history
* Better employee accountability
* Easier identification of low-stock products
* Better visibility into product movement

---

# Idea 2 - Hotel Maintenance Tracker

A second idea considered was a maintenance request management system.

Hotel employees could report problems involving:

* Air conditioning
* Plumbing
* Electrical systems
* Furniture
* Hotel room equipment
* Common areas

Each request could contain:

* Location or room
* Problem description
* Priority
* Employee who reported it
* Date and time
* Current status

## Main Goal

Improve organization and communication between hotel employees and maintenance personnel.

---

# Idea 3 - Employee Shift Task Manager

A third idea considered was a system for managing employee responsibilities during work shifts.

The system could track:

* Employee
* Shift
* Assigned task
* Priority
* Status
* Completion time

## Main Goal

Provide better visibility into tasks that must be completed during each shift.

---

# How Might We Questions

The "How Might We" technique was used to explore the inventory problem.

Questions included:

* How might we reduce the amount of time spent manually checking inventory?
* How might we know which employee handled a product?
* How might we record which product was delivered?
* How might we record how many units were delivered?
* How might we know which hotel room received a product?
* How might we automatically record when the transaction occurred?
* How might we identify products that are running low?
* How might we know when physical inventory verification is necessary?
* How might we make inventory transactions quick enough for normal employee workflows?

These questions helped refine the project into a focused inventory system.

---

# SCAMPER Analysis

## Substitute

Replace part of the manual inventory recording process with digital transaction records.

## Combine

Combine information about:

* Employees
* Products
* Quantities
* Rooms
* Inventory
* Transactions
* Dates and times

inside one system.

## Adapt

Adapt common inventory-management concepts to the operational workflow of Hotel Girasol.

## Modify

Update recorded inventory quantities whenever product movements occur instead of depending entirely on complete inventory counts.

## Put to Another Use

Use transaction history to provide information about product usage and inventory activity.

## Eliminate

Reduce unnecessary repeated inventory verification when reliable digital records already exist.

Physical inventory verification will still be performed when necessary.

## Reverse

Instead of performing a complete count simply to discover which products may be low, allow the system to identify inventory that may require verification or replenishment.

---

# Initial Technical Research

The project requires a web application with persistent inventory information.

The selected initial technical direction is:

## Backend

* Python
* Flask
* SQLAlchemy
* Flask-Login

## Database

* PostgreSQL

## Frontend

* HTML
* CSS
* JavaScript
* Jinja2

## Testing

* pytest

## Version Control

* Git
* GitHub

This stack was selected because it provides everything required to build the MVP while keeping the architecture manageable for an individual developer.

---

# Task 1 Conclusion

Three possible project concepts were considered:

1. Hotel Girasol Stock Flow
2. Hotel Maintenance Tracker
3. Employee Shift Task Manager

Hotel Girasol Stock Flow appeared to provide the strongest connection between a real operational problem, measurable potential improvement, and relevant software engineering challenges.

The next step was to evaluate the ideas using consistent criteria.