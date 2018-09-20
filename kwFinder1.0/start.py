import multiprocessing
import time


class Start:
    jobs = []

    def __init__(self):
        initiate()


def worker(q, p):
    x = 0
    while x < 10:
        x = x + 1
        q.put(x)
        time.sleep(1)
    q.put(p * 10)


def multiprocess():
    while 0 == 0:
        p = 10
        q = multiprocessing.Queue()
        p = multiprocessing.Process(target=worker, args=(q, p))
        Start.jobs.append(p)
        p.start()
        while q.get() != 100:
            print(q.get())
        p.terminate()


def initiate():
    Start.jobs = []
    for _ in range(1):
        multiprocess()


Start()
