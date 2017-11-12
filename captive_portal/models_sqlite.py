import uorm


db = uorm.DB("sqlite.db")


class LoginData(uorm.Model):

    __db__ = db
    __table__ = "login"
    __pkey__ = "timestamp"
    __schema__ = """
        CREATE TABLE note(
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP PRIMARY KEY,
        archived INT NOT NULL DEFAULT 0,
        username TEXT NOT NULL
        password TEXT NOT NULL
        email TEXT NOT NULL
        street TEXT NOT NULL
        city TEXT NOT NULL
        postcode TEXT NOT NULL
        country TEXT NOT NULL
        mobile TEXT NOT NULL
        content TEXT NOT NULL
        )
    """

    @classmethod
    def public(cls):
        return cls.execute("""
            SELECT * FROM login
            WHERE archived=0
            ORDER BY timestamp
        """)
