def get_response(user):
    user = user.lower().strip()

    responses = {
        "hi": "👋 Hello! Welcome.",
        "hello": "👋 Hi! How can I help you?",
        "hey": "👋 Hey there!",
        "how are you": "😊 I'm doing great. Thanks for asking!",
        "what is your name": "🤖 My name is RuleBot.",
        "who created you": "I was created by an AI Intern.",
        "what is ai": "Artificial Intelligence enables machines to think and solve problems like humans.",
        "python": "Python is one of the most popular programming languages.",
        "java": "Java is an object-oriented programming language.",
        "html": "HTML is used to create webpages.",
        "css": "CSS is used to style webpages.",
        "javascript": "JavaScript makes webpages interactive.",
        "bye": "👋 Goodbye! Have a nice day.",
        "exit": "👋 Goodbye!",
        "thanks": "😊 You're welcome!",
        "thank you": "😊 Happy to help!"
    }

    if user == "help":
        return """
### Available Commands

- hi
- hello
- hey
- how are you
- what is your name
- who created you
- what is ai
- python
- java
- html
- css
- javascript
- thanks
- bye
"""

    return responses.get(user, "❌ Sorry, I don't understand. Type **help** to see available commands.")