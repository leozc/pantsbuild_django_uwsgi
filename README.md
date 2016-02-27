## This is an hello-world example to demonstrate how to integrate pantsbuild + python + django + wsgi runner.


Steps:
    # Install dependencies for running uwsgi

    pip install pex uwsgi
    # Build
    ./pants binary   examples/src/python/djangoHelloMain
    # Run
    uwsgi --http :8080 -p4 --import examples/src/python/djangoHelloMain/bootstrap.py --env UWSGI_PEX=dist/djangoHelloMain.pex --module 'djangoHello.wsgi'


Some thoughts:
1. Django project structure needs to be tailored for Pants.
2. uwsgi needs a bootstrap in order to load the module from Pex.


References:
1. PEX bootstrap https://github.com/kwlzn/pyuwsgi_pex/blob/master/pyuwsgi/resources/bootstrap.py
2. Pants documents https://pantsbuild.github.io
