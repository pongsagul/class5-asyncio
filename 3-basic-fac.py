import asyncio
import time 

#กำหนดให้ทุก factorial for ทำการคำนวน  factorial วนไปตามที่กำหนด
async def factorial(n):
    f = 1
    for i in range(2, n + 1):
        print(f"Computing factorial({n}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i

    return f

#เริ่มคำนวณ factorial ทั้ง 3 ค่าแบบพร้อมกัน แต่จะจบไม่พร้อมกันเพราะ gather มีเงื่อนไขว่าต้องทำให้ครบ task ถึงจะปริ้น L ออกมา
async def main():
    L = await asyncio.gather(factorial(2), factorial(3), factorial(4))
    print(L) # [2, 6, 24]

if __name__ =='__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')