# import time
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
#
#
# myclass = MyNumbers()
# myiter = iter(myclass)
# tricks = time.time()
# print("当前时间戳为",tricks)
#
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# import sys
# def fin(n):
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a+b
#         counter +=1
# f = fin(10)
# while True:
#     try:
#         print(next(f),end=" ")
#     except StopIteration:
#         sys.exit()
# def changeval(a):
#     a = 19
# b = 2
# changeval(b)
# print(b)
# def unkonwlength (a,c,*,b):
#     print(a+c+b)
# unkonwlength(3, 2,b=1)
# sum = lambda a, b : a+b
# print(sum(2,3))
# total = 0
# def ss(a,b):
#     global total
#     total = a+b
#     print(total)
# ss(1,2)
# print(total)
# num = [1,2,3]
# print([x*2 for x in num])
# a = [[1,2,3],[4,5,6],[7,8,9]]
# print([[row[i] for row in a] for i in range(3)])
# collection = {"a",1,"b",2,"c",3,3}
# b = set('avbcjbcccdjl')
# "a" in collection
# print("a" in collection)
# print(collection)
# print(b)
# import io
# print(dir(id))
# f = open(r"C:\Users\ilu25\PycharmProjects\io_test.txt","w")
# f.write("this is test\n test is success\n test is good")
# f.close()
# f = open(r"C:\Users\ilu25\PycharmProjects\io_test.txt","r")
# str = f.readlines()
# print(str)
# for line in str:
#     print(line)
# print(f.tell())
# f.close()
# import pickle
# dd = {"name":"caozixia","age":22,"关系":"my"}
# d_byte = pickle.dumps(dd)
# print(d_byte)
# obj = pickle.loads(d_byte)
# print(obj)
# with open("pick_a","wb") as f:
#     dd = {"name": "caozixia", "age": 22, "关系": "my"}
#     pickle.dump(dd,f)
# class Vectot :
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def __str__(self):
#         return "Vector(%d, %d) % (self.a,self.b)"
#     def __add__(self,other):
#         return other(self.a + other.a,self.b + other.b)
# v1 = Vectot(1, 2)
# v2 = Vectot(2, 3)
# print(v1 + v2)
# import os
# print(os.getcwd())
# import glob
# print(glob.glob("*.py"))
# import zlib
# #这个b是数据格式转换，转换为byte型
# s = b"dda jdkwnfao jfakdheifajdhwj"
# # s = c'witch which has which witches wrist watch'
# # s = b'witch which has which witches wrist watch'
# print(len(s))
# b = zlib.compress(s)
# print(b)
# import _thread
# import time
# def thread_test(thread_name,delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count +=1
#         print("%s : %s" % (thread_name,time.ctime(time.time())))
# try:
#     _thread.start_new_thread(thread_test,("thread_1",1,))
#     _thread.start_new_thread(thread_test,("thread_2",4,))
# except:
#     print("无法启动线程")
# while 1:
#     pass
# import threading
# import time
# flag = 0
# class my_thread(threading.Thread):
#     def __init__(self, threadID, name, count):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.count = count
#     def run(self):
#         print("开始线程：",self.name)
#         thread_go(self.name, 5, self.count)
#         print("退出线程：",self.name)
# def thread_go(thead_name, delay, count):
#     while count:
#         if flag:
#             thead_name.exit()
#         time.sleep(delay)
#         print("%s: %s" % (thead_name, time.ctime(time.time())))
#         count -= 1;
# thread1 = my_thread(1,"thread_1",1)
# thread2 = my_thread(2,"thread_2",2)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print("退出主线程")
# import threading
# import time
# class thread_locke(threading.Thread):
#     def __init__(self, threadId, name, count,):
#         threading.Thread.__init__(self)
#         self.threadId = threadId
#         self.name = name
#         self.count = count
#     def run(self):
#         print("线程开始：",self.name)
#         locke.acquire()
#         thread_go(self.name,self.count,5)
#         locke.release()
# locke = threading.Lock()
# def thread_go(thread_name, delay, count):
#     while count:
#         time.sleep(delay)
#         print("%s: %s" % (thread_name,time.ctime(time.time())))
#         count -=1
# thread1 = thread_locke(1, "thread_1", 1)
# thread2 = thread_locke(2, "thread_2", 2)
# thread1.start()
# thread2.start()
# threads = []
# threads.append(thread1)
# threads.append(thread2)
# for i in threads:
#     i.join()
# print("退出主线程")
import queue
import time
import threading
flag = 0
thread_list = ["thread_1", "thread_2", "thread_3"]
name_lsit = ["one", "two", "three", "four", "five"]
locke = threading.Lock()
work_queue = queue.Queue(10)
threadID = 1
threads = []
def thread_queue(thread_name,que):
    while not flag:
        locke.acquire()
        if not work_queue.empty():
            data = que.get()
            locke.release()
            print("%s process %s" % (thread_name, data))
        else:
            locke.release()
        time.sleep(1)
class my_thread(threading.Thread):
    def __init__(self, threadID, name, que):
        self.threadID = threadID
        self.name = name
        self.que = que
    def run(self):
        print("开启线程：", self.name)
        thread_queue(self.name, self.que)
        print("退出线程：", self.name)
for t_name in thread_list:
    thread = my_thread(threadID, t_name, work_queue)
    thread.start()
    threads.append(thread)
    threadID += 1
locke.acquire()
for word in name_lsit:
    work_queue.put(word)
locke.release()
while not work_queue.empty():
    pass
flag = 1
for t in threads:
    t.join()
print("退出主线程")


