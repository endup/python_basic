import time
import asyncio
#http://www.cnblogs.com/aademeng/articles/7238336.html
now = lambda : time.time()

"""
async def do_some_work(x):
    print('Waiting: ', x)

start = now()

coroutine = do_some_work(2)

loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)

print('TIME: ', now() - start)
"""


"""
async def do_some_work(x):
    print('Waiting: ', x)
    return 'Done after {}s'.format(x)

def callback(future):
    print('Callback: ', future.result())

start = now()

coroutine = do_some_work(2)
#创建循环
loop = asyncio.get_event_loop()
#创建一个task
task = asyncio.ensure_future(coroutine)
#添加回掉函数
task.add_done_callback(callback)
#开始执行
loop.run_until_complete(task)

print('TIME: ', now() - start)
"""

"""
async def do_some_work(x):
    print('Waiting: ', x)
	#模拟在IO环境下的阻塞
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
loop.run_until_complete(task)

print('Task ret: ', task.result())
print('TIME: ', now() - start)
"""

#并发并行
async def do_some_work(x):
    print('Waiting: ', x)

    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

start = now()

coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(4)

tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task ret: ', task.result())

print('TIME: ', now() - start)