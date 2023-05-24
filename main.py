import uvicorn
from fastapi import FastAPI
from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT



posts = [
    {
        "id": 1,
        "title" : "Penguins", 
        "text" : "Penguins are a group of aquatic flightless birds."
    }, 
    {
        "id": 2, 
        "title" : "tigers", 
        "text" : "Tigers are the largest living cat species and a members of the genus Panthera"
    }, 
    {
        "id":3,
        "title": "Koalas", 
        "content": "Koala is arboreal herbivorous marsupial native to Australia"
    }
]

users = []
app = FastAPI()


#1 Get  - For testing
@app.get('/', tags=["Introduction et bienvenue"])
def Hello_World():
    return "Hello World !"


#2 Get Posts
@app.get('/posts', tags=["Tous les posts"])
def get_posts():
    return {"data" : posts}


#3 Get Single post {id}
@app.get('/posts/{id}', tags=["Un post"])
def get_one_post(id: int):
    if id > len(posts):
        return {
            "Erreur": "Ce post n'existe pas"
        }
    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }

#4 Post a blog post [A handler for creating a post]

@app.post('/posts', tags=["posts"])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "data": "Post ajouté !"
    }