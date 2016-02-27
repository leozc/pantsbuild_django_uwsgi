import os
import sys
#pip install pex
#uwsgi --http :8080 -p4 --import examples/src/python/djangoHelloMain/bootstrap.py --env UWSGI_PEX=dist/djangoHelloMain.pex --module 'djangoHello:wsgi'

def activate_pex():
  entry_point = os.environ.get('UWSGI_PEX')
  if not entry_point:
    sys.stderr.write('couldnt determine pex from UWSGI_PEX environment variable, bailing!\n')
    sys.exit(1)

  sys.stderr.write('entry_point=%s\n' % entry_point)

  sys.path[0] = os.path.abspath(sys.path[0])
  sys.path.insert(0, entry_point)
  sys.path.insert(0, os.path.abspath(os.path.join(entry_point, '.bootstrap')))

  from pex import pex_bootstrapper
  from pex.environment import PEXEnvironment
  from pex.finders import register_finders
  from pex.pex_info import PexInfo

  pex_bootstrapper.monkeypatch_build_zipmanifest()
  register_finders()

  pex_info = PexInfo.from_pex(entry_point)
  print str(pex_info)
  env = PEXEnvironment(entry_point, pex_info)
  working_set = env.activate()

  sys.stderr.write('sys.path=%s\n\n' % sys.path)

  return entry_point, pex_info, env, working_set

activate_pex()
