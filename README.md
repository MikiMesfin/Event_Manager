# Event Management System

A robust Django REST Framework-based event management system with JWT authentication and comprehensive API documentation.

## 🚀 Features

- JWT Authentication
- REST API
- Event Management
- Rate Limiting
- API Documentation with Spectacular
- CORS Support
- Security Best Practices

## 🛠️ Technologies

- Python 3.12+
- Django 5.1+
- Django REST Framework
- SimpleJWT
- Django CORS Headers
- DRF Spectacular
- Django Filters

## 📋 Prerequisites

- Python 3.12 or higher
- pip (Python package manager)
- virtualenv (recommended)

## 🔧 Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd event-management
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create `.env` file:
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## 🔒 Security Features

- CSRF Protection
- JWT Authentication
- Rate Limiting
- Secure Cookie Configuration
- CORS Configuration
- XSS Protection
- HSTS Support

## 📚 API Documentation

Access the API documentation at:
- Swagger UI: `/api/schema/swagger-ui/`
- ReDoc: `/api/schema/redoc/`

## 🧪 Running Tests

```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⚠️ Security

If you discover any security-related issues, please email security@yourdomain.com instead of using the issue tracker.

## 📦 Project Structure

```
event_management/
├── api/                # API endpoints and views
├── core/              # Core application functionality
├── events/            # Event management app
├── tests/             # Test suite
├── static/            # Static files
├── templates/         # HTML templates
└── event_management/  # Project settings
```

## 🔧 Environment Variables

Required environment variables:
- `SECRET_KEY`: Django secret key
- `DEBUG`: Debug mode (True/False)
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DATABASE_URL`: Database connection string
- `CORS_ALLOWED_ORIGINS`: Allowed CORS origins

## 📝 Additional Notes

- Make sure to update your `SECRET_KEY` in production
- Set `DEBUG=False` in production
- Configure proper CORS settings for production
- Set up proper SSL/TLS in production
