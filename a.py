import multiprocessing as mp
import os


def a():
    print("a")

if __name__ == "__main__":
    print(os.getcwd())
    mp.set_start_method("fork")
    p = mp.Process(target=a)
    p.start()
    p.join(10)
    code = p.exitcode
    p.close()
    assert code == 0
