# Hotel Girasol Stock Flow

Hotel Girasol Stock Flow is a software engineering portfolio project designed to improve inventory management at Hotel Girasol.

The project focuses on reducing unnecessary manual inventory work while providing better visibility and traceability of product movements.

## Problem

The current inventory process depends heavily on manual counting.

A complete inventory verification can take approximately **40 minutes**.

Another problem is the lack of immediate visibility into product movement. When an employee takes a product from inventory or delivers it to a hotel room, it is useful to know:

* Which employee handled the product
* Which product was involved
* How many units were used
* Which room received the product
* When the transaction occurred

Without a centralized digital record, inventory quantities may need to be repeatedly verified manually.

## Solution

Hotel Girasol Stock Flow will maintain a digital inventory and transaction history.

A typical product transaction will follow this structure:

**Employee → Product → Quantity → Room → Date → Time**

When a valid product delivery is registered:

1. The transaction is stored.
2. The employee responsible is recorded.
3. The hotel room is recorded.
4. The inventory quantity is updated automatically.
5. The transaction becomes part of the inventory history.

The system is not intended to completely eliminate physical inventory checks.

Instead, it should reduce unnecessary counting and make it easier to determine when physical verification is actually needed.

## Main Goal

The current manual inventory process can take approximately **40 minutes**.

One measurable goal of the project is to investigate whether a software-assisted workflow can reduce inventory verification time to approximately **15 minutes**.

This is a project target and will need to be validated through testing after the application is functional.

## Target Users

The primary users will be:

* Hotel employees
* Supervisors
* Hotel management

## MVP Features

The initial MVP will include:

1. User authentication
2. Employee identification
3. Product inventory
4. Product delivery registration
5. Quantity tracking
6. Room tracking
7. Automatic date and time recording
8. Inventory quantity updates
9. Restocking transactions
10. Low-stock identification
11. Transaction history

## Technology Stack

### Backend

* Python
* Flask
* SQLAlchemy
* Flask-Login

### Database

* PostgreSQL

### Frontend

* HTML
* CSS
* JavaScript
* Jinja2

### Testing

* pytest

### Development Tools

* Git
* GitHub

## Project Developer

### Anthony

Responsibilities:

* Project management
* Backend development
* Frontend development
* Database design
* Testing
* Documentation

Primary technical focus:

* Python
* Backend development
* APIs
* Databases

## Current Status

**Stage 1 — Research, Idea Evaluation, and MVP Definition**

The current objective is to define the problem, evaluate the project concept, establish the MVP scope, and document the initial development direction before implementation begins.

## Documentation

Stage 1 documentation is located in:

```text
docs/stage_1/
├── 0_team_formation.md
├── 1_research_brainstorming.md
├── 2_idea_evaluation.md
├── 3_decision_refinement.md
└── 4_stage_1_report.md
```