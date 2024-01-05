import multiprocessing as mp

def a():
    print("\n\nA\n\n")


import sys
print(__name__, sys.modules["__main__"])
# print(sys.path)
# print(globals())
# print(globals()["__main__"])

if __name__ == "__main__":
    mp.set_start_method("spawn")
    ctx = mp.get_context("spawn")
    p = ctx.Process(target=a)
    p.start()
    p.join()
    p.close()
