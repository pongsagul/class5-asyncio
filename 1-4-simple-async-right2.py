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

#เปลี่ยนวิธีการเขียน จากการกำหนด task เป็นการใช้ gather แทน มันก็คือการสร้าง task และ run พร้อมกัน
async def  main() :
    await asyncio.gather(sum("A",[1,2]), sum("B", [1, 2, 3]))

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())

#output ออกมา เวลาจะต่างจาก ข้อ 2 จะเหลืออยู่ 3 วิ
    end = time.time()
    print(f'Time: {end-start:.2f}sec')


