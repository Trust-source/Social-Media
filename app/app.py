from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse

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
def get_all_posts(limit: int = None):
    if limit :
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int) -> PostResponse:
     if id not in text_posts:
        raise HTTPException(status_codes = 404, detail = "Post not found")
     return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title":post.title, "content":post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post

@app.delete("/posts/{id}")
def delete_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_codes = 404, detail = "Post not found")
    
