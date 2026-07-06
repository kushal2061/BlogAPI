# 🧠 BlogApi Project

The BlogApi project is a Django-based RESTful API designed to manage blog posts, categories, and comments. It provides a robust and scalable framework for building blog applications, with features such as user registration, authentication, and authorization. The project utilizes the Django REST framework to define API endpoints, serialize data, and handle HTTP requests.

## 🚀 Features

- User registration and authentication using JSON Web Tokens (JWT)
- CRUD operations for blog posts, categories, and comments
- Filtering and pagination for API responses
- Support for multiple database backends
- Extensive use of Django's built-in features, such as models, views, and templates

## 🛠️ Tech Stack

- **Backend**: Django , Django REST framework
- **Database**: SQLite
- **Authentication**: JSON Web Tokens (JWT) using `rest_framework_simplejwt` 5.2.0
- **Serialization**: Django REST framework's built-in serializers

## 📦 Installation

To install the BlogApi project, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/blog-api.git`
2. Navigate to the project directory: `cd blog-api`
3. Install dependencies: `pip install -r requirements.txt`
4. Create a new database: `python manage.py migrate`
5. Run the development server: `python manage.py runserver`

## 💻 Usage

To use the BlogApi project, follow these steps:

1. Register a new user: `POST /api/v1/users/` with `username`, `email`, and `password` in the request body
2. Obtain a JWT token: `POST /api/v1/token/` with `username` and `password` in the request body
3. Use the JWT token to authenticate API requests: include the token in the `Authorization` header with each request

## 📂 Project Structure

```markdown
.
├── BlogApi
│ ├── **init**.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── blog
│ ├── **init**.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── urls.py
│ └── views.py
├── manage.py
└── requirements.txt
```

## 💖 Thanks Message

Thank you for using the BlogApi project!
