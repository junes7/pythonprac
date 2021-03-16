# async with
import asyncio
 
class AsyncAdd:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    async def __aenter__(self):
        await asyncio.sleep(1.0)
        return self.a + self.b    # __aenter__에서 값을 반환하면 as에 지정한 변수에 들어감
 
    async def __aexit__(self, exc_type, exc_value, traceback):
        pass
 
async def main():
    async with AsyncAdd(1, 2) as result:    # async with에 클래스의 인스턴스 지정
        print(result)    # 3
 
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

# async for
import asyncio
 
class AsyncCounter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop
 
    def __aiter__(self):
        return self
 
    async def __anext__(self):
        if self.current < self.stop:
            await asyncio.sleep(1.0)
            r = self.current
            self.current += 1
            return r
        else:
            raise StopAsyncIteration
 
async def main():
    async for i in AsyncCounter(3):    # for 앞에 async를 붙임
        print(i, end=' ')
 
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

# 프로퍼티 사용하기
class Person:
    def __init__(self):
        self.__age = 0
 
    def get_age(self):           # getter
        return self.__age
    
    def set_age(self, value):    # setter
        self.__age = value
 
james = Person()
james.set_age(20)
print(james.get_age())

