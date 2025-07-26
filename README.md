# Task Management System

A comprehensive task management system built with Django and Django REST Framework, featuring JWT authentication, PostgreSQL database, and RESTful APIs for efficient daily task management.

## 🚀 Features

### Core Functionality
- **Task CRUD Operations**: Create, read, update, and delete tasks
- **Task Status Tracking**: Pending, In Progress, Completed
- **Priority Levels**: Low, Medium, High, Urgent
- **Due Date Management**: Set and track task deadlines
- **User Authentication**: Secure JWT-based authentication
- **User Isolation**: Users can only access their own tasks

### Advanced Features
- **Search & Filter**: Search tasks by title/description, filter by status and priority
- **Sorting**: Order tasks by creation date, due date, or priority
- **Pagination**: Efficient handling of large task lists
- **Task Statistics**: Overview dashboard with task distribution
- **Quick Status Updates**: Dedicated endpoint for rapid status changes
- **Data Validation**: Comprehensive input validation and error handling

## 🛠️ Technology Stack

- **Backend**: Django 4.2.7, Django REST Framework 3.14.0
- **Database**: PostgreSQL
- **Authentication**: JWT (djangorestframework-simplejwt)
- **API Documentation**: RESTful API design
- **Environment Management**: python-decouple
- **CORS**: django-cors-headers for frontend integration

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL 12+
- pip (Python package manager)
- Virtual environment (recommended)

## 🔧 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/task-management-system.git
cd task-management-system
```

### 2. Create Virtual Environment
```bash
python -m venv task_management_env
source task_management_env/bin/activate  # On Windows: task_management_env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
Create a PostgreSQL database:
```bash
createdb task_management
```

### 5. Environment Configuration
Create a `.env` file in the project root:
```env
# Database Configuration
DB_NAME=task_management
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

# Django Configuration
SECRET_KEY=your-very-secret-key-here
DEBUG=True
```

### 6. Run Migrations
```bash
python manage.py makemigrations
python manage.py makemigrations users
python manage.py makemigrations tasks
python manage.py migrate
```

### 7. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 8. Start Development Server
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

## 📚 API Documentation

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register/` | User registration |
| POST | `/api/auth/login/` | User login (get JWT tokens) |
| POST | `/api/auth/token/refresh/` | Refresh JWT token |
| GET | `/api/auth/profile/` | Get user profile |
| PUT | `/api/auth/profile/` | Update user profile |

### Task Management Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks/` | List all user tasks |
| POST | `/api/tasks/` | Create new task |
| GET | `/api/tasks/{id}/` | Get specific task |
| PUT | `/api/tasks/{id}/` | Update specific task |
| PATCH | `/api/tasks/{id}/` | Partially update task |
| DELETE | `/api/tasks/{id}/` | Delete specific task |
| GET | `/api/tasks/statistics/` | Get task statistics |
| PATCH | `/api/tasks/{id}/status/` | Update task status only |

### Query Parameters for Task List

- `status`: Filter by status (`pending`, `in_progress`, `completed`)
- `priority`: Filter by priority (`low`, `medium`, `high`, `urgent`)
- `search`: Search in title and description
- `ordering`: Sort by field (`created_at`, `-created_at`, `due_date`, `-due_date`, `priority`, `-priority`)

## 🔐 Authentication

Include JWT token in request headers:
```
Authorization: Bearer <your_jwt_token>
```

## 📝 API Usage Examples

### User Registration
```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "securepassword123",
    "password_confirm": "securepassword123",
    "first_name": "Test",
    "last_name": "User"
  }'
```

### User Login
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "securepassword123"
  }'
```

### Create Task
```bash
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_jwt_token>" \
  -d '{
    "title": "Complete project documentation",
    "description": "Write comprehensive documentation for the task management system",
    "priority": "high",
    "due_date": "2024-12-31T23:59:59Z"
  }'
```

### Update Task Status
```bash
curl -X PATCH http://localhost:8000/api/tasks/1/status/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_jwt_token>" \
  -d '{
    "status": "completed"
  }'
```

### Get Task Statistics
```bash
curl -X GET http://localhost:8000/api/tasks/statistics/ \
  -H "Authorization: Bearer <your_jwt_token>"
```

## 🗂️ Project Structure

```
task-management-system/
├── task_management/          # Main project directory
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py
├── tasks/                   # Tasks app
│   ├── models.py            # Task model
│   ├── serializers.py       # API serializers
│   ├── views.py             # API views
│   ├── urls.py              # Task URLs
│   └── admin.py
├── users/                   # Users app
│   ├── serializers.py       # User serializers
│   ├── views.py             # Authentication views
│   └── urls.py              # Authentication URLs
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
├── .gitignore              # Git ignore file
├── manage.py               # Django management script
└── README.md               # Project documentation
```

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

## 🚀 Deployment

### Environment Variables for Production
```env
DEBUG=False
SECRET_KEY=your-production-secret-key
DB_NAME=task_management_prod
DB_USER=prod_user
DB_PASSWORD=secure_production_password
DB_HOST=your-db-host
DB_PORT=5432
```

### Deployment Checklist
- [ ] Set `DEBUG=False` in production
- [ ] Use environment variables for sensitive data
- [ ] Configure static file serving
- [ ] Set up proper database backups
- [ ] Configure logging
- [ ] Use HTTPS in production
- [ ] Set up monitoring and error tracking

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📊 Database Schema

### Task Model
- `id`: Primary key
- `title`: Task title (max 200 chars)
- `description`: Optional task description
- `status`: Task status (pending, in_progress, completed)
- `priority`: Task priority (low, medium, high, urgent)
- `due_date`: Optional due date
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp
- `user`: Foreign key to User model

### User Model
- Django's built-in User model with additional profile fields

## 🔒 Security Features

- JWT token-based authentication
- Password validation
- CORS configuration
- Input sanitization and validation
- User data isolation
- Secure headers configuration

## 📈 Performance Optimizations

- Database indexes on frequently queried fields
- Pagination for large datasets
- Efficient query optimization
- Minimal API response payloads
- Caching-ready architecture

## 🐛 Common Issues & Solutions

### Database Connection Issues
```bash
# Check PostgreSQL service status
sudo systemctl status postgresql

# Restart PostgreSQL
sudo systemctl restart postgresql
```

### Migration Issues
```bash
# Reset migrations (development only)
python manage.py migrate tasks zero
python manage.py migrate users zero
python manage.py migrate

# Or delete migration files and recreate
rm tasks/migrations/00*.py
rm users/migrations/00*.py
python manage.py makemigrations
python manage.py migrate
```

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Email: support@taskmanagement.com
- Documentation: [API Documentation](http://localhost:8000/api/docs/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django and Django REST Framework communities
- PostgreSQL team
- JWT authentication library maintainers
- Open source contributors

---

**Built with ❤️ using Django and Django REST Framework**