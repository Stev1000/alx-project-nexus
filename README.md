# 🛒 Project Nexus: E-Commerce Backend (ALX ProDev BE)

A full-featured **E-Commerce Backend API** built with **Django REST Framework (DRF)** as part of the ALX ProDev Backend Engineering track.  
This project simulates a real-world e-commerce backend environment, focusing on **scalability, security, and performance**.

---

## 📌 Features (Implemented ✅ / Advanced Planned ⏳)

### ✅ Core Features

- **User Authentication (JWT-secured)**
  - Register, login, refresh token, and manage user profile.
- **Product & Category Management**
  - Full CRUD APIs for products and categories.
- **Product Discovery**
  - Filter by category.
  - Sort by price.
  - Paginated responses for large datasets.
- **Cart Management**
  - Add, update, and remove items from cart.
- **Orders**
  - Place orders with multiple items.
  - Track order status (`pending`, `paid`, etc.).
- **Payments**
  - Record payments for orders.
  - View payment history per user.
- **Reviews**
  - Customers can leave product reviews with ratings.
- **Admin Dashboard**
  - Custom Django Admin with filters, search, and inline editing.
- **API Documentation**
  - Interactive Swagger UI (`/swagger/`) and ReDoc (`/redoc/`).

### ⏳ Advanced Features (Planned Roadmap)

- **Database Optimization**
  - PostgreSQL migration (currently SQLite in dev).
  - Indexing (`db_index=True`) and query tuning with `select_related` / `prefetch_related`.
- **Deployment & DevOps**
  - Docker & Docker Compose for containerized services.
  - CI/CD with GitHub Actions (automated tests & deployment).
  - Production deployment to **Heroku / AWS / DigitalOcean**.
- **Asynchronous Processing**
  - Celery + RabbitMQ for background tasks (e.g., order confirmation emails, payment notifications).
  - Scheduled jobs (e.g., nightly sales reports).
- **Caching**
  - Redis integration for product listing & query caching.
- **GraphQL API**
  - Parallel GraphQL endpoints using **Graphene-Django**.
- **Monitoring & Analytics**
  - Admin dashboard analytics (sales by day, top products).
  - Integration with tools like **Prometheus + Grafana** for monitoring.
- **Security Enhancements**
  - Rate limiting (DRF throttling).
  - CORS & CSRF protection for frontend integration.
  - Environment variable management (`.env` with `django-environ`).
- **Testing**
  - Unit tests & integration tests with `pytest` / `coverage`.
  - Postman collections for automated API testing.
- **Logging**
  - Centralized logging for payments, orders, and errors.
  - Request/response audit trail.

---

## ⚙️ Tech Stack

- **Backend Framework:** Django REST Framework (DRF)
- **Database:** SQLite (development) → PostgreSQL (production planned)
- **Authentication:** JWT (via `djangorestframework-simplejwt`)
- **API Documentation:** Swagger UI & ReDoc (via `drf-yasg`)
- **Containerization:** Docker & Docker Compose (planned)
- **CI/CD:** GitHub Actions (planned)
- **Async & Caching:** Celery, RabbitMQ, Redis (planned)
- **GraphQL API:** Graphene-Django (planned)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Stev1000/alx-project-nexus.git
cd alx-project-nexus

1. Create and Activate Virtual Environment

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Install Dependencies

pip install -r requirements.txt

4. Run Migrations

python manage.py makemigrations
python manage.py migrate

5. Create Superuser

python manage.py createsuperuser

6. Run Development Server

python manage.py runserver

🔑 API Documentation
Swagger UI: http://127.0.0.1:8000/swagger/

ReDoc: http://127.0.0.1:8000/redoc/

Use the Authorize button (🔒) in Swagger to add my JWT token:

Bearer <your_access_token>

📊 Admin Dashboard
URL: http://127.0.0.1:8000/admin/
Manage Users, Products, Categories, Carts, Orders, Payments, Reviews with filters, search, and inline editing.

📂 Project Structure

alx-project-nexus/
│
├── ecommerce_backend/        # Project settings
├── users/                    # Custom user model + JWT auth
├── products/                 # Categories & Products
├── carts/                    # Cart & CartItem
├── orders/                   # Orders & OrderItem
├── payments/                 # Payments
├── reviews/                  # Product reviews
└── requirements.txt

🧪 Example Workflow (Swagger or Postman)

Register/Login → get JWT tokens.

Authorize using access token.

Add products (POST /products/).

Add to cart (POST /cart/add/).

Place order (POST /orders/place/).

Make payment (POST /payments/pay/).

Track orders (GET /orders/my-orders/).

Leave review (POST /reviews/).

✨ Author

👤 Steven Nsanzabandi Gasasira

GitHub: Stev1000

LinkedIn: Steven Nsanzabandi

📜 License

This project is licensed under the BSD License. See the LICENSE file for details.


---

✅ This version highlights what’s already solid, and also markets my repo as an **advanced project roadmap** (with Celery, Redis, GraphQL, Docker, CI/CD, monitoring). It shows employers/mentors that i am thinking like a **production engineer**.  



