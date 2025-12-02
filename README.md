# 📦 Inventory Management System (Flask)

A clean, simple, and efficient **Inventory Management System** built using **Flask**, **HTML**, **CSS**, and **SQLite**.  
This application is designed for businesses, shops, and students who want a lightweight and easy-to-use stock management solution.

The system provides **role-based access** for both **Admin** and **User**, ensuring proper control, security, and smooth workflow.

---

## 🚀 Key Features

### 🔐 Role-Based Access Control (RBAC)
- **Admin**
  - Full access to the system
  - Can add, edit, update, and delete products
  - Can manage stock and quantities
  - Can view, accept, or reject user requests
  - Can see analytics or dashboard stats (if added)

- **User**
  - Can view available inventory
  - Can send requests to admin (e.g., stock request)
  - Can see status of their requests
  - Limited permissions for safety

---

## 📊 Core Inventory Features
- Add new products with price, quantity, description
- Update product details
- Delete products safely
- Search items quickly
- Clean and consistent UI across all pages
- Error Pages (Invalid password, User not found)
- Direct buttons for login/register
- Mobile-friendly design

---

## 📁 Project Structure (Example)
/inventory_management_system
│── app.py
│── static/
│── templates/
│── requirements.txt
│── README.md
│── database.db (auto-created)

