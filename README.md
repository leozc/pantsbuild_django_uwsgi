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
./pants -ldebug test.pytest examples/src/python::
DEBUG] Target alias resources has already been registered. Overwriting!
DEBUG] loading native engine python module from: /var/folders/lw/22q0mxgn2x37dmd2j7chl_vc0000gp/T/tmpIQLVUZ
DEBUG] Executing: git --git-dir=/Users/leo/dev/tmp/pantsbuild_django_uwsgi/.git --work-tree=/Users/leo/dev/tmp/pantsbuild_django_uwsgi rev-parse --abbrev-ref HEAD
DEBUG] Detected git repository at /Users/leo/dev/tmp/pantsbuild_django_uwsgi on branch broken_django
DEBUG] ProjectTree ignore_patterns: ['.*/', '/dist/']
DEBUG] args are: None
DEBUG] spec_roots are: OrderedSet([DescendantAddresses(directory='examples/src/python')])
DEBUG] changed_request is: ChangedRequest(changes_since=None, diffspec=None, include_dependees='none', fast=False)
DEBUG] target_roots are: LiteralTargetRoots(OrderedSet([DescendantAddresses(directory='examples/src/python')]))
DEBUG] build_graph is: <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: OrderedSet([DescendantAddresses(directory='examples/src/python')])
DEBUG] Launching 2 roots.
DEBUG] Root Select(DescendantAddresses(directory='examples/src/python'), =BuildFileAddresses) completed.
DEBUG] Root Select(DescendantAddresses(directory='examples/src/python'), =Collection.of(HydratedTarget)) completed.
DEBUG] computed 2 nodes in 0.049611 seconds. there are 74 total nodes.
DEBUG] address_mapper is: <pants.engine.legacy.address_mapper.LegacyAddressMapper object at 0x11259ac50>
DEBUG] Launching 1 roots.
DEBUG] Root Select(SingleAddress(directory=u'test', name=u'test'), =BuildFileAddresses) completed.
DEBUG] computed 1 nodes in 0.002303 seconds. there are 79 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: OrderedSet([DescendantAddresses(directory='examples/src/python')])
DEBUG] Launching 2 roots.
DEBUG] Root Select(DescendantAddresses(directory='examples/src/python'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(DescendantAddresses(directory='examples/src/python'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.000367 seconds. there are 79 total nodes.
DEBUG] Executing: git --git-dir=/Users/leo/dev/tmp/pantsbuild_django_uwsgi/.git --work-tree=/Users/leo/dev/tmp/pantsbuild_django_uwsgi rev-parse HEAD
DEBUG] Executing: git --git-dir=/Users/leo/dev/tmp/pantsbuild_django_uwsgi/.git --work-tree=/Users/leo/dev/tmp/pantsbuild_django_uwsgi rev-parse --abbrev-ref HEAD

23:12:47 00:00 [main]
               (To run a reporting server: ./pants server)
23:12:47 00:00   [setup]
23:12:48 00:01     [parse]DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'jarjar')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'jarjar'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'jarjar'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001821 seconds. there are 86 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'zinc')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'zinc'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'zinc'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001286 seconds. there are 93 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'compiler-bridge')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'compiler-bridge'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'compiler-bridge'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001406 seconds. there are 100 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'compiler-interface')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'compiler-interface'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'compiler-interface'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001281 seconds. there are 107 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'scalac_2_10')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalac_2_10'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalac_2_10'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001874 seconds. there are 114 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'scala-repl_2_10')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scala-repl_2_10'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scala-repl_2_10'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001227 seconds. there are 121 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'scalastyle_2_10')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalastyle_2_10'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalastyle_2_10'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001100 seconds. there are 128 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'scalac_2_11')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalac_2_11'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalac_2_11'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001202 seconds. there are 135 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'scala-repl_2_11')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scala-repl_2_11'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scala-repl_2_11'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001042 seconds. there are 142 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'scalastyle_2_11')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalastyle_2_11'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalastyle_2_11'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001136 seconds. there are 149 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'scalac_2_12')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalac_2_12'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalac_2_12'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001015 seconds. there are 156 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'scala-repl_2_12')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scala-repl_2_12'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scala-repl_2_12'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001025 seconds. there are 163 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'scalastyle_2_12')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalastyle_2_12'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalastyle_2_12'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001183 seconds. there are 170 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'scalac')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalac'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalac'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.002481 seconds. there are 177 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'scala-repl')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scala-repl'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scala-repl'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001082 seconds. there are 184 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'scalastyle')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalastyle'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalastyle'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001017 seconds. there are 191 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'javac')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'javac'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'javac'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001392 seconds. there are 198 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'jacoco-agent')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'jacoco-agent'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'jacoco-agent'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001103 seconds. there are 205 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'jacoco-cli')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'jacoco-cli'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'jacoco-cli'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001280 seconds. there are 212 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'jar-tool')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'jar-tool'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'jar-tool'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.013899 seconds. there are 219 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'junit_library')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'junit_library'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'junit_library'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001167 seconds. there are 226 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'junit')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'junit'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'junit'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001021 seconds. there are 233 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'benchmark-caliper-0.5')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'benchmark-caliper-0.5'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'benchmark-caliper-0.5'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001311 seconds. there are 240 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'benchmark-java-allocation-instrumenter-2.1')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'benchmark-java-allocation-instrumenter-2.1'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'benchmark-java-allocation-instrumenter-2.1'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001293 seconds. there are 247 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'nailgun-server')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'nailgun-server'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'nailgun-server'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.002467 seconds. there are 254 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'javac-plugin-dep')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'javac-plugin-dep'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'javac-plugin-dep'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.002003 seconds. there are 261 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'scalac-plugin-jars')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalac-plugin-jars'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalac-plugin-jars'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001148 seconds. there are 268 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'scalac-plugin-dep')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalac-plugin-dep'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalac-plugin-dep'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001401 seconds. there are 275 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'scalafix')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalafix'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalafix'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001219 seconds. there are 282 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'scalafmt')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalafmt'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'scalafmt'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001290 seconds. there are 289 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'antlr-3.4')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'antlr-3.4'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'antlr-3.4'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001403 seconds. there are 296 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'antlr-4')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'antlr-4'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'antlr-4'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001378 seconds. there are 303 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'antlr-3.1.3')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'antlr-3.1.3'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'antlr-3.1.3'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001169 seconds. there are 310 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'wire-runtime')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'wire-runtime'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'wire-runtime'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001053 seconds. there are 317 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'wire-compiler')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'wire-compiler'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'wire-compiler'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001075 seconds. there are 324 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'checkstyle')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'checkstyle'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'checkstyle'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001383 seconds. there are 331 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'dependency-update-checker')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'dependency-update-checker'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'dependency-update-checker'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001215 seconds. there are 338 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'pants-runner')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'pants-runner'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'pants-runner'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001788 seconds. there are 345 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'xalan')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'xalan'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'xalan'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001529 seconds. there are 352 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'cobertura-instrument')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'cobertura-instrument'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'cobertura-instrument'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001189 seconds. there are 359 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'cobertura-run')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'cobertura-run'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'cobertura-run'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001234 seconds. there are 366 total nodes.
DEBUG] Injecting to <pants.engine.legacy.graph.LegacyBuildGraph object at 0x1121bc710>: [SingleAddress(directory=u'', name=u'cobertura-report')]
DEBUG] Launching 2 roots.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'cobertura-report'), =Collection.of(HydratedTarget)) completed.
DEBUG] Root Select(SingleAddress(directory=u'', name=u'cobertura-report'), =BuildFileAddresses) completed.
DEBUG] computed 2 nodes in 0.001414 seconds. there are 373 total nodes.

               Executing tasks in goals: jvm-platform-validate -> bootstrap -> imports -> unpack-jars -> deferred-sources -> gen -> resolve -> compile -> resources -> pyprep -> test
