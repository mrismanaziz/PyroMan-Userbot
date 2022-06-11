try:
    from ProjectMan.helpers.SQL import BASE, SESSION
except ImportError:
    raise AttributeError

from sqlalchemy import Column, String


class GBan(BASE):
    __tablename__ = "gban"
    sender = Column(String(14), primary_key=True)

    def __init__(self, sender):
        self.sender = str(sender)


GBan.__table__.create(checkfirst=True)


def is_gbanned(sender):
    try:
        ret = SESSION.query(GBan).filter(GBan.sender == str(sender)).all()
        return len(ret) > 0
    except BaseException:
        return None
    finally:
        SESSION.close()


def gbanned_users():
    try:
        return SESSION.query(GBan).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def gban(sender):
    adder = GBan(str(sender))
    SESSION.add(adder)
    SESSION.commit()


def ungban(sender):
    rem = SESSION.query(GBan).get((str(sender)))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()
