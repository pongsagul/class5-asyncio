import asyncio
import time

#สร้างฟังชั่น hello เพื่อปริ้นค่า แบบ asyncio
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

#สร้างฟังชั่น main และกำหนดตัว แปร coros เพื่อ กำหนดการทำงานทั้งหมด 10 อัน
#เก็บ task 10 ไว้ใน gather 

async def main():
    coros = [hello(i) for i in range(10)]
    await asyncio.gather(*coros)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')

#start ในเวลาเท่ากัน แต่ done ไม่เท่ากัน