# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# Like Hello world, but built with Pants.

python_library(name='djangoHello',
  dependencies=[
    '3rdparty/python:Django',
    #'3rdparty/python:django-core', # enable this line and disable line below to demostrate build break
    '3rdparty_src/python/django-core', #enable this line and disable line above to show "just work"
    'examples/src/python/greet:greet', # pretent we need this
  ],
  sources=globs('*.py'),
)
