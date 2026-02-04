# Mindgame - Quiz Application

A comprehensive Django-based online quiz platform that allows users to take quizzes, track their performance, and compete on leaderboards. The application provides a complete user management system with authentication, quiz creation, and performance analytics.

## Project Overview

**Mindgame** is a full-featured web application built with Django that enables users to:
- Register and manage user accounts
- Browse and attempt quizzes organized by categories
- Take timed quizzes with multiple-choice questions
- Track their quiz performance and scores
- View detailed statistics and history of quiz attempts
- Compete on leaderboards

## Features

### User Management
- **User Registration**: Create new accounts with email verification
- **User Authentication**: Secure login and logout functionality
- **User Profiles**: View personal quiz statistics and attempt history
- **Custom User Model**: Extended Django's AbstractUser model with email field

### Quiz System
- **Quiz Categories**: Organize quizzes by different categories
- **Quiz Management**: Create and manage quizzes with descriptions and time limits
- **Multiple Choice Questions**: Each quiz contains questions with multiple choice answers
- **Answer Validation**: Automatic scoring based on correct answers
- **Time Limits**: Define time constraints for each quiz
- **Quiz Status**: Active/Inactive quiz management

### Performance Tracking
- **Quiz Attempts**: Track each user's quiz attempts with timestamps
- **Score Recording**: Store total questions and user scores
- **Attempt History**: View complete history of quiz attempts
- **Performance Statistics**: Calculate total quizzes attempted and total score
- **Leaderboards**: Rank users based on performance

## Project Structure

```
quiz/
├── manage.py                  # Django management script
├── db.sqlite3                 # SQLite database
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
│
├── mindgame/                  # Main project configuration
│   ├── settings.py           # Django settings
│   ├── urls.py               # Main URL routing
│   ├── wsgi.py               # WSGI application
│   └── asgi.py               # ASGI application
│
├── account/                   # User account management app
│   ├── models.py             # Custom User model
│   ├── views.py              # Registration, login, profile views
│   ├── urls.py               # Account URL patterns
│   ├── admin.py              # Admin configuration
│   ├── apps.py               # App configuration
│   ├── migrations/           # Database migrations
│   └── __pycache__/          # Cached files
│
├── quiz/                      # Quiz management app
│   ├── models.py             # Quiz, Question, Choice, QuizAttempt models
│   ├── views.py              # Quiz listing, starting, and scoring logic
│   ├── urls.py               # Quiz URL patterns
│   ├── admin.py              # Admin configuration
│   ├── apps.py               # App configuration
│   ├── migrations/           # Database migrations
│   └── __pycache__/          # Cached files
│
├── core/                      # Core functionality app
│   ├── models.py             # Core models
│   ├── views.py              # Home page view
│   ├── urls.py               # Core URL patterns
│   ├── admin.py              # Admin configuration
│   ├── apps.py               # App configuration
│   ├── migrations/           # Database migrations
│   └── __pycache__/          # Cached files
│
├── templates/                 # HTML templates
│   ├── base/
│   │   ├── base.html         # Base template with navigation
│   │   ├── navbar.html       # Navigation bar component
│   │   └── footer.html       # Footer component
│   ├── accounts/
│   │   ├── login.html        # Login page
│   │   ├── register.html     # Registration page
│   │   └── profile.html      # User profile page
│   ├── quiz/
│   │   ├── quiz_list.html    # List of available quizzes
│   │   ├── quiz_detail.html  # Quiz details before starting
│   │   ├── question.html     # Quiz question display
│   │   ├── instruction.html  # Quiz instructions
│   │   ├── result.html       # Quiz results page
│   │   └── leaderboard.html  # Leaderboard display
│   └── core/
│       ├── home.html         # Home page
│       └── dashboard.html    # User dashboard
│
├── static/                    # Static files
│   ├── css/
│   │   └── style.css         # Main stylesheet
│   └── js/
│       └── main.js           # Main JavaScript
│
└── env/                       # Python virtual environment
```

## Data Models

### Account App

#### User Model
- **Extends**: Django's AbstractUser
- **Fields**:
  - `username`: Unique username
  - `email`: Unique email address (extended field)
  - `password`: Hashed password
  - Inherits: first_name, last_name, is_active, is_staff, etc.

### Quiz App

#### Category Model
- `name`: Category name (CharField, max_length=200)
- String representation: Category name

#### Quiz Model
- `category`: ForeignKey to Category
- `title`: Quiz title (CharField, max_length=200)
- `description`: Quiz description (TextField)
- `time_limit`: Time limit in minutes (IntegerField)
- `is_active`: Quiz availability status (BooleanField, default=True)
- String representation: Quiz title

#### Question Model
- `quiz`: ForeignKey to Quiz
- `text`: Question text (TextField)
- `choice_set`: Reverse relation to Choice model
- String representation: Question text

#### Choice Model
- `question`: ForeignKey to Question
- `text`: Choice text (CharField, max_length=200)
- `is_correct`: Correct answer flag (BooleanField, default=False)
- String representation: Choice text

#### QuizAttempt Model
- `user`: ForeignKey to User
- `quiz`: ForeignKey to Quiz
- `total`: Total number of questions (IntegerField)
- `score`: User's score (IntegerField)
- `created_at`: Timestamp of attempt (DateTimeField, auto_now_add=True)
- **Unique Constraint**: One attempt per user per quiz
- String representation: Quiz name, total questions, score, and timestamp

## URL Routing

### Account URLs (`/account/`)
- `login/`: User login page
- `logout/`: User logout
- `register/`: User registration
- `profile/`: User profile and quiz history

