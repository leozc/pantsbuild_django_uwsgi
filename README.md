This is an example to demostrate how to setup pants + python + django + wsgi runner

Steps:
    # Install dependencies for running uwsgi
    pip install pex uwsgi
    # Build
    ./pants binary   examples/src/python/djangoHelloMain
    # Run
    uwsgi --http :8080 -p4 --import examples/src/python/djangoHelloMain/bootstrap.py --env UWSGI_PEX=dist/djangoHelloMain.pex --module 'djangoHello.wsgi'
