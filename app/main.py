from fastapi import FastAPI, Request, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .posts import posts

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", include_in_schema=False, name="home")
@app.get('/posts', include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home"})

@app.get('/post/{post_id}', include_in_schema=False, name="post")
def post(request: Request, post_id: int):
    for post in posts:
        title = post['title'][:50]
        if post.get("id") == post_id:
            return templates.TemplateResponse(request, "post.html", {"post": post, "title": title})
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

@app.get("/api/posts")
def get_posts():
    return posts

@app.get('/api/post/{post_id}')
def get_post(post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return post
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")