### Quiz URLs (`/quiz/`)
- ``: List all active quizzes
- `<id>/`: Quiz details page
- `start/<id>/`: Start quiz and process answers

### Core URLs (`/`)
- ``: Home page
- Additional core functionality routes

## Key Features Explanation

### User Registration & Authentication
- New users can create an account with username, email, and password
- Email uniqueness is enforced
- Passwords are securely hashed using Django's authentication system
- Login redirects to user profile on success

### Quiz Workflow
1. **Browse Quizzes**: Users view all active quizzes on the quiz list page
2. **View Details**: Click on a quiz to see description, time limit, and question count
3. **Start Quiz**: Begin the quiz (requires login)
4. **Answer Questions**: Select answers from multiple choices
5. **Submit Answers**: Form submission triggers automatic scoring
6. **View Results**: See score, total questions, and performance statistics
7. **Prevent Retakes**: Users can only attempt each quiz once

### Scoring System
- Automatic scoring based on selected correct answers
- One point per correct answer
- Results stored in QuizAttempt model with timestamp
- Users cannot retake quizzes (enforced by unique constraint)

### Performance Tracking
- User profile displays all quiz attempts ordered by date
- Statistics include total quizzes attempted and cumulative score
- Each attempt shows quiz name, score, total questions, and date/time

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd quiz
   ```

2. **Create virtual environment**
   ```bash
   python -m venv env
   ```

3. **Activate virtual environment**
   - **Windows**:
     ```bash
     env\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source env/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install django==5.2.10 asgiref sqlparse tzdata
   ```

5. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser for admin access**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Access application**
   - Application: http://localhost:8000
   - Admin Panel: http://localhost:8000/admin

## Usage

### As Administrator
1. Log in to admin panel at `/admin/`
2. Create Categories for organizing quizzes
3. Create Quizzes with descriptions and time limits
4. Add Questions to each quiz
5. Add Choices to each question (mark correct answers)
6. Manage user accounts and quiz attempts

### As User
1. Register for a new account at `/account/register/`
2. Log in at `/account/login/`
3. Browse available quizzes on the home page
4. Click on a quiz to view details and instructions
5. Click "Start Quiz" to begin attempting
6. Select answers for all questions and submit
7. View your score and results immediately
8. Access your profile to see quiz history and statistics

## Technologies Used

- **Backend**: Django 5.2.10 (Python Web Framework)
- **Database**: SQLite3 (Default Django database)
- **Frontend**: HTML, CSS, JavaScript
- **Authentication**: Django's built-in authentication system
- **ORM**: Django ORM for database operations
- **Web Server**: Django development server (use production server like Gunicorn for production)

## Dependencies

```
Django==5.2.10
asgiref==3.11.0
sqlparse==0.5.5
tzdata==2025.3
```

## Configuration

### Settings File (`mindgame/settings.py`)
Key configuration variables:
- `DEBUG = True` (Change to False in production)
- `ALLOWED_HOSTS = []` (Add your domain in production)
- `SECRET_KEY`: Generated security key (change in production)
- `INSTALLED_APPS`: Includes quiz, account, and core apps
- `AUTH_USER_MODEL = "account.User"`: Uses custom user model
- `DATABASES`: SQLite configuration

## Admin Panel Features

The Django admin panel allows administrators to:
- Manage Users: Create, edit, delete user accounts
- Manage Categories: Organize quizzes by topic
- Manage Quizzes: Create and edit quiz parameters
- Manage Questions: Add and edit quiz questions
- Manage Choices: Add answer options and mark correct answers
- Manage Quiz Attempts: View and manage user quiz attempts
- Filter and Search: Find specific quizzes, users, or attempts
- Bulk Actions: Perform operations on multiple items

## Security Considerations

- **Password Security**: All passwords are hashed using Django's PBKDF2 algorithm
- **CSRF Protection**: Cross-Site Request Forgery protection enabled by default
- **SQL Injection Protection**: Django ORM prevents SQL injection attacks
- **Authentication Required**: Login required for quiz attempts
- **Email Uniqueness**: Prevents account duplication

⚠️ **Production Deployment Notes**:
- Set `DEBUG = False` in production
- Change `SECRET_KEY` to a secure random value
- Update `ALLOWED_HOSTS` with your domain
- Use a production database (PostgreSQL recommended)
- Use a production web server (Gunicorn, uWSGI)
- Enable HTTPS/SSL
- Set up proper logging and monitoring

## Future Enhancements

Potential features for future versions:
- Question difficulty levels
- Partial marking for subjective questions
- Real-time leaderboards with ranking
- Quiz statistics and analytics dashboard
- Email notifications for new quizzes
- Timed quiz with automatic submission
- Question randomization
- Multiple quiz attempts with best score tracking
- Certificate generation for quiz completion
- API endpoint for mobile app integration
- Social sharing features
- Quiz recommendations based on performance

## Troubleshooting

### Database Errors
- Run `python manage.py migrate` to ensure all migrations are applied

### Static Files Not Loading
- Run `python manage.py collectstatic` in production
- Check `STATIC_URL` and `STATIC_ROOT` settings

### Login Issues
- Clear browser cache and cookies
- Ensure user is created in the database
- Check if user account is active

### Quiz Scoring Issues
- Verify correct answers are marked in admin panel
- Check browser console for JavaScript errors
- Ensure all questions have at least one choice

## Contributing

When contributing to this project:
1. Create a new branch for your feature
2. Make changes and test thoroughly
3. Write clear commit messages
4. Submit a pull request with description

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or suggestions:
- Create an issue in the repository
- Contact the development team
- Check existing documentation

---

**Last Updated**: February 2026
**Django Version**: 5.2.10
**Python Version**: 3.8+
