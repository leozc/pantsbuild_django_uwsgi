## Django has problem with run.py but PEX is fine 
### Good cases
./pants  -ldebug run.py   examples/src/python/main:: # works
./pants  -ldebug binary   examples/src/python/main:: 
./dist/main.pex # works


./pants  -ldebug binary   examples/src/python/djangoHello_main::  # works
./dist/djangoHello_main.pex runserver # works


./pants  -ldebug repl   examples/src/python/djangoHello_main::  # works
> import djangoHello_main

### Failures
./pants  -ldebug run.py examples/src/python/djangoHello_main:: --run-py-args="runserver" # failed

```
07:50:13 00:03       [run]
mod_name __main__
loader_name <pkgutil.ImpLoader instance at 0x7f503b5545f0>
mod_name djangoHello_main.manage
loader_name <pkgutil.ImpLoader instance at 0x7f5038c7ff80>
>> loaded script properly
>> load Django in main ['/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/run/py/CPython-2.7.12/006b431d01ca2c6f3536bf32fbd6ed54b53505e3', 'runserver']
>> load Django with sys arg ['/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/run/py/CPython-2.7.12/006b431d01ca2c6f3536bf32fbd6ed54b53505e3', 'runserver']
mod_name __main__
loader_name <pkgutil.ImpLoader instance at 0x7f9decd1b5f0>
mod_name djangoHello_main.manage
Traceback (most recent call last):
  File "/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/run/py/CPython-2.7.12/006b431d01ca2c6f3536bf32fbd6ed54b53505e3/.bootstrap/_pex/pex.py", line 360, in execute
    self._wrap_coverage(self._wrap_profiling, self._execute)
  File "/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/run/py/CPython-2.7.12/006b431d01ca2c6f3536bf32fbd6ed54b53505e3/.bootstrap/_pex/pex.py", line 288, in _wrap_coverage
    runner(*args)
  File "/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/run/py/CPython-2.7.12/006b431d01ca2c6f3536bf32fbd6ed54b53505e3/.bootstrap/_pex/pex.py", line 320, in _wrap_profiling
    runner(*args)
  File "/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/run/py/CPython-2.7.12/006b431d01ca2c6f3536bf32fbd6ed54b53505e3/.bootstrap/_pex/pex.py", line 403, in _execute
    return self.execute_entry(self._pex_info.entry_point)
  File "/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/run/py/CPython-2.7.12/006b431d01ca2c6f3536bf32fbd6ed54b53505e3/.bootstrap/_pex/pex.py", line 461, in execute_entry
    return runner(entry_point)
  File "/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/run/py/CPython-2.7.12/006b431d01ca2c6f3536bf32fbd6ed54b53505e3/.bootstrap/_pex/pex.py", line 466, in execute_module
    runpy.run_module(module_name, run_name='__main__')
  File "/usr/lib/python2.7/runpy.py", line 185, in run_module
    mod_name, loader, code, fname = _get_module_details(mod_name)
  File "/usr/lib/python2.7/runpy.py", line 110, in _get_module_details
    raise error(format(e))
ImportError: No module named djangoHello_main

FAILURE: /usr/bin/python2.7 djangoHello_main.manage runserver ... exited non-zero (1)


07:50:16 00:06   [complete]
               FAILURE
```

## Observation
The error happens within Django and observed in Pants 1.3 context while 1.2.1 is just fine and here is output for a good run
```
07:56:21 00:22       [run]
mod_name __main__
loader_name <pkgutil.ImpLoader instance at 0x7f68355665f0>
mod_name djangoHello_main.manage
loader_name <pkgutil.ImpLoader instance at 0x7f6832c58a28>
>> loaded script properly
>> load Django in main ['/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/python-setup/chroots/d0c4cd781ae4672091a1d8dec5ed4151c095242e', 'runserver']
>> load Django with sys arg ['/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/python-setup/chroots/d0c4cd781ae4672091a1d8dec5ed4151c095242e', 'runserver']
mod_name __main__
loader_name <pkgutil.ImpLoader instance at 0x7f481a5235f0>
mod_name djangoHello_main.manage
loader_name <pkgutil.ImpLoader instance at 0x7f4817c15ab8>
>> loaded script properly
>> load Django in main ['/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/python-setup/chroots/d0c4cd781ae4672091a1d8dec5ed4151c095242e', 'runserver']
>> load Django with sys arg ['/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/python-setup/chroots/d0c4cd781ae4672091a1d8dec5ed4151c095242e', 'runserver']
Performing system checks...

System check identified no issues (0 silenced).
December 14, 2017 - 07:56:25
Django version 1.8.12, using settings 'djangoHello.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
