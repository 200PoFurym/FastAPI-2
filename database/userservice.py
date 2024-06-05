from database.models import User, UserAnswers, Questions, Result
from datetime import datetime
from database import get_db
def get_all_users_db():
    # Соединение с нашим БД
    db = next(get_db())
    users = db.query(User).all()
    return users

def register_user_db(name, phone_number, level):
    db = next(get_db())
    cheker = db.query(User).filter_by(phone_number=phone_number).first()
    if cheker:
        return f'Уже есть такой пользователь и его ID {cheker.id}'
    else:
        new_user = User(name=name, phone_number=phone_number, level=level, datetime=datetime.now())
        db.add(new_user)
        db.commit()
        return f'Успешный ввод ИД нового пользователя {new_user.id}'

def user_answer_db(user_id, id, level, correct_answer):
    db = next(get_db())
    exact_question = db.query(Questions).filter_by(id=id).first()
    if exact_question:
        if exact_question.correct_answer == correct_answer:
            correctness = True
        else:
            correctness = False
        #     созданиме обьекта в БД
        new_answer = UserAnswers(user_id=user_id, q_id=id, level=level, correctness=correctness)
        db.add(new_answer)
        db.commit()
        return True if correctness else False
    else:
        return 'Вопрос не найден('

def plus_point_db(user_id, correct_answer, level):
    db = next(get_db())
    checker = db.query(Result).filter_by(user_id=user_id).first()
    if checker:
        checker.correct_answer += correct_answer
        return checker.correct_answer
    else:
        new_data = Result(user_id=user_id,correct_answer=correct_answer, level=level)
        db.add(new_data)
        db.commit()

        all_leader = db.query(Result.user_id).order_by(Result.correct_answer.desc())

        return all_leader.index((user_id,)) + 1

