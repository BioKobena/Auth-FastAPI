import uvicorn
from fastapi import FastAPI, Body, Depends
from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer


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

@app.post('/posts', dependencies=[Depends(jwtBearer())], tags=["posts"])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "data": "Post ajouté !"
    }



#5 User Signup [ Create a new user ]
@app.post("/user/signup", tags=["user"])
def user_signup(user : UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

def check_user(data : UserSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        else: return False

@app.post('/user/login', tags=["user"])
def user_login(user : UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else: return {"Error" : "Login invalide !"}