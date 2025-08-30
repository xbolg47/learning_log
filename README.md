# Learning Log

A Django web application that helps you track your learning journey. Keep a personal log of topics you're studying and record what you've learned about each topic.

## Features

- **User Authentication**: Register, login, and logout functionality
- **Personal Topics**: Create and manage learning topics that are private to your account
- **Learning Entries**: Add detailed entries about what you've learned for each topic
- **Entry Management**: Edit existing entries to update your learning progress
- **Responsive Design**: Bootstrap-styled interface that works on all devices

## Technology Stack

- **Backend**: Django 5.2.4
- **Database**: SQLite3
- **Frontend**: HTML, CSS, Bootstrap 5
- **Authentication**: Django's built-in user authentication system

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd learning_log
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv ll_env
   ll_env\Scripts\activate  # On Windows
   # source ll_env/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   Open your browser and go to `http://127.0.0.1:8000/`

## Usage

1. **Register**: Create a new account or login with existing credentials
2. **Add Topics**: Create topics for subjects you want to learn about
3. **Add Entries**: Record what you've learned about each topic
4. **Edit Entries**: Update your learning entries as you progress
5. **View Progress**: Browse through your topics and entries to track your learning journey

## Project Structure

```
learning_log/
├── accounts/           # User authentication app
├── learning_logs/      # Main application logic
│   ├── models.py      # Topic and Entry models
│   ├── views.py       # Application views
│   ├── forms.py       # Django forms
│   └── templates/     # HTML templates
├── ll_project/        # Django project settings
├── ll_env/           # Virtual environment
├── db.sqlite3        # SQLite database
├── requirements.txt   # Project dependencies
└── manage.py         # Django management script
```

## Models

- **Topic**: Represents a learning topic with title, creation date, and owner
- **Entry**: Represents a learning entry linked to a topic with content and date

## Security Features

- User authentication required for all learning log operations
- Users can only view and edit their own topics and entries
- CSRF protection enabled
- Secure password validation

## Development

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests (if available)
5. Submit a pull request

## License

This project is for educational purposes.