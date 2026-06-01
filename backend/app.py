#!/usr/bin/python3
"""Main Flask application for Girasol StockFlow."""

from flask import Flask, jsonify, request
from database import get_connection

app = Flask(__name__)


@app.route("/")
def home():
    """Return a simple API status message."""
    return jsonify({"message": "Girasol StockFlow API is running"})


@app.route("/api/login", methods=["POST"])
def login():
    """Log in an employee using a punch number."""
    data = request.get_json()

    if not data or "punch_number" not in data:
        return jsonify({
            "success": False,
            "message": "Punch number is required"
        }), 400

    punch_number = data["punch_number"]

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, punch_number, full_name, role
        FROM employees
        WHERE punch_number = ? AND active = 1
    """, (punch_number,))

    employee = cursor.fetchone()
    connection.close()

    if employee is None:
        return jsonify({
            "success": False,
            "message": "Invalid punch number"
        }), 401

    return jsonify({
        "success": True,
        "employee": {
            "id": employee["id"],
            "punch_number": employee["punch_number"],
            "full_name": employee["full_name"],
            "role": employee["role"]
        }
    })


@app.route("/api/products")
def get_products():
    """Return all active products."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, category, price, stock, active
        FROM products
        WHERE active = 1
        ORDER BY category, name
    """)

    products = []
    for row in cursor.fetchall():
        products.append({
            "id": row["id"],
            "name": row["name"],
            "category": row["category"],
            "price": row["price"],
            "stock": row["stock"],
            "active": bool(row["active"])
        })

    connection.close()

    return jsonify(products)


if __name__ == "__main__":
    app.run(debug=True)
