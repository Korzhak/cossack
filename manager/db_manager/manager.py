from manager.db_manager import User, BotSession, Base, engine, sess as db
from sqlalchemy import desc
from datetime import datetime


def create_db():
    Base.metadata.create_all(engine)


def add_user(user_id, pin_code, permission, session_duration):
    user = User(user_id=user_id, pin_code=pin_code, permission=permission, session_duration=session_duration)
    db.add(user)
    db.commit()


def add_session(user_id, current_directory="~/"):
    session = BotSession(user_id=user_id, start_session=int(datetime.now().timestamp()),
                         current_directory=current_directory)
    db.add(session)
    db.commit()


def get_user(id):
    return db.query(User).filter_by(user_id=id).first()


def get_last_session():
    return db.query(BotSession).order_by(desc(BotSession.start_session)).first()
