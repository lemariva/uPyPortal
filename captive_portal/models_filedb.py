from ucollections import OrderedDict
import filedb as uorm


db = uorm.DB("login-db")

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
    def mapkeys(cls, obj):
        return [obj.get(k) for k in cls.__schema__.keys()]

    @classmethod
    def public(cls):
        res = [x for x in cls.scan() if x.archived == 0]
        res.sort(key=lambda x: x.timestamp, reverse=True)
        return res
