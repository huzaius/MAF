
document.addEventListener('DOMContentLoaded', () => {

    // --- Mock Data ---
    let questions = [
        { id: 1, author: { name: 'Alice Johnson', avatar: 'https://placehold.co/40x40/7e22ce/ffffff?text=AJ' }, title: 'How to vertically align a div?', content: 'I\'ve been struggling with this for hours. I have a parent container and a child div. I want the child to be perfectly centered both horizontally and vertically. I\'ve tried using `margin: auto` and `position: absolute`, but nothing seems to work consistently across browsers. What is the modern, standard way to do this with Flexbox or Grid?', tags: ['css', 'flexbox', 'layout'], upvotes: 128, downvotes: 3, answersCount: 2, timestamp: '2024-08-21T14:30:00Z', answers: [ { id: 101, author: { name: 'Bob Williams', avatar: 'https://placehold.co/40x40/16a34a/ffffff?text=BW' }, content: 'The easiest way is to use Flexbox. Just apply `display: flex`, `justify-content: center`, and `align-items: center` to the parent container.', upvotes: 95, downvotes: 1, accepted: true, timestamp: '2024-08-21T14:35:00Z' }, { id: 102, author: { name: 'Charlie Brown', avatar: 'https://placehold.co/40x40/be123c/ffffff?text=CB' }, content: 'CSS Grid is also a great option! On the parent container, use `display: grid` and `place-items: center`. It\'s very concise.', upvotes: 42, downvotes: 0, accepted: false, timestamp: '2024-08-21T14:40:00Z' } ] },
        { id: 2, author: { name: 'Diana Miller', avatar: 'https://placehold.co/40x40/b45309/ffffff?text=DM' }, title: 'What is the difference between `let`, `const`, and `var` in JavaScript?', content: 'I\'m new to modern JavaScript and I see these three keywords used for variable declarations. What are the key differences in terms of scope and mutability? When should I use each one?', tags: ['javascript', 'es6', 'scope'], upvotes: 256, downvotes: 5, answersCount: 0, timestamp: '2024-08-20T10:15:00Z', answers: [] },
        { id: 3, author: { name: 'Ethan Davis', avatar: 'https://placehold.co/40x40/0369a1/ffffff?text=ED' }, title: 'How to pass props from a parent to a deeply nested child component in React?', content: 'I have a component tree that is 5 levels deep. Passing props down through every single component seems inefficient and makes the code messy. Is there a better way to manage this kind of state, like using Context API or a state management library like Zustand?', tags: ['react', 'state-management', 'context-api'], upvotes: 98, downvotes: 1, answersCount: 3, timestamp: '2024-08-19T09:00:00Z', answers: [] }
    ];

    // --- DOM Elements ---
    const questionListView = document.getElementById('question-list-view');
    const questionPageView = document.getElementById('question-page-view');
    const questionListContainer = document.getElementById('question-list-container');
    const sortDropdown = document.getElementById('dropdown');
    const sortDropdownButton = document.getElementById('dropdownDefaultButton');

    // --- Helper Functions ---
    const timeAgo = (date) => {
        const seconds = Math.floor((new Date() - new Date(date)) / 1000);
        let interval = seconds / 31536000;
        if (interval > 1) return `${Math.floor(interval)} years ago`;
        interval = seconds / 2592000;
        if (interval > 1) return `${Math.floor(interval)} months ago`;
        interval = seconds / 86400;
        if (interval > 1) return `${Math.floor(interval)} days ago`;
        interval = seconds / 3600;
        if (interval > 1) return `${Math.floor(interval)} hours ago`;
        interval = seconds / 60;
        if (interval > 1) return `${Math.floor(interval)} minutes ago`;
        return `${Math.floor(seconds)} seconds ago`;
    };

    // --- Sorting Logic ---
    function sortQuestions(criteria) {
        switch (criteria) {
            case 'votes':
                questions.sort((a, b) => (b.upvotes - b.downvotes) - (a.upvotes - a.downvotes));
                sortDropdownButton.firstChild.textContent = 'Sort by: Most Voted ';
                break;
            case 'answers':
                questions.sort((a, b) => b.answersCount - a.answersCount);
                sortDropdownButton.firstChild.textContent = 'Sort by: Most Answered ';
                break;
            case 'newest':
            default:
                questions.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
                sortDropdownButton.firstChild.textContent = 'Sort by: Newest ';
                break;
        }
        renderQuestionList();
    }

    // --- Render Functions ---
    
    function renderQuestionList() {
        questionListContainer.innerHTML = ''; // Clear previous list
        questions.forEach(q => {
            const questionElement = document.createElement('div');
            // Using Flowbite's card styling
            questionElement.className = 'block p-6 bg-white border border-gray-200 rounded-lg shadow-sm hover:border-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:hover:border-blue-500 cursor-pointer transition-colors';
            questionElement.dataset.questionId = q.id;

            const tagsHtml = q.tags.map(tag => `<span class="bg-blue-100 text-blue-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full dark:bg-blue-900 dark:text-blue-300">${tag}</span>`).join('');

            questionElement.innerHTML = `
                <div class="flex space-x-6">
                    <div class="flex flex-col items-center text-center w-24">
                        <div class="text-2xl font-bold text-gray-800 dark:text-gray-200">${q.upvotes - q.downvotes}</div>
                        <div class="text-sm text-gray-500 dark:text-gray-400">votes</div>
                        <div class="mt-4 text-2xl font-bold text-gray-800 dark:text-gray-200">${q.answersCount}</div>
                        <div class="text-sm text-gray-500 dark:text-gray-400">answers</div>
                    </div>
                    <div class="flex-1">
                        <h3 class="text-xl font-semibold text-blue-600 dark:text-blue-400 mb-2">${q.title}</h3>
                        <p class="text-gray-600 dark:text-gray-300 line-clamp-2 mb-4">${q.content}</p>
                        <div class="flex justify-between items-center">
                            <div class="flex flex-wrap gap-2">${tagsHtml}</div>
                            <div class="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400">
                                <img class="w-10 h-10 rounded-full object-cover border-2 border-white dark:border-gray-800" src="${q.author.avatar}" alt="${q.author.name}">
                                <span>${q.author.name}</span>
                                <span>asked ${timeAgo(q.timestamp)}</span>
                            </div>
                        </div>
                    </div>
                </div>
            `;
            questionElement.addEventListener('click', () => showQuestionPage(q.id));
            questionListContainer.appendChild(questionElement);
        });
    }

    function renderQuestionPage(question) {
        const tagsHtml = question.tags.map(tag => `<span class="bg-blue-100 text-blue-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full dark:bg-blue-900 dark:text-blue-300">${tag}</span>`).join('');
        
        const answersHtml = question.answers.sort((a,b) => b.accepted - a.accepted).map(answer => `
            <div class="block p-6 bg-white border ${answer.accepted ? 'border-green-500 bg-green-50 dark:bg-green-900/20' : 'border-gray-200 dark:border-gray-700'} rounded-lg shadow-sm dark:bg-gray-800">
                <div class="flex space-x-6">
                    <div class="flex flex-col items-center">
                        <button class="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-700"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m18 15-6-6-6 6"/></svg></button>
                        <span class="text-xl font-bold text-gray-800 dark:text-gray-200">${answer.upvotes - answer.downvotes}</span>
                        <button class="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-700"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg></button>
                        ${answer.accepted ? '<div class="mt-4" title="Accepted Answer"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-green-600"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg></div>' : ''}
                    </div>
                    <div class="flex-1">
                        <div class="prose dark:prose-invert max-w-none"><p>${answer.content}</p></div>
                        <div class="mt-6 flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400">
                            <img class="w-10 h-10 rounded-full object-cover border-2 border-white dark:border-gray-800" src="${answer.author.avatar}" alt="${answer.author.name}">
                            <div>
                                <div>answered by <span class="font-medium">${answer.author.name}</span></div>
                                <div>on ${new Date(answer.timestamp).toLocaleDateString()}</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `).join('');

        questionPageView.innerHTML = `
            <div class="space-y-8">
                <div>
                    <button id="back-to-questions-btn" type="button" class="text-gray-900 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-100 font-medium rounded-lg text-sm px-5 py-2.5 mb-6 dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700">&larr; Back to Questions</button>
                    <div class="block p-6 bg-white border border-gray-200 rounded-lg shadow-sm dark:bg-gray-800 dark:border-gray-700">
                        <div class="flex space-x-6">
                            <div class="flex flex-col items-center space-y-2">
                                <button class="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-700"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m18 15-6-6-6 6"/></svg></button>
                                <span class="text-xl font-bold text-gray-800 dark:text-gray-200">${question.upvotes - question.downvotes}</span>
                                <button class="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-700"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg></button>
                            </div>
                            <div class="flex-1">
                                <h1 class="text-3xl font-bold text-gray-900 dark:text-white mb-4">${question.title}</h1>
                                <div class="prose dark:prose-invert max-w-none mb-6"><p>${question.content}</p></div>
                                <div class="flex flex-wrap gap-2 mb-6">${tagsHtml}</div>
                                <div class="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400">
                                    <img class="w-10 h-10 rounded-full object-cover border-2 border-white dark:border-gray-800" src="${question.author.avatar}" alt="${question.author.name}">
                                    <div>
                                        <div>asked by <span class="font-medium">${question.author.name}</span></div>
                                        <div>on ${new Date(question.timestamp).toLocaleDateString()}</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white">${question.answers.length} Answers</h2>
                <div class="space-y-6">${answersHtml}</div>
                <div>
                    <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-4">Your Answer</h2>
                    <div class="block p-6 bg-white border border-gray-200 rounded-lg shadow-sm dark:bg-gray-800 dark:border-gray-700">
                        <textarea rows="6" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white" placeholder="Write your detailed answer here..."></textarea>
                        <div class="mt-4 flex justify-end">
                            <button type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Post Your Answer</button>
                        </div>
                    </div>
                </div>
            </div>
        `;
        document.getElementById('back-to-questions-btn').addEventListener('click', showQuestionList);
    }

    // --- View Navigation ---
    function showQuestionList() {
        questionPageView.classList.add('hidden');
        questionListView.classList.remove('hidden');
    }

    function showQuestionPage(questionId) {
        const question = questions.find(q => q.id === questionId);
        if (question) {
            renderQuestionPage(question);
            questionListView.classList.add('hidden');
            questionPageView.classList.remove('hidden');
            window.scrollTo(0, 0);
        }
    }
    
    // --- Event Listeners ---
    sortDropdown.addEventListener('click', (e) => {
        if (e.target.tagName === 'A' && e.target.dataset.sort) {
            e.preventDefault();
            sortQuestions(e.target.dataset.sort);
        }
    });

    // --- Initial Render ---
    sortQuestions('newest'); // Default sort
});