23:12:48 00:01   [jvm-platform-validate]
23:12:48 00:01     [jvm-platform-validate]
23:12:48 00:01   [bootstrap]
23:12:48 00:01     [substitute-aliased-targets]DEBUG] ProjectTree ignore_patterns: None

                   expanding examples/src/python/greet:greetDEBUG] ProjectTree ignore_patterns: None

                   expanding examples/src/python/djangoHello:djangoHelloDEBUG] ProjectTree ignore_patterns: None

                   expanding examples/src/python/djangoHello_main:djangoHello_mainDEBUG] ProjectTree ignore_patterns: None

                   expanding examples/src/python/main:main
23:12:48 00:01     [jar-dependency-management]DEBUG] None is not a valid distribution because: Failed to locate the java executable, Distribution('/Users/leo/.cargo/bin', minimum_version=None, maximum_version=None jdk=False) does not appear to be a valid JRE distribution
DEBUG] None is not a valid distribution because: The specified binary path is invalid: /Users/leo/.rbenv/shims
DEBUG] None is not a valid distribution because: The specified binary path is invalid: /Users/leo/.rbenv/shims
DEBUG] None is not a valid distribution because: Failed to locate the java executable, Distribution('/Users/leo/google-cloud-sdk/bin', minimum_version=None, maximum_version=None jdk=False) does not appear to be a valid JRE distribution
DEBUG] None is not a valid distribution because: Failed to locate the java executable, Distribution('/Users/leo/.cargo/bin', minimum_version=None, maximum_version=None jdk=False) does not appear to be a valid JRE distribution
DEBUG] None is not a valid distribution because: The specified binary path is invalid: /Users/leo/.rbenv/shims
DEBUG] None is not a valid distribution because: Failed to locate the java executable, Distribution('/usr/local/bin', minimum_version=None, maximum_version=None jdk=False) does not appear to be a valid JRE distribution
DEBUG] Located Distribution(u'/Library/Java/JavaVirtualMachines/jdk1.8.0_91.jdk/Contents/Home/bin', minimum_version=None, maximum_version=None jdk=False) for constraints: minimum_version None, maximum_version None, jdk False

