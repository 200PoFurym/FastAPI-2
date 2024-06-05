from fastapi import APIRouter
from database.testservice import get_question_db, add_question_db, get_5_leaders_db

test_router = APIRouter(prefix='/test', tags=['API for tests'])

@test_router.get('/questions')
async def get_quest():
    questions = get_question_db()
    return questions
@test_router.post('/add_question')
async def add_quest(main_question: str, v1: str, v2: str, v3: str, v4: str, correct_answer: int):
    question =  add_question_db(main_question, v1, v2, v3, v4, correct_answer)
    return question

@test_router.get('/5leaders')
async def leaders():
    leaders = get_5_leaders_db()
    return leaders