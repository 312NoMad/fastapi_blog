from fastapi import FastAPI, Depends, Request
from fastapi.responses import Response
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from db import Post, get_db
from models import PostBase, PostCreate


app = FastAPI()


templates = Jinja2Templates('templates')


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})




@app.post('/create/', response_model=PostCreate)
def create_post(post_data: PostBase, db: Session = Depends(get_db)):
    post = Post(**post_data.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
