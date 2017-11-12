from .app import app
from . import views
from .dns import DNSServer

import gc


def main(**params):
    gc.collect()
    import logging
    logging.basicConfig(level=logging.INFO)

    # Preload templates to avoid memory fragmentation issues
    gc.collect()
    app._load_template('homepage.html')
    app._load_template('admin.html')
    app._load_template('login.html')
    gc.collect()

    import micropython
    micropython.mem_info()

    gc.collect()
    # starting dns server
    dns_server = DNSServer(**params)
    dns_server.start()
    gc.collect()

    # webserver
    app.run(debug=True, **params)
if __name__ == '__main__':
    main()