23:12:48 00:01     [bootstrap-jvm-tools]
23:12:48 00:01     [provide-tools-jar]
23:12:48 00:01   [imports]
23:12:48 00:01     [ivy-imports]
23:12:48 00:01   [unpack-jars]
23:12:48 00:01     [unpack-jars]
23:12:48 00:01   [deferred-sources]
23:12:48 00:01     [deferred-sources]
23:12:48 00:01   [gen]
23:12:48 00:01     [antlr-java]
23:12:48 00:01     [antlr-py]
23:12:48 00:01     [jaxb]
23:12:48 00:01     [protoc]
23:12:48 00:01     [ragel]
23:12:48 00:01     [thrift-java]
23:12:48 00:01     [thrift-py]
23:12:48 00:01     [wire]
23:12:48 00:01   [resolve]
23:12:48 00:01     [ivy]DEBUG] Using previous fetch.

23:12:48 00:01   [compile]
23:12:48 00:01     [compile-jvm-prep-command]
23:12:48 00:01       [jvm_prep_command]
23:12:48 00:01     [compile-prep-command]
23:12:48 00:01     [compile]
23:12:48 00:01     [zinc]
23:12:48 00:01     [jvm-dep-check]
23:12:48 00:01   [resources]
23:12:48 00:01     [prepare]
23:12:48 00:01     [services]
23:12:48 00:01   [pyprep]
23:12:49 00:02     [interpreter]
23:12:49 00:02     [requirements]
                   pants_backend_python_tasks2_resolve_requirements_ResolveRequirements will read from local artifact cache at /Users/leo/dev/tmp/pantsbuild_django_uwsgi/.cache/pants_backend_python_tasks2_resolve_requirements_ResolveRequirements
