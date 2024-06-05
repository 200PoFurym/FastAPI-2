from random import random
from sqlalchemy import func

from .models import Result, Questions
from database import get_db

def get_5_leaders_db():
    db = next(get_db())
    leaders = db.query(Result.user_id).order_by(Result.correct_answer.desc())
    return leaders[:5]

def get_question_db():
    db = next(get_db())
    questions = db.query(Questions).order_by(func.random).limit(20).all()
    # random.shuffle(questions)
    return questions  #[:20]

def add_question_db(main_question, v1, v2, v3, v4, correct_answer):
    db = next(get_db())
    new_question = Questions(main_question=main_question, v1=v1,v2=v2, v3=v3, v4=v4, correct_answer=correct_answer)
    db.add(new_question)
    db.commit()
    return 'Вщпрос успешно добавлен!'
