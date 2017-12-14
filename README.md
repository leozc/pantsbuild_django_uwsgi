## Problem Run Django Fail but executing PEX is fine
e.g.
./pants  -ldebug run.py   examples/src/python/main:: # works
./pants  -ldebug binary   examples/src/python/main:: 
./dist/main.pex # works


./pants  -ldebug binary   examples/src/python/djangoHello_main::  # works
./dist/djangoHello_main.pex runserver # works

./pants  -ldebug repl   examples/src/python/djangoHello_main::  # works
> import djangoHello_main


./pants  -ldebug run.py examples/src/python/djangoHello_main:: --run-py-args="runserver" # works

```
06:26:03 00:01       [run]
Traceback (most recent call last):
  File "/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/run/py/CPython-2.7.12/0531921f8a33670720671cf2e3c98fc5a3fd030c/.bootstrap/_pex/pex.py", line 360, in execute
    self._wrap_coverage(self._wrap_profiling, self._execute)
  File "/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/run/py/CPython-2.7.12/0531921f8a33670720671cf2e3c98fc5a3fd030c/.bootstrap/_pex/pex.py", line 288, in _wrap_coverage
    runner(*args)
  File "/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/run/py/CPython-2.7.12/0531921f8a33670720671cf2e3c98fc5a3fd030c/.bootstrap/_pex/pex.py", line 320, in _wrap_profiling
    runner(*args)
  File "/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/run/py/CPython-2.7.12/0531921f8a33670720671cf2e3c98fc5a3fd030c/.bootstrap/_pex/pex.py", line 403, in _execute
    return self.execute_entry(self._pex_info.entry_point)
  File "/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/run/py/CPython-2.7.12/0531921f8a33670720671cf2e3c98fc5a3fd030c/.bootstrap/_pex/pex.py", line 461, in execute_entry
    return runner(entry_point)
  File "/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/run/py/CPython-2.7.12/0531921f8a33670720671cf2e3c98fc5a3fd030c/.bootstrap/_pex/pex.py", line 466, in execute_module
    runpy.run_module(module_name, run_name='__main__')
  File "/usr/lib/python2.7/runpy.py", line 182, in run_module
    mod_name, loader, code, fname = _get_module_details(mod_name)
  File "/usr/lib/python2.7/runpy.py", line 107, in _get_module_details
    raise error(format(e))
ImportError: No module named djangoHello_main

FAILURE: /usr/bin/python2.7 djangoHello_main.manage runserver ... exited non-zero (1)
```
"
