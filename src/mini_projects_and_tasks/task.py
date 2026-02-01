from fastapi import FastAPI,APIRouter

app = FastAPI()

blog_router = APIRouter(prefix="/blogs")

@blog_router.get("/",tags=["Blogs"])
async def list_blogs():
    return [{"blog_id": 1, "title": "My Tech Blog"}, {"blog_id": 2, "title": "Travel Blog"}]

@blog_router.get("/{blog_id}",tags=["Blogs"])
async def get_blog(blog_id: int):
    return {"blog_id": blog_id, "title": f"Blog {blog_id}"}

post_router = APIRouter("/{blog_id}/posts")

@post_router.get("/",tags=["Posts"])
async def list_posts(blog_id: int):
    return [{"post_id": 1, "blog_id": blog_id, "title": "Post 1"}, {"post_id": 2, "blog_id": blog_id, "title": "Post 2"}]

@post_router.get("/{post_id}",tags=["Posts"])
async def get_post(blog_id: int, post_id: int):
    return {"post_id": post_id, "blog_id": blog_id, "title": f"Post {post_id}"}

comment_router = APIRouter(prefix="/{post_id}/comments")

@comment_router.get("/",tags=["Comments"])
async def list_comments(blog_id: int, post_id: int):
    return [{"comment_id": 1, "post_id": post_id, "text": "Comment 1"}, {"comment_id": 2, "post_id": post_id, "text": "Comment 2"}]

@comment_router.get("/{comment_id}",tags=["Comments"])
async def get_comment(blog_id: int, post_id: int, comment_id: int):
    return {"comment_id": comment_id, "post_id": post_id, "text": f"Comment {comment_id} on post {post_id}"}

post_router.include_router(comment_router)

blog_router.include_router(post_router)

app.include_router(blog_router)