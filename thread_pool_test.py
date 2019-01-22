# from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time
import random


def deal_num(n):
    time.sleep(n)
    print(n)
    return n ** 2


if __name__ == '__main__':
    # 参数默认是CPU个数*5
    p = ThreadPoolExecutor()

    obj_l = []
    ww = [1,7, 4, 2, 9,3]
    for i in ww:
        # 异步提交任务
        obj = p.submit(deal_num, i)
        obj_l.append(obj)

    p.shutdown()  # 等同于p.close(),p.join()
    print([obj.result() for obj in obj_l])

