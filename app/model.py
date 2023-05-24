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
