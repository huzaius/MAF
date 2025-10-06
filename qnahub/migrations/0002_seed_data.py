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
                ("`var` is function-scoped and can be re-declared and updated. `let` is block-scoped, can be updated but not re-declared. `const` is block-scoped and cannot be re-declared or updated (for primitive values). Generally, prefer `const`, then `let`, and avoid `var`.", True),
                ("A key thing to remember is that `const` does not make objects or arrays immutable. It only prevents reassignment of the variable itself. You can still change the properties of an object or the elements of an array declared with `const`.", False)
            ]
        },
        {
            "question": ("How to pass props from a parent to a deeply nested child component in React?", "I have a component tree that is 5 levels deep. Passing props down through every single component seems inefficient and makes the code messy. Is there a better way to manage this kind of state, like using Context API or a state management library like Zustand?"),
            "answers": [
                ("This is a classic problem called 'prop drilling'. The React Context API is designed specifically for this. You create a context, provide a value at a high level in the component tree, and any component deep down can consume it without props being passed through intermediate components.", True),
                ("For more complex state, a dedicated state management library like Zustand or Redux Toolkit is often a better choice. They offer more powerful tools for state updates, middleware, and performance optimization that go beyond what Context API provides out of the box.", False)
            ]
        },
        {"question": ("What are Django signals?", "I've heard about signals in Django but I don't quite understand what they are or when to use them. Can someone explain?"), "answers": [
            ("Signals are a way for decoupled applications to get notified when actions occur elsewhere in the framework. For example, the `post_save` signal is sent after a model's `save()` method is called. You can write a function that 'listens' for this signal and performs an action, like creating a user profile automatically when a new user is created.", True),
            ("Be careful with signals! While powerful, they can make code harder to follow because the logic is not explicitly called. For simple, direct relationships (e.g., updating a field on the same model), a custom `save()` method is often clearer. Use signals for actions that need to cross application boundaries.", False)
        ]},
        {"question": ("How to handle asynchronous operations in Python?", "What is the best way to handle async tasks in a Python backend? I'm looking at asyncio, Celery, and other options."), "answers": [
            ("For long-running background tasks that are separate from the web request-response cycle (like sending emails or processing a video), Celery is the industry standard. It uses a message broker (like RabbitMQ or Redis) to manage a queue of tasks and workers to execute them.", True),
            ("For I/O-bound operations within a single web request (like making multiple API calls to external services), `asyncio` with `aiohttp` or `httpx` is a great choice. It allows your application to handle other requests while waiting for the I/O to complete, improving throughput without needing multiple processes.", False)
        ]},
        {"question": ("Best practices for REST API design?", "What are some key principles to follow when designing a RESTful API to ensure it's scalable and easy to use?"), "answers": [
            ("Use nouns for resource URLs (e.g., /users), use HTTP verbs correctly (GET, POST, PUT, DELETE), and version your API (e.g., /api/v1/users).", True),
            ("Provide meaningful HTTP status codes. For example, `201 Created` when a resource is created, `400 Bad Request` for client errors, and `404 Not Found` when a resource doesn't exist. Good error messages are also crucial for a good developer experience.", False)
        ]},
        {"question": ("How does the CSS Box Model work?", "Can someone explain the components of the CSS box model (margin, border, padding, content)?"), "answers": [
            ("Every element on a page is a rectangular box. The box model describes the layers of this box. From the inside out: Content (text, images), Padding (clears an area around the content), Border (a line that goes around the padding and content), and Margin (clears an area outside the border).", True),
            ("A key concept is `box-sizing`. By default, `box-sizing: content-box;` means if you set an element's width, the padding and border are added *on top* of that width. It's often easier to use `box-sizing: border-box;`, which includes padding and border *within* the total width you set.", False)
        ]},
        {"question": ("What is a closure in JavaScript?", "I'm having a hard time grasping the concept of closures. What's a simple explanation?"), "answers": [
            ("A closure is when a function 'remembers' the variables from its outer (enclosing) scope, even after that outer function has finished running. It gives you access to an outer function’s scope from an inner function.", True),
            ("A classic example is a counter function. An outer function creates a `count` variable and returns an inner function. The inner function can increment and return the `count`. Each time you call the inner function, it remembers the last value of `count` because of the closure.", False)
        ]},
        {"question": ("How to set up a virtual environment in Python?", "What are the commands to create and activate a virtual environment using `venv`?"), "answers": [
            ("To create: `python -m venv myenv`. To activate on Windows: `myenv\\Scripts\\activate`. On Mac/Linux: `source myenv/bin/activate`.", True),
            ("It's a good practice to add your virtual environment directory (e.g., `myenv/`) to your project's `.gitignore` file. This prevents the environment's contents from being committed to version control, as other developers will create their own local environments.", False)
        ]},
        {"question": ("Difference between SQL and NoSQL databases?", "When would I choose a NoSQL database like MongoDB over a traditional SQL database like PostgreSQL?"), "answers": [
            ("SQL databases (like PostgreSQL) are relational, with a predefined schema and structured data in tables. They are great for complex queries and ensuring data integrity. NoSQL databases (like MongoDB) are non-relational, often using document-based storage (like JSON), offering flexible schemas and horizontal scalability.", True),
            ("Choose NoSQL when you have unstructured or semi-structured data, need a flexible schema that can evolve quickly, or require massive horizontal scaling. Choose SQL for applications that rely on transactions and strong data consistency, like e-commerce or financial systems.", False)
        ]},
        {"question": ("How to use Git for version control?", "I'm a beginner. What are the basic Git commands I need to know to start working on a project with a team?"), "answers": [
            ("The core workflow is: `git clone <url>` to get the project, `git pull` to get the latest changes, `git checkout -b <new-feature-branch>` to create a new branch, make your changes, then `git add .`, `git commit -m 'Your message'`, and `git push origin <new-feature-branch>` to share your work.", True),
            ("Don't forget `git status`! It's your best friend. It tells you which branch you are on, what files have been modified, and what files are staged for the next commit. Run it often to understand the state of your repository.", False)
        ]},
        {"question": ("What is the purpose of a `Dockerfile`?", "I see `Dockerfile` in many projects. What does it do and why is it important for deployment?"), "answers": [
            ("A `Dockerfile` is a text file that contains instructions for building a Docker image. The image is a lightweight, standalone, executable package that includes everything needed to run an application: code, runtime, system tools, system libraries, and settings.", True),
            ("It's crucial for modern deployment because it solves the 'it works on my machine' problem. By containerizing the application, you ensure that the environment is identical in development, testing, and production, leading to more reliable and predictable deployments.", False)
        ]},
        {"question": ("How to secure a web application?", "What are the most common security vulnerabilities (like XSS, CSRF) and how can I protect my Django app against them?"), "answers": [
            ("Django has built-in protection against many common threats. For example, its template system auto-escapes variables to prevent Cross-Site Scripting (XSS), and it has a middleware for Cross-Site Request Forgery (CSRF) protection. Always use the `{% csrf_token %}` in your forms.", True),
            ("Another major vulnerability is SQL Injection. Django's ORM protects against this by using parameterized queries, which separates the query logic from the data. As long as you use the ORM and don't build raw SQL strings with user input, you are generally safe from this attack vector.", False)
        ]},
        {"question": ("What are Python decorators?", "The `@` syntax in Python is confusing. How do decorators work and what are they used for?"), "answers": [
            ("A decorator is a function that takes another function as an argument, adds some functionality, and then returns the modified function. It's a way to wrap a function in another function.", True),
            ("The `@` syntax is just syntactic sugar. Writing `@my_decorator` above a function `my_function` is equivalent to writing `my_function = my_decorator(my_function)` after the function definition. They are commonly used for logging, timing, and enforcing authentication (like Django's `@login_required`).", False)
        ]},
        {"question": ("How to center an image horizontally and vertically?", "I'm trying to center an image inside a div. What's the most reliable CSS method?"), "answers": [
            ("Using Flexbox on the parent div is the most common and reliable method: `display: flex; justify-content: center; align-items: center;`. This works perfectly for both horizontal and vertical centering.", True),
            ("If the parent div has a defined height, you can also use CSS Grid: `display: grid; place-items: center;`. It's even more concise and achieves the same result.", False)
        ]},
        {"question": ("What is the event loop in Node.js?", "I hear about the event loop all the time in the context of Node.js. How does it enable non-blocking I/O?"), "answers": [
            ("The event loop allows Node.js to perform non-blocking I/O operations, despite JavaScript being single-threaded. When an async operation (like reading a file or a network request) is started, the operation is handed off to the system kernel. The event loop can then process other events. When the async operation completes, a callback is placed in the event queue to be executed.", True),
            ("Think of it like a restaurant kitchen with one chef (the thread). When an order needs a long time to cook (I/O), the chef doesn't just stand and wait. They start the cooking process and move on to other, quicker tasks. When the long-cooking dish is ready, the waiter (event loop) brings it to the chef's attention to be plated (callback execution).", False)
        ]},
        {"question": ("How to make a responsive navigation bar?", "What's a good approach to create a navbar that collapses into a hamburger menu on mobile devices?"), "answers": [
            ("A common approach is to use CSS media queries. Have one set of styles for the full desktop menu (`display: flex`). Then, use a media query like `@media (max-width: 768px)` to hide the desktop menu and show a 'hamburger' icon. The navigation links can be placed in a container that is hidden by default on mobile and shown when the hamburger icon is clicked (usually toggled with JavaScript).", True),
            ("CSS-only solutions are also possible using a hidden checkbox and the `:checked` pseudo-selector. The hamburger icon is the `<label>` for the checkbox. When the checkbox is checked, you use the adjacent sibling combinator (`~`) or general sibling combinator (`+`) to show the navigation menu. This avoids the need for JavaScript for the basic toggle functionality.", False)
        ]},
        {"question": ("What are CSS preprocessors like Sass or Less?", "Are they still relevant with modern CSS features like custom properties (variables)?"), "answers": [
            ("They are still very relevant! While CSS now has variables (custom properties), preprocessors like Sass offer much more, such as mixins (reusable blocks of styles), functions, loops, and nesting, which help in writing more organized, maintainable, and DRY (Don't Repeat Yourself) code.", True),
            ("Nesting is one of the most beloved features. Instead of writing `.navbar .nav-item .nav-link { ... }`, in Sass you can write `.navbar { .nav-item { .nav-link { ... } } }`, which is much more readable and mirrors the HTML structure.", False)
        ]},
        {"question": ("How to deploy a Django project to production?", "What are the steps to take a Django project from my local machine to a live server? What services are recommended?"), "answers": [
            ("A typical production stack includes a WSGI server like Gunicorn to run the Django app, a web server like Nginx to act as a reverse proxy and serve static files, and a process manager like Supervisor or systemd to keep Gunicorn running. For the database, you'd switch from SQLite to something more robust like PostgreSQL.", True),
            ("Platform-as-a-Service (PaaS) options like Heroku, Vercel, or Railway can greatly simplify deployment. You connect your Git repository, configure a few settings, and the platform handles the infrastructure (Gunicorn, Nginx, etc.) for you. It's a great way to get started with production deployments.", False)
        ]},
        {"question": ("What is Object-Relational Mapping (ORM)?", "How does Django's ORM work and what are its advantages over writing raw SQL queries?"), "answers": [
            ("An ORM, like Django's, lets you interact with your database using an object-oriented paradigm. You define models as Python classes, and the ORM translates your Python code (e.g., `User.objects.all()`) into SQL queries. This improves developer productivity and database portability.", True),
            ("A major advantage is database abstraction. You can write your queries in Python once, and Django's ORM can translate them to work with different database backends (like PostgreSQL, MySQL, or SQLite). This makes it much easier to switch databases if needed, without rewriting all your data access logic.", False)
        ]},
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