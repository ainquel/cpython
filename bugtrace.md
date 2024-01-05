reproducer:

```python
import multiprocessing as mp

def a():
    print("a")


if __name__ == "__main__":
    # fork is working, spawn/forkserver are not
    mp.set_start_method("spawn")
    p = mp.Process(target=a)
    p.start()
    p.join()
```

python version: `Python 3.12.0a5+ (heads/master:3ba7743b06, Feb 22 2023, 09:49:21) [GCC 11.3.0] on linux`

stacktrace:

```bash
Traceback (most recent call last):
  File "/home/a/me/python/cpython/Lib/runpy.py", line 198, in _run_module_as_main
    return _run_code(code, main_globals, None,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/a/me/python/cpython/Lib/runpy.py", line 88, in _run_code
    exec(code, run_globals)
  File "/home/a/me/python/cpython/Lib/trace.py", line 765, in <module>
    main()
  File "/home/a/me/python/cpython/Lib/trace.py", line 753, in main
    t.runctx(code, globs, globs)
  File "/home/a/me/python/cpython/Lib/trace.py", line 450, in runctx
    exec(cmd, globals, locals)
  File "bugtrace.py", line 10, in <module>
    p.start()
  File "/home/a/me/python/cpython/Lib/multiprocessing/process.py", line 121, in start
    self._popen = self._Popen(self)
                  ^^^^^^^^^^^^^^^^^
  File "/home/a/me/python/cpython/Lib/multiprocessing/context.py", line 224, in _Popen
    return _default_context.get_context().Process._Popen(process_obj)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/a/me/python/cpython/Lib/multiprocessing/context.py", line 301, in _Popen
    return Popen(process_obj)
           ^^^^^^^^^^^^^^^^^^
  File "/home/a/me/python/cpython/Lib/multiprocessing/popen_forkserver.py", line 35, in __init__
    super().__init__(process_obj)
  File "/home/a/me/python/cpython/Lib/multiprocessing/popen_fork.py", line 19, in __init__
    self._launch(process_obj)
  File "/home/a/me/python/cpython/Lib/multiprocessing/popen_forkserver.py", line 47, in _launch
    reduction.dump(process_obj, buf)
  File "/home/a/me/python/cpython/Lib/multiprocessing/reduction.py", line 60, in dump
    ForkingPickler(file, protocol).dump(obj)
_pickle.PicklingError: Can't pickle <function a at 0x7f7c07164b50>: attribute lookup a on __main__ failed
```