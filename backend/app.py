#!/usr/bin/python3
"""Main Flask application for Girasol StockFlow."""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    """Return a simple API status message."""
    return {"message": "Girasol StockFlow API is running"}


if __name__ == "__main__":
    app.run(debug=True)
