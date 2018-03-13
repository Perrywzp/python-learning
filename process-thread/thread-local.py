# -*- coding: utf-8 -*-
# def process_student(name):
#     std = Student(name)
#     # std 是局部变量， 但是每个函数都要用它， 因此必须传进去
#     do_task_1(std)
#     do_task_2(std)


# def do_task_1(std):
#     do_subtask_1(std)
#     do_subtask_2(std)


# def do_task_2(std):
#     do_subtask_2(std)
#     do_subtask_2(std)

# global_dict = {}

# def std_thread(name):
#     std = Student(name)
#     # 把std放到全局变量global_dict中
#     global_dict[threading.current_thread()] = std
#     do_task_1()
#     do_task_2()


# def do_task_1():
#     # 不传入std， 而是根据当前线程查找：
#     std = global_dic[threading.current_thread()]
#     ...

# def do_task_2()):
#     # 不传入std， 而是根据当前线程查找：
#     std = global_dic[threading.current_thread()]
#     ...

import threading

# 创建全局ThreadLocal对象：
local_school = threading.local()

def process_student()
