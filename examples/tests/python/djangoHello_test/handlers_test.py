# coding=utf-8
# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

import sys
import os
import unittest
from django.test import RequestFactory

from djangoHello.svc_handlers import hello

# making django happy!
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoHello.settings")

class HandlersTest(unittest.TestCase):
  request_factory = RequestFactory()
  def test_hello(self):
    request = HandlersTest.request_factory.get('/hello', data={'name': u'foo'})
    resp = hello(request)
    assert('hello' in resp.content)
    assert('foo' in resp.content)
    assert(200 == resp.status_code)
