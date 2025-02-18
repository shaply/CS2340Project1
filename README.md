# CS2340Project1
*GT Movies Store*

GT Movies Store is a web application that offers users a seamless experience for browsing, purchasing, and reviewing movies. Built with Django, this platform provides an intuitive and responsive interface, ensuring accessibility across various devices.

Features
* User Registration and Authentication: Users can create accounts, log in securely, and manage their profiles.
* Movie Browsing and Search: Explore a vast collection of movies with advanced search and filter options.
* Shopping Cart and Order Management: Add movies to a cart, proceed to checkout, and track order history.
* Review System: Write, edit, and delete reviews to share opinions and help others make informed decisions.
* Responsive Design: Optimized for desktops, tablets, and mobile devices.
* Password Reset Functionality: Users can reset their passwords to maintain account security.

Watch our Demo Video (here)[https://www.youtube.com/watch?v=IQyVzN6H_VM]!
```bash
https://www.youtube.com/watch?v=IQyVzN6H_VM
```

Installation

To set up the GT Movies Store locally, follow these steps:

# Clone the Repository:
```bash
git clone https://github.com/shaply/CS2340Project1.git
cd CS2340Project1
```

# Set Up a Virtual Environment:
```bash
python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

# Install Dependencies:
```bash
pip install -r requirements.txt
```

# Apply Migrations:
```bash
python manage.py migrate
```

# Run the Development Server:
```bash
python manage.py runserver
```

# Access the application at 
```bash
http://127.0.0.1:8000/.
```
Deployment

GT Movies Store is deployed on PythonAnywhere. To deploy your own instance:

* Upload Your Code to PythonAnywhere:
* Sign in to your PythonAnywhere account.
* Open a Bash console and clone your repository:
```bash
git clone https://github.com/yourusername/your-repo.git
```
* Set Up a Virtual Environment on PythonAnywhere:
```bash
mkvirtualenv --python=/usr/bin/python3.10 yourenv
```
* Activate the virtual environment and install dependencies:
```bash
workon yourenv
pip install -r requirements.txt
```
* Configure the Web App:
* In the PythonAnywhere dashboard, navigate to the "Web" tab.
* Add a new web app and choose "Manual configuration" with the appropriate Python version.
* Set the virtual environment and project paths.
* Edit the WSGI configuration file to point to your Django project's WSGI application.
* Set Up Static Files and Database:
* Run migrations:
```bash
python manage.py migrate
```
* Collect static files:
```bash
python manage.py collectstatic
```
* Configure static files in the PythonAnywhere "Web" tab.
* Reload the Web App:
* After configuration, reload the web app from the PythonAnywhere dashboard to apply changes.
* For detailed deployment instructions, refer to the PythonAnywhere deployment guide.

# Development Process

Our team followed the Scrum framework, organizing development into two-week sprints and completing approximately ten user stories each week. The Scrum Master assigned tasks via Trello, and team members provided daily progress updates. Post-development, we conducted playtesting sessions to identify and resolve bugs or UI issues.

Initially, we worked on separate branches but faced challenges due to task dependencies. For instance, implementing the review functionality required the prior creation of an index.html page. To address this, we adopted a linear task completion model, with some members focusing on bug fixes and refinements. Regular meetings and daily Discord updates ensured effective communication and progress tracking.

A notable challenge occurred during midterms, leading to scheduling conflicts and inconsistent contributions. Despite this, team member David Gu successfully debugged a major issue in Chapter 9, maintaining our momentum. Retrospective meetings allowed us to reflect on such challenges and refine our approach for smoother collaboration in subsequent sprints.

# Technologies Used

* Backend: Django 5, utilizing the Model-View-Template (MVT) architecture.

* Database: SQLite for development; configurable for other databases in production.

* Frontend: HTML, CSS, JavaScript.

* Deployment: Hosted on PythonAnywhere.

* Version Control: Git and GitHub for code management and collaboration.


# Acknowledgments

We extend our gratitude to all team members for their dedication and hard work. 
