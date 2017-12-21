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
This falure can only be observed from Pants 1.3.x, it works on 1.2.x and 1.4.x, which I can assume it is a regression(?!)
./pants  -ldebug run.py examples/src/python/djangoHello_main:: --run-py-args="runserver" # failed

```
07:50:13 00:03       [run]
mod_name __main__
loader_name <pkgutil.ImpLoader instance at 0x7f503b5545f0>
mod_name djangoHello_main.manage
loader_name <pkgutil.ImpLoader instance at 0x7f5038c7ff80>
>> loaded script properly
['/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/run/py/CPython-2.7.12/60c0e2312ab1a339593e3b93a2af74e5e33a4b24/.bootstrap',
 '/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/run/py/CPython-2.7.12/60c0e2312ab1a339593e3b93a2af74e5e33a4b24',
 '/usr/lib/python2.7',
 '/usr/lib/python2.7/plat-x86_64-linux-gnu',
 '/usr/lib/python2.7/lib-tk',
 '/usr/lib/python2.7/lib-old',
 '/usr/lib/python2.7/lib-dynload',
 '/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/pyprep/requirements/CPython-2.7.12/fc1cd49392ca7bcd34e13bd2633c40b2a64b6dbd',
 '/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/pyprep/sources/3d487b5f212d0bbe5be444b679f91999466ca834',
 '/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/pyprep/requirements/CPython-2.7.12/fc1cd49392ca7bcd34e13bd2633c40b2a64b6dbd/.deps/ansicolors-1.0.2-py2-none-any.whl',
 '/mnt/tmp/pantsbuild_django_uwsgi/.pants.d/pyprep/requirements/CPython-2.7.12/fc1cd49392ca7bcd34e13bd2633c40b2a64b6dbd/.deps/Django-1.8.12-py2.py3-none-any.whl']
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

Here is the log for 1.2.1 - which it works
```

stderr:
Traceback (most recent call last):
  File "<stdin>", line 7, in <module>
  File "setup.py", line 39, in <module>
    classifiers=classifiers
  File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/core.py", line 111, in setup
    _setup_distribution = dist = klass(attrs)
  File "build/bdist.macosx-10.12-x86_64/egg/setuptools/dist.py", line 315, in __init__
  File "build/bdist.macosx-10.12-x86_64/egg/setuptools/dist.py", line 361, in fetch_build_eggs
  File "build/bdist.macosx-10.12-x86_64/egg/pkg_resources/__init__.py", line 846, in resolve
  File "build/bdist.macosx-10.12-x86_64/egg/pkg_resources/__init__.py", line 1118, in best_match
  File "build/bdist.macosx-10.12-x86_64/egg/pkg_resources/__init__.py", line 1130, in obtain
  File "build/bdist.macosx-10.12-x86_64/egg/setuptools/dist.py", line 429, in fetch_build_egg
  File "build/bdist.macosx-10.12-x86_64/egg/setuptools/command/easy_install.py", line 665, in easy_install

  File "build/bdist.macosx-10.12-x86_64/egg/setuptools/command/easy_install.py", line 695, in install_item

  File "build/bdist.macosx-10.12-x86_64/egg/setuptools/command/easy_install.py", line 876, in install_eggs

  File "build/bdist.macosx-10.12-x86_64/egg/setuptools/command/easy_install.py", line 1115, in build_and_install

  File "build/bdist.macosx-10.12-x86_64/egg/setuptools/command/easy_install.py", line 1101, in run_setup

  File "build/bdist.macosx-10.12-x86_64/egg/setuptools/sandbox.py", line 251, in run_setup
  File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/contextlib.py", line 35, in __exit__
    self.gen.throw(type, value, traceback)
  File "build/bdist.macosx-10.12-x86_64/egg/setuptools/sandbox.py", line 198, in setup_context
  File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/contextlib.py", line 35, in __exit__
    self.gen.throw(type, value, traceback)
  File "build/bdist.macosx-10.12-x86_64/egg/setuptools/sandbox.py", line 169, in save_modules
  File "build/bdist.macosx-10.12-x86_64/egg/setuptools/sandbox.py", line 144, in resume
  File "build/bdist.macosx-10.12-x86_64/egg/setuptools/sandbox.py", line 157, in save_modules
  File "build/bdist.macosx-10.12-x86_64/egg/setuptools/sandbox.py", line 198, in setup_context
  File "build/bdist.macosx-10.12-x86_64/egg/setuptools/sandbox.py", line 248, in run_setup
  File "build/bdist.macosx-10.12-x86_64/egg/setuptools/sandbox.py", line 278, in run
  File "build/bdist.macosx-10.12-x86_64/egg/setuptools/sandbox.py", line 246, in runner
  File "build/bdist.macosx-10.12-x86_64/egg/setuptools/sandbox.py", line 47, in _execfile
  File "/var/folders/lw/22q0mxgn2x37dmd2j7chl_vc0000gp/T/easy_install-iNpBii/Django-2.0/setup.py", line 32, in <module>
    license='MIT',
  File "/var/folders/lw/22q0mxgn2x37dmd2j7chl_vc0000gp/T/easy_install-iNpBii/Django-2.0/django/__init__.py", line 1, in <module>
  File "/var/folders/lw/22q0mxgn2x37dmd2j7chl_vc0000gp/T/easy_install-iNpBii/Django-2.0/django/utils/version.py", line 61, in <module>
AttributeError: 'module' object has no attribute 'lru_cache'
```
