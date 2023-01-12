try:
    from ProjectMan.helpers.SQL import BASE, SESSION
except ImportError:
    raise AttributeError
from sqlalchemy import Column, Numeric, String, UnicodeText


class Notes(BASE):
    __tablename__ = "notes"
    user_id = Column(String(14), primary_key=True)
    keyword = Column(UnicodeText, primary_key=True, nullable=False)
    mesg_id = Column(Numeric)

    def __init__(self, user_id, keyword, f_mesg_id):
        self.user_id = str(user_id)
        self.keyword = keyword
        self.mesg_id = int(mesg_id)


Notes.__table__.create(checkfirst=True)


def get_note(user_id, keyword):
    try:
        return SESSION.query(Notes).get((str(user_id), keyword))
    finally:
        SESSION.close()


def get_notes(user_id):
    try:
        return SESSION.query(Notes).filter(Note.user_id == str(user_id)).all()
    finally:
        SESSION.close()


def add_note(user_id, keyword, mesg_id):
    to_check = get_note(user_id, keyword)
    if not to_check:
        adder = Notes(str(user_id), keyword, mesg_id)
        SESSION.add(adder)
        SESSION.commit()
        return True
    rem = SESSION.query(Notes).get((str(user_id), keyword))
    SESSION.delete(rem)
    SESSION.commit()
    adder = Note(str(user_id), keyword, mesg_id)
    SESSION.add(adder)
    SESSION.commit()
    return False


def rm_note(user_id, keyword):
    to_check = get_note(user_id, keyword)
    if not to_check:
        return False
    rem = SESSION.query(Notes).get((str(user_id), keyword))
    SESSION.delete(rem)
    SESSION.commit()
    return True
