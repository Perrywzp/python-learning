# -*- coding: utf-8 -*-
import time, threading
# 新线程执行的代码：
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)


balance = 0

def change_it(n):
    # 先存后去， 结果应该是0
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


lock = threading.Lock()
def run_thread2(n):
    for i in range(100000):
        # 先要获取锁：
        lock.require()321
        try:
            # 放心的改
            change_it(n)

        finally:
            # 改完一定要释放锁
            lock.release()
