from django.db import migrations
from django.contrib.auth.hashers import make_password
import random


def seed_data(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Question = apps.get_model('qnahub', 'Question')
    Answer = apps.get_model('qnahub', 'Answer')

    # --- Create Users ---
    users = []
    users_data = [
        {'username': 'alice', 'password': 'password123', 'first_name': 'Alice', 'last_name': 'Johnson', 'email': 'alice@example.com'},
        {'username': 'bob', 'password': 'password123', 'first_name': 'Bob', 'last_name': 'Williams', 'email': 'bob@example.com'},
        {'username': 'charlie', 'password': 'password123', 'first_name': 'Charlie', 'last_name': 'Brown', 'email': 'charlie@example.com'},
        {'username': 'diana', 'password': 'password123', 'first_name': 'Diana', 'last_name': 'Miller', 'email': 'diana@example.com'},
        {'username': 'ethan', 'password': 'password123', 'first_name': 'Ethan', 'last_name': 'Davis', 'email': 'ethan@example.com'},
    ]
    for user_data in users_data:
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults={
                'password': make_password(user_data['password']),
                'first_name': user_data['first_name'],
                'last_name': user_data['last_name'],
                'email': user_data['email'],
                'is_staff': False,
                'is_superuser': False,
            }
        )
        users.append(user)

    # --- Questions and Answers Data ---
    qa_data = [
        {
            "question": ("How to vertically align a div?", "I've been struggling with this for hours. I have a parent container and a child div. I want the child to be perfectly centered both horizontally and vertically. I've tried using `margin: auto` and `position: absolute`, but nothing seems to work consistently across browsers. What is the modern, standard way to do this with Flexbox or Grid?"),
            "answers": [
                ("The easiest way is to use Flexbox. Just apply `display: flex`, `justify-content: center`, and `align-items: center` to the parent container.", True),
                ("CSS Grid is also a great option! On the parent container, use `display: grid` and `place-items: center`. It's very concise.", False),
            ]
        },
        {
            "question": ("What is the difference between `let`, `const`, and `var` in JavaScript?", "I'm new to modern JavaScript and I see these three keywords used for variable declarations. What are the key differences in terms of scope and mutability? When should I use each one?"),
            "answers": [
                ("`var` is function-scoped and can be re-declared and updated. `let` is block-scoped, can be updated but not re-declared. `const` is block-scoped and cannot be re-declared or updated (for primitive values). Generally, prefer `const`, then `let`, and avoid `var`.", True)
            ]
        },
        {
            "question": ("How to pass props from a parent to a deeply nested child component in React?", "I have a component tree that is 5 levels deep. Passing props down through every single component seems inefficient and makes the code messy. Is there a better way to manage this kind of state, like using Context API or a state management library like Zustand?"),
            "answers": [
                ("This is a classic problem called 'prop drilling'. The React Context API is designed specifically for this. You create a context, provide a value at a high level in the component tree, and any component deep down can consume it without props being passed through intermediate components.", False)
            ]
        },
        {"question": ("What are Django signals?", "I've heard about signals in Django but I don't quite understand what they are or when to use them. Can someone explain?"), "answers": []},
        {"question": ("How to handle asynchronous operations in Python?", "What is the best way to handle async tasks in a Python backend? I'm looking at asyncio, Celery, and other options."), "answers": []},
        {"question": ("Best practices for REST API design?", "What are some key principles to follow when designing a RESTful API to ensure it's scalable and easy to use?"), "answers": [("Use nouns for resource URLs (e.g., /users), use HTTP verbs correctly (GET, POST, PUT, DELETE), and version your API (e.g., /api/v1/users).", False)]},
        {"question": ("How does the CSS Box Model work?", "Can someone explain the components of the CSS box model (margin, border, padding, content)?"), "answers": []},
        {"question": ("What is a closure in JavaScript?", "I'm having a hard time grasping the concept of closures. What's a simple explanation?"), "answers": []},
        {"question": ("How to set up a virtual environment in Python?", "What are the commands to create and activate a virtual environment using `venv`?"), "answers": [("To create: `python -m venv myenv`. To activate on Windows: `myenv\\Scripts\\activate`. On Mac/Linux: `source myenv/bin/activate`.", True)]},
        {"question": ("Difference between SQL and NoSQL databases?", "When would I choose a NoSQL database like MongoDB over a traditional SQL database like PostgreSQL?"), "answers": []},
        {"question": ("How to use Git for version control?", "I'm a beginner. What are the basic Git commands I need to know to start working on a project with a team?"), "answers": []},
        {"question": ("What is the purpose of a `Dockerfile`?", "I see `Dockerfile` in many projects. What does it do and why is it important for deployment?"), "answers": []},
        {"question": ("How to secure a web application?", "What are the most common security vulnerabilities (like XSS, CSRF) and how can I protect my Django app against them?"), "answers": []},
        {"question": ("What are Python decorators?", "The `@` syntax in Python is confusing. How do decorators work and what are they used for?"), "answers": [("A decorator is a function that takes another function as an argument, adds some functionality, and then returns the modified function. It's a way to wrap a function in another function.", False)]},
        {"question": ("How to center an image horizontally and vertically?", "I'm trying to center an image inside a div. What's the most reliable CSS method?"), "answers": []},
        {"question": ("What is the event loop in Node.js?", "I hear about the event loop all the time in the context of Node.js. How does it enable non-blocking I/O?"), "answers": []},
        {"question": ("How to make a responsive navigation bar?", "What's a good approach to create a navbar that collapses into a hamburger menu on mobile devices?"), "answers": []},
        {"question": ("What are CSS preprocessors like Sass or Less?", "Are they still relevant with modern CSS features like custom properties (variables)?"), "answers": []},
        {"question": ("How to deploy a Django project to production?", "What are the steps to take a Django project from my local machine to a live server? What services are recommended?"), "answers": []},
        {"question": ("What is Object-Relational Mapping (ORM)?", "How does Django's ORM work and what are its advantages over writing raw SQL queries?"), "answers": [("An ORM, like Django's, lets you interact with your database using an object-oriented paradigm. You define models as Python classes, and the ORM translates your Python code (e.g., `User.objects.all()`) into SQL queries. This improves developer productivity and database portability.", False)]},
    ]

    # --- Create Questions and Answers ---
    for item in qa_data:
        question_data = item['question']
        answers_data = item['answers']

        # Create Question
        question = Question.objects.create(
            author=random.choice(users),
            title=question_data[0],
            content=question_data[1]
        )

        # Create Answers
        for answer_data in answers_data:
            Answer.objects.create(
                question=question,
                author=random.choice(users),
                content=answer_data[0],
                accepted=answer_data[1]
            )


def unseed_data(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Question = apps.get_model('qnahub', 'Question')
    Answer = apps.get_model('qnahub', 'Answer')

    # Delete questions and answers created by the seed users
    seed_usernames = ['alice', 'bob', 'charlie', 'diana', 'ethan']
    Question.objects.filter(author__username__in=seed_usernames).delete()
    Answer.objects.filter(author__username__in=seed_usernames).delete()

    # Optionally, delete the seed users themselves
    User.objects.filter(username__in=seed_usernames).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('qnahub', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data, unseed_data),
    ]