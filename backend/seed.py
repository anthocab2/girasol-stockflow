#!/usr/bin/python3
"""Seed test data for Girasol StockFlow."""

from database import get_connection, create_tables


def seed_employees(cursor):
    """Insert sample employees."""
    employees = [
        ("1001", "Anthony Caban", "admin", 1),
        ("1002", "Test Employee", "employee", 1),
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO employees
        (punch_number, full_name, role, active)
        VALUES (?, ?, ?, ?)
    """, employees)


def seed_products(cursor):
    """Insert sample products."""
    products = [
        ("Coca-Cola", "Beverage", 1.50, 30, 1),
        ("Sprite", "Beverage", 1.50, 25, 1),
        ("Water Bottle", "Beverage", 1.00, 40, 1),
        ("Medalla", "Alcohol", 3.00, 24, 1),
        ("Doritos", "Snack", 1.75, 20, 1),
        ("Snickers", "Snack", 1.50, 15, 1),
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO products
        (name, category, price, stock, active)
        VALUES (?, ?, ?, ?, ?)
    """, products)


def seed_database():
    """Create tables and insert sample data."""
    create_tables()

    connection = get_connection()
    cursor = connection.cursor()

    seed_employees(cursor)
    seed_products(cursor)

    connection.commit()
    connection.close()

    print("Database seeded successfully.")


if __name__ == "__main__":
    seed_database()
