# StudyPlanner -- Cybersecurity Project

## 1. Project Description

StudyPlanner is a web application developed with Django that allows
users to manage their exams.

Users can log in with their username and password and access their
personal area, where they can:

-   View their exams, including course name, date, time and description.
-   Add new exams.
-   Delete existing exams.
-   Search for exams by course name.

This project was developed for the Cybersecurity course at the
University of Helsinki. It contains five intentional security
vulnerabilities based on the **OWASP Top 10 (2021)**. Each vulnerability
is demonstrated and a corresponding fix is included in the code.

## 2. Technologies

-   Python
-   Django
-   SQLite
-   HTML
-   python-dotenv

## 3. Installation

Clone the repository:

``` bash
git clone https://github.com/martalifi/Cybersecurity-University-of-Helsinki.git
cd Cybersecurity-University-of-Helsinki
```

Install the required dependencies:

``` bash
pip install -r requirements.txt
```

Create a `.env` file in the root directory and define the Django secret
key:

``` env
DJANGO_SECRET_KEY=your-secret-key
```

Apply the database migrations:

``` bash
python manage.py migrate
```

## 4. Running the Application

Start the Django development server:

``` bash
python manage.py runserver
```

Open your browser and visit:

http://127.0.0.1:8000/


## 5. Security Vulnerabilities

The project demonstrates five categories from the OWASP Top 10 (2021):

1.  **A01 -- Broken Access Control**
2.  **A02 -- Cryptographic Failures**
3.  **A03 -- Injection (SQL Injection)**
4.  **A07 -- Identification and Authentication Failures**
5.  **A09 -- Security Logging and Monitoring Failures**

The vulnerabilities, their corresponding fixes and screenshots
demonstrating the results before and after applying the fixes are
included in the project.

Screenshots can be found in the `screenshots/` directory.

