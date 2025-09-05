uv init MAF
cd MAF
uv add django
uv django-admin startproject MAsjidFarouk .
uv django-admin startapp QNAHub


 questions = [
        {'id': 1, 'author': {'name': 'Alice Johnson', 'avatar': 'https://placehold.co/40x40/7e22ce/ffffff?text=AJ'}, 'title': 'How to vertically align a div?', 'content': 'I\'ve been struggling with this for hours. I have a parent container and a child div. I want the child to be perfectly centered both horizontally and vertically. I\'ve tried using `margin: auto` and `position: absolute`, but nothing seems to work consistently across browsers. What is the modern, standard way to do this with Flexbox or Grid?', 'tags': ['css', 'flexbox', 'layout'], 'upvotes': 128, 'downvotes': 3, 'answersCount': 2, 'timestamp': '2024-08-21T14:30:00Z', 'answers': [{'id': 101, 'author': {
            'name': 'Bob Williams', 'avatar': 'https://placehold.co/40x40/16a34a/ffffff', 'name': 'Bob Williams'}, 'content': 'The easiest way is to use Flexbox. Just apply `display: flex`, `justify-content: center`, and `align-items: center` to the parent container.', 'upvotes': 95, 'downvotes': 1, 'accepted': True, 'timestamp': '2024-08-21T14:35:00Z'}, {'id': 102, 'author': {'name': 'Charlie Brown', 'avatar': 'https://placehold.co/40x40/be123c/ffffff', 'name': 'Charlie Brown'}, 'content': 'CSS Grid is also a great option! On the parent container, use `display: grid` and `place-items: center`. It\'s very concise.', 'upvotes': 42, 'downvotes': 0, 'accepted': False, 'timestamp': '2024-08-21T14:40:00Z'}]},
        {'id': 2, 'author': {'name': 'Diana Miller', 'avatar': 'https://placehold.co/40x40/b45309/ffffff?text=DM'}, 'title': 'What is the difference between `let`, `const`, and `var` in JavaScript?',
            'content': 'I\'m new to modern JavaScript and I see these three keywords used for variable declarations. What are the key differences in terms of scope and mutability? When should I use each one?', 'tags': ['javascript', 'es6', 'scope'], 'upvotes': 256, 'downvotes': 5, 'answersCount': 0, 'timestamp': '2024-08-20T10:15:00Z', 'answers': []},
        {'id': 3, 'author': {'name': 'Ethan Davis', 'avatar': 'https://placehold.co/40x40/0369a1/ffffff?text=ED'}, 'title': 'How to pass props from a parent to a deeply nested child component in React?',
            'content': 'I have a component tree that is 5 levels deep. Passing props down through every single component seems inefficient and makes the code messy. Is there a better way to manage this kind of state, like using Context API or a state management library like Zustand?', 'tags': ['react', 'state-management', 'context-api'], 'upvotes': 98, 'downvotes': 1, 'answersCount': 3, 'timestamp': '2024-08-19T09:00:00Z', 'answers': []}
    ]