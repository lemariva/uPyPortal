from ucollections import OrderedDict
import ujson
import utime

import btreedb as uorm
import btree


db = uorm.DB("login-data.db")

class LoginData(uorm.Model):

    __db__ = db
    __table__ = "login"
    __schema__ = OrderedDict([
        ("timestamp", ("TIMESTAMP", uorm.now)),
        ("archived", ("INT", 0)),
        ("username", ("TEXT", "")),
        ("password", ("TEXT", "")),
        ("email", ("TEXT", "")),
        ("street", ("TEXT", "")),
        ("city", ("TEXT", "")),
        ("postcode", ("TEXT", "")),
        ("country", ("TEXT", "")),
        ("mobile", ("TEXT", "")),
        ("content", ("TEXT", "")),
    ])

    @classmethod
    def public(cls):
        print("public")
        for v in cls.__db__.db.values(None, None, btree.DESC):
            res = ujson.loads(v)
            row = cls.Row(*res)
            if row.archived:
                continue
            yield row
