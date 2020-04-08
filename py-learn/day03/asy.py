# coding: utf-8

import asyncio


async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)
    print('worker_1 done')


async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)
    print('worker_2 done')


async def diaodu():
    # task1 task2 创建后不会马上启动执行，只是加到需要运行的队列中了， 而是需要当前线程执行await 让出cpu使用权时才会执行
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    print('before await')
    await task1
    print('awaited worker_1')
    await task2
    print('awaited worker_2')

    # 对于 task 来实现多 协程并发运行， 使用api
    # asyncio.gather(*aws, loop=None, return_exceptions=False)
    # *aws 是task的list


async def log(tag):
    print("%s---start" % tag)
    tag1 = 10 if tag > 10 else tag
    await asyncio.sleep(tag1)
    print("%s -----end" % tag)


async def example(tag_lst):
    tasks = [asyncio.create_task(log(tag)) for tag in tag_lst]
    # 启动时候是串行启动的，结束是等待耗时最长的任务结束的
    await asyncio.gather(*tasks)


# 这个方法验证了，协程是挨个拿到调度器并执行的，如果多个协程处在一个进程中，但是如果再每个协程中都没有释放调度器的操作，
# 多个协程的启动和关闭还是串行的，
# 而多个线程的启动和关闭则是没有相互依赖关系的， 显示的 start, join 即可。
async def log1(tag):
    print("%s---start" % tag)
    print("%s -----end" % tag)


async def example1(tag_lst):
    tasks = [asyncio.create_task(log1(tag)) for tag in tag_lst]
    # 启动时候是串行启动的，结束是等待耗时最长的任务结束的
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    # asyncio.run(diaodu())
    # asyncio.run(example(range(1, 10000)))
    asyncio.run(example1(range(1, 10000)))
