import asyncio 
import time

#สร้าง ฟังชั่น sleep เพื่อเพื่อให้ปริ้นค่า time เริ่ม start ไปเรื่อยโดยมรทศนิยม 2 ตำแหน่ง
#เปลี่ยนการเขียน asyncio ให้ถูกต้อง
async def sleep():
    print (f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)

#สร้าง ฟังชั่น sum และสร้างตัวแปร total และค่า task a และ b และนำมาบวกกับ number
async def sum (name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
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