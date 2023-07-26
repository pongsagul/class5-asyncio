import asyncio 
import time
from concurrent.futures.thread import ThreadPoolExecutor


#สร้าง ฟังชั่น sleep แบบ synconus
def sleep():
    print (f'Time: {time.time() - start:.2f}')
    time.sleep(1)

#สร้าง ฟังชั่น sum และสร้างตัวแปร total และค่า task a และ b และนำมาบวกกับ number
#สร้าง ตัวแปร executor เพื่อรับ ThreadPoolExecutor ที่ใช้แค่ 2 ตัว ใน pool
#และก็ loop.run_in_executor เพื่อจะให้ run อีก tesk ด้วย synconus ได้
async def sum (name, numbers):
    _executor = ThreadPoolExecutor(2)
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await loop.run_in_executor(_executor, sleep)
        total += number
    print (f'Task {name}: Sum = {total}\n')

start =  time.time()

# สร้าง loop ขึ้นมา และก็สร้าง task ออกมา 2 task และก็ loop เข้าไปและก็ print ออกมา และก็ปิด loop
loop = asyncio.get_event_loop()
tasks = [
    loop.create_task (sum ("A", [1, 2])),
    loop.create_task (sum ("B", [1, 2, 3])),
]
loop.run_until_complete (asyncio.wait(tasks))
loop.close()

#output ออกมา เวลาจะต่างจาก ข้อ 2 จะเหลืออยู่ 3 วิ
end =  time.time()
print (f'Time: {end-start:.2f} sec') 