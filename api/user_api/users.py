from fastapi import APIRouter
from database.userservice import get_all_users_db, user_answer_db, plus_point_db, register_user_db

user_router = APIRouter(prefix='/user', tags=['API FOR USERS'])
@user_router.get('/all-users')
async def all_users():
    return get_all_users_db()
@user_router.post('/register')
async def register(name: str, phone_number: int, level: str):
    reg = register_user_db(name, phone_number, level)
    return reg

@user_router.post('/answer-done')
async def get_leaders(user_id: int, id: int, level: str, user_answer: int):
    leaders = user_answer_db(user_id, id, level, user_answer)
    return f'Ответ {leaders}'

@user_router.post('/plus')
async def done(user_id: int, id: int, correct_answer: int, level: str):
    result = plus_point_db(user_id, id, correct_answer, level)
    return f'Результат {result}'