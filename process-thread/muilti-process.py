# -*- coding: utf-8 -*-
from multiprocessing import Pool, Process, Queue
import os, time, random
import subprocess


def long_time_task(name):
    print('Run tsk %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args = (i, ))
    print('Wating for all subprocess done ...')
    p.close()
    p.join()
    print('All subprocess done.')


print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)


# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code.', p.returncode)


# 写数据进程执行的代码
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读取数据进程执行的代码
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 父进程创建Queue, 并传给子进程
    q = Queue()
    pw = Process(target=write, args = (q,))
    pr = Process(target=read, args = (q,))
    # 启动子进程pw，写入
    pw.start()
    # 启动子进程pr, 读取
    pr.start()
    # 等待pw结束
    pw.join()
    # pr进程里是死循环， 无法等待其结束， 只能强行终止：
    pr.terminate()

