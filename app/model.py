from pydantic import BaseModel, EmailStr, Field

class PostSchema(BaseModel):
 id : int = Field(default=None)
 title : str = Field(default=None)
 content : str = Field(default=None)
 class Config:
  schema_extra = {
   "post_demo": {
    "title": "Some title about animals",
    "content": "Some content bout animals"
   }
  }



#Schema de données pour l'utilisateur
class UserSchema(BaseModel):
 fullname : str = Field(default=None)
 email : EmailStr = Field(default=None)
 password : str = Field(default=None)
 class config:
  the_schema = {
   "user_demo": {
    "name" : "Bio", 
    "eamil" : "biok8990@gmail.com", 
    "passswrod" : "123"
   }
  }


#Schema de données pour le Login User
class UserLoginSchema(BaseModel):
 email : EmailStr = Field(default=None)
 password : str = Field(default=None)
 class config:
  the_schema = {
   "user_demo": {
    "eamil" : "biok8990@gmail.com", 
    "passswrod" : "123"
   }
  }