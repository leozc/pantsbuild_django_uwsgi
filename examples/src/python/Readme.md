## What is this?
This helloWorld example demonstrates how to integrate pantsbuild + python + django + [wsgi](https://uwsgi-docs.readthedocs.org/en/latest/) runner together.

[Pants](http://pantsbuild.github.io/) is a build system for software projects in a variety of languages. It works particularly well for a source code repository that contains many distinct projects.

.pex is generated by [PEX](https://github.com/pantsbuild/pex), it is a type of Python EXecutable file which is executable Python environments in the spirit of virtualenvs.

## Steps to run under uwsgi:

    # Install dependencies for running uwsgi
    pip install pex uwsgi
    # Build, this generates dist/djangoHello_main.pex
    ./pants binary examples/src/python/djangoHello_main
    # Run on port 8080, can be accessed through http://localhost:8080/hello/?name=ouper
    uwsgi --http :8080 -p4 --import examples/src/python/djangoHello_main/bootstrap.py --env UWSGI_PEX=dist/djangoHello_main.pex --module 'djangoHello.wsgi'


## Steps to run in Django manage mode:
    # run without building binary
    ./pants run.py --args='runserver' examples/src/python/djangoHello_main
    # run with binary
    dist/djangoHello_main.pex runserver

## To test
./pants test examples/tests/python/djangoHello_test:test

## There're some catches:
1. Django project structure needs to be tailored for Pants default BuildRoot structure.
2. uwsgi needs a bootstrap in order to load the module from PEX.


## References:
1. PEX bootstrap https://github.com/kwlzn/pyuwsgi_pex/blob/master/pyuwsgi/resources/bootstrap.py
2. Pants documents https://pantsbuild.github.io
