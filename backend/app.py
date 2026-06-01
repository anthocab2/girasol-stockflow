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


@app.route("/api/sales", methods=["POST"])
def create_sale():
    """Create a sale and update product inventory."""
    data = request.get_json()

    required_fields = [
        "employee_id",
        "product_id",
        "quantity",
        "room_number",
        "payment_method"
    ]

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body is required"
        }), 400

    for field in required_fields:
        if field not in data:
            return jsonify({
                "success": False,
                "message": f"{field} is required"
            }), 400

    employee_id = data["employee_id"]
    product_id = data["product_id"]
    quantity = int(data["quantity"])
    room_number = str(data["room_number"])
    payment_method = data["payment_method"]

    if quantity <= 0:
        return jsonify({
            "success": False,
            "message": "Quantity must be greater than zero"
        }), 400

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, price, stock
        FROM products
        WHERE id = ? AND active = 1
    """, (product_id,))

    product = cursor.fetchone()

    if product is None:
        connection.close()
        return jsonify({
            "success": False,
            "message": "Product not found"
        }), 404

    if product["stock"] < quantity:
        connection.close()
        return jsonify({
            "success": False,
            "message": "Not enough stock available"
        }), 400

    total = product["price"] * quantity

    cursor.execute("""
        INSERT INTO sales (
            employee_id,
            product_id,
            quantity,
            room_number,
            payment_method,
            total
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        employee_id,
        product_id,
        quantity,
        room_number,
        payment_method,
        total
    ))

    cursor.execute("""
        UPDATE products
        SET stock = stock - ?
        WHERE id = ?
    """, (quantity, product_id))

    cursor.execute("""
        INSERT INTO inventory_movements (
            product_id,
            employee_id,
            movement_type,
            quantity_change,
            reason
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        product_id,
        employee_id,
        "sale",
        -quantity,
        f"Sale registered for room {room_number}"
    ))

    connection.commit()
    connection.close()

    return jsonify({
        "success": True,
        "message": "Sale registered successfully",
        "sale": {
            "product": product["name"],
            "quantity": quantity,
            "room_number": room_number,
            "payment_method": payment_method,
            "total": total
        }
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