23:12:49 00:02       [cache]
                   No cached artifacts for 1 target.
                   Invalidated 1 target.
                     Dumping requirement: PythonRequirement(ansicolors==1.0.2)
                     Dumping requirement: PythonRequirement(Django==1.8.12)
                     Dumping requirement: PythonRequirement(django-core==1.4.1)DEBUG] Converted retries value: 5 -> Retry(total=5, connect=None, read=None, redirect=None, status=None)
DEBUG] Converted retries value: 5 -> Retry(total=5, connect=None, read=None, redirect=None, status=None)
DEBUG] Starting new HTTPS connection (1): pypi.python.org
DEBUG] https://pypi.python.org:443 "HEAD /simple/ansicolors/ HTTP/1.1" 200 0
DEBUG] https://pypi.python.org:443 "GET /simple/ansicolors/ HTTP/1.1" 200 957
DEBUG] Converted retries value: 5 -> Retry(total=5, connect=None, read=None, redirect=None, status=None)
DEBUG] https://pypi.python.org:443 "HEAD /simple/Django/ HTTP/1.1" 301 0
DEBUG] https://pypi.python.org:443 "HEAD /simple/django HTTP/1.1" 301 0
DEBUG] https://pypi.python.org:443 "HEAD /simple/django/ HTTP/1.1" 200 0
DEBUG] https://pypi.python.org:443 "GET /simple/django/ HTTP/1.1" 200 16235
DEBUG] Converted retries value: 5 -> Retry(total=5, connect=None, read=None, redirect=None, status=None)
DEBUG] https://pypi.python.org:443 "HEAD /simple/django-core/ HTTP/1.1" 200 0
DEBUG] https://pypi.python.org:443 "GET /simple/django-core/ HTTP/1.1" 200 657
**** Failed to install django-core-1.4.1 (caused by: NonZeroExit("received exit code 1 during execution of `[u'/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/bin/python2.7', '-', 'bdist_wheel', '--dist-dir=/var/folders/lw/22q0mxgn2x37dmd2j7chl_vc0000gp/T/tmpGzb7XJ']` while trying to execute `[u'/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/bin/python2.7', '-', 'bdist_wheel', '--dist-dir=/var/folders/lw/22q0mxgn2x37dmd2j7chl_vc0000gp/T/tmpGzb7XJ']`",)
):
stdout:

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
  File "/var/folders/lw/22q0mxgn2x37dmd2j7chl_vc0000gp/T/easy_install-M8kbH8/Django-2.0/setup.py", line 32, in <module>
    license='MIT',
  File "/var/folders/lw/22q0mxgn2x37dmd2j7chl_vc0000gp/T/easy_install-M8kbH8/Django-2.0/django/__init__.py", line 1, in <module>
  File "/var/folders/lw/22q0mxgn2x37dmd2j7chl_vc0000gp/T/easy_install-M8kbH8/Django-2.0/django/utils/version.py", line 61, in <module>
AttributeError: 'module' object has no attribute 'lru_cache'



23:12:58 00:11   [complete]
               FAILURE
Exception caught: (<class 'pex.resolver.Untranslateable'>)

Exception message: Package SourcePackage(u'file:///Users/leo/dev/tmp/pantsbuild_django_uwsgi/.pants.d/python-setup/resolved_requirements/CPython-2.7.13/django-core-1.4.1.tar.gz') is not translateable by ChainedTranslator(WheelTranslator, EggTranslator, SourceTranslator)
```

## Observation
The error happens within Django and observed in Pants 1.4 context while 1.2.1 is just fine (after performing pip install django)

In high level, in pants 1.2, the context of the local python environment can [leak|https://github.com/pantsbuild/pex/issues/302] into the wheel, yet the latest pants fixed the issue.
