from fastapi import FastAPI 

app = FastAPI()

text_posts = {
    1: {"title": "New Post", "content": "Cool test post"},
    2: {"title": "Getting Started with FastAPI", "content": "FastAPI makes building APIs fast and fun."},
    3: {"title": "Why I Love SQLite", "content": "A whole database in a single file, no server needed."},
    4: {"title": "Debugging Tips", "content": "Read the last line of the traceback first."},
    5: {"title": "Weekend Project Ideas", "content": "Build a small budget tracker or a notes app."},
    6: {"title": "Understanding Sessions", "content": "A session is a short trip to the database: add, commit, done."},
    7: {"title": "Python Type Hints", "content": "Type hints help your editor catch mistakes before you run the code."},
    8: {"title": "Lagos Tech Meetup Recap", "content": "Great talks on backend development and APIs."},
    9: {"title": "Learning in Public", "content": "Sharing what you learn helps you remember it."},
    10: {"title": "Final Test Post", "content": "If you can read this, your endpoint works."},
}

@app.get("/posts")
def get_all_posts():
    return text_posts
 