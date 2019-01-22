from multiprocessing import Queue
import threading
import time
import traceback
import random
from time import sleep
from blessings import Terminal
from progressive.bar import Bar
from progressive.tree import ProgressTree, Value, BarDescriptor
__DEFAULT_NUM__=5
class WorkPool:
    def __init__(self,worker_num=__DEFAULT_NUM__):
        self.workers=[]
        self.leaf_values=[Value(0) for i in range(worker_num)]
                #创建进度条显示对象
        self.taskGraphics=TaskGraphics(self.leaf_values,worker_num)
        for i in range(0,worker_num):
            self.workers.append(Worker(i,self.taskGraphics))
    def selectWorker(self):
        worker = None
        for w in self.workers:
            if worker == None or w.task_num() < worker.task_num():
                worker=w
        return worker
    def add_task(self,func,*args):
        availableWorker = self.selectWorker()
        if availableWorker:
            availableWorker.add_task(func,args)
    def wait(self):
        for worker in self.workers:
            worker.join()
                #当所有任务都完成后，应该停止刷新进度显示
        self.taskGraphics.stop()
class Worker(threading.Thread):
    def __init__(self,id,graphics):
        threading.Thread.__init__(self)
        self.id=id
        self.work_queue=Queue.Queue()
        self.size=0
        self.running=False
        self.graphics=graphics
    def getId(self):
        return self.id
    def add_task(self,func,args):#由于这个args是从外边*args传进来的，不需要再取地址,否则多个参数会被打包成一个对象
        self.work_queue.put((func,args))
        self.size+=1
        if not self.running:
            self.start()
    def task_num(self):
        return self.size
    def isRunning(self):
        return self.running
    def stop(self):
        self.running=False
    def run(self):
        self.running=True
        while self.running:
            #self.bind_data[self.id].value+=1
            try:
                func,args_ori=self.work_queue.get(block=False)
                                #添加进度反馈
                args_callback=(self.update,)
                args=args_ori+args_callback
                func(*args)#重新取值，避免直接函数调用时参数个数匹配不上
                self.size-=1
                self.work_queue.task_done()
            except :
                traceback.print_exc()
                break
    def update(self,fileName,percent):
        self.graphics.updateTask(self.id,'task_%d: %s'%(self.id,fileName))
        self.graphics.updateValue(self.id,percent)
class TaskGraphics:
    def __init__(self,data,num=__DEFAULT_NUM__):
        self.bind_data=[Value(0) for i in range(num)]
        #self.bind_data=data
        self.terminal=False
        self.bd_defaults=dict(type=Bar,kwargs=dict(max_value=100))
        self.indicator={}
        self.graph_data={}
        for i in range(0,num):
            task_name='task_%d'%i
            self.indicator[i]=task_name
            self.graph_data[task_name]=BarDescriptor(value=self.bind_data[i],**self.bd_defaults)
        self.__init_tree__()
        threading.Thread(target=self.invalidate,args=()).start()
    def __init_tree__(self):
        t=Terminal()
        self.n=ProgressTree(term=t)
        self.n.make_room(self.graph_data)
    def updateTask(self,id,task_name):
        old_task_name=self.indicator[id]
        if task_name == old_task_name:
            return
        self.graph_data[task_name]=self.graph_data[old_task_name]
        self.indicator[id]=task_name
        del self.graph_data[old_task_name]
    def updateValue(self,id,value):
        self.bind_data[id].value=value
    def invalidate(self):
        while not self.terminal:
            time.sleep(0.1)
            self.n.cursor.restore()
            self.n.draw(self.graph_data,BarDescriptor(self.bd_defaults))
    def stop(self):
        self.terminal=True
def test(i,j):
    #print threading.current_thread(),i
    #print i+j
    time.sleep(0.1)
if __name__ == '__main__':
    workPool=WorkPool(10)
    for k in range(1,100):
        workPool.add_task(test,k,k+1)
    workPool.wait()