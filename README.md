# Coffee Shop Management System

## Overview

This is a simple Python application that models a coffee shop ordering system. It includes core entities such as Customers, Coffees, and Orders, allowing the creation and management of orders, and provides statistics like order counts, average prices, and customer affinities.

The system enforces input validation and exception handling to ensure data integrity.

---

## Features

- Create and manage customers with validated attributes.
- Define coffee types with validated names.
- Place orders linking customers and coffee types, with price validation.
- Retrieve statistics such as number of orders and average price per coffee.
- Identify the top customer (“most aficionado”) for a given coffee type.
- Simple in-memory storage for all orders during runtime.

---

## Getting Started

Clone the repository and navigate to the phase-3/coffee_shop directory.

Ensure Python 3.8 or above is installed.

Run the interactive debug script to test the system: python -m coffee_shop.debug

## Running Tests

Unit tests are written with pytest. From the root project directory, run: pytest
