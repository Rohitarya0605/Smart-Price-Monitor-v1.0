![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-yellow)
# 📈 Smart Price Monitor

A modern **FastAPI-based competitor price monitoring platform** that helps businesses track product prices, compare competitor pricing, visualize price trends, and manage products through an interactive dashboard.

Built with **FastAPI, SQLAlchemy, JWT Authentication, SQLite, Jinja2, and Chart.js**.

---

## 🚀 Features

### 🔐 Authentication System
- User Signup
- User Login
- JWT-based Authentication
- Secure Session Handling
- Logout Functionality

### 📦 Product Management (CRUD)
- Add new products
- Edit existing products
- Delete products
- View tracked products in dashboard

### 💹 Price Monitoring
Track product prices across:
- Your Price
- Amazon Price
- Flipkart Price

Automatically identify:
- ✅ Best Price
- ⚠ Competitor Cheaper
- 📉 Price Drops

### 📊 Price History Analytics
- Historical price tracking
- Automatic history update on every product edit
- Interactive line charts using Chart.js
- Trend visualization for competitor comparison

### 🎨 Modern Dashboard UI
- Responsive dark theme
- Glassmorphism cards
- Analytics widgets
- Clean admin dashboard experience

---

# 🖥️ Dashboard Preview

## Login Page
Secure JWT login system.

## Main Dashboard
Includes:
- Product statistics
- Price analytics chart
- Product cards
- CRUD operations

---

# 🛠 Tech Stack

## Backend
- FastAPI
- Python 3
- SQLAlchemy ORM
- SQLite
- JWT Authentication
- Passlib / Bcrypt

## Frontend
- HTML5
- CSS3
- Jinja2 Templates
- JavaScript
- Chart.js

## Development Tools
- VS Code
- Git
- GitHub

---

# 📂 Project Structure

```bash
Smart-Price-Monitor-v1.0/
│
├── main.py
├── auth.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── edit.html
│   ├── login.html
│   └── signup.html
│
├── static/
│   └── style.css
│
└── _pycache_/
```

---


User → FastAPI → JWT Auth → SQLAlchemy ORM → SQLite DB

                         
                         ↓
                   
                    Dashboard + Charts

## 📊 Project Stats

- Backend Routes: 10+
- Database Tables: 3
- Authentication: JWT
- Features Implemented: 15+
- Development Time: 20+ hours


| Feature | Status |
|---------|--------|
| JWT Authentication | ✅ |
| Product CRUD | ✅ |
| Price Analytics | ✅ |
| Chart Visualization | ✅ |
| Responsive UI | ✅ |
| Price Alerts | 🚧 |



# ⚙️ Installation Guide

## 1. Clone Repository

```bash
git clone https://github.com/Rohitarya0605/Smart-Price-Monitor-v1.0
cd Smart-Price-Monitor-v1.0
```

---

## 2. Create Virtual Environment

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run Application

```bash
uvicorn main:app --reload
```

---

## 5. Open Browser

```bash
http://127.0.0.1:8000
```

---

# 🧠 Database Schema

## Users Table
| Field | Type |
|---|---|
| id | Integer |
| username | String |
| hashed_password | String |

---

## Products Table
| Field | Type |
|---|---|
| id | Integer |
| product_name | String |
| your_price | Float |
| amazon_price | Float |
| flipkart_price | Float |

---

## Price History Table
| Field | Type |
|---|---|
| id | Integer |
| product_id | Integer |
| day | String |
| your_price | Float |
| amazon_price | Float |
| flipkart_price | Float |

---

# 🔄 Workflow

1. User signs up / logs in  
2. JWT token generated  
3. User accesses dashboard  
4. Add product pricing details  
5. Product stored in database  
6. Price history automatically recorded  
7. Every update creates new historical record  
8. Chart reflects pricing trend  

---

# 📌 Use Cases

This platform can be used by:

- E-commerce businesses
- Product managers
- Pricing analysts
- Competitor research teams
- Marketplace sellers

---

# 🔮 Future Improvements

Potential upgrades:

- Real-time web scraping
- Email alerts for price drops
- AI-based price prediction
- Product search and filtering
- CSV / PDF export
- Admin analytics dashboard
- Multi-user product ownership
- PostgreSQL deployment
- Cloud deployment

---

# 📚 Learning Outcomes

This project helped in understanding:

- FastAPI backend development
- Database relationships
- CRUD operations
- Authentication using JWT
- ORM with SQLAlchemy
- Data visualization
- Full-stack project architecture
- Git & GitHub workflow

---

# 👨‍💻 Author

**Nupur Patankar, Rohit Arya, Sneha Pawar, Manavi Tamkhane, Sneha Gadhave, Swayambhu Swami**

B.Tech Electronics & Communication Engineering  
MIT ADT University, Pune  


---

# ⭐ Support

If you found this project useful, consider starring the repository.

---
