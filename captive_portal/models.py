from . import config


if config.DB_BACKEND == "btree":
    from .models_btree import *
elif config.DB_BACKEND == "filedb":
    from .models_filedb import *
elif config.DB_BACKEND == "sqlite":
    from .models_sqlite import *
else:
    raise ValueError("Unknown DB backend")
