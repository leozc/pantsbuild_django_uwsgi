# coding=utf-8
# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

import unittest

import os

from django.test import RequestFactory
from djangoHello.svc_handlers import hello

from greet.greet import greet

# make django happy!
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoHello.settings")

class HandlersTest(unittest.TestCase):
  request_factory = RequestFactory()
  def test_hello_with_param(self):
    request = HandlersTest.request_factory.get('/hello', data={'name': u'foo'})
    resp = hello(request)
    assert('hello' in resp.content)
    assert('foo' in resp.content)
    assert(200 == resp.status_code)

  def test_hello_without_param(self):
    request = HandlersTest.request_factory.get('/hello', )
    resp = hello(request)
    assert('hello' in resp.content)
    assert('UNKNOWN' in resp.content)
    assert(200 == resp.status_code)

  def test_greeting_mentions_addressee(self):
    """Fancy formatting should not omit the person we're greeting"""
    assert('foo' in greet('foo'))
