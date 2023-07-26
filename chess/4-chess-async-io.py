import asyncio
import time

#async จะต่างจาก syconus คือ ตัว judy นั้นจะไม่สนว่า ฝั่งตรงข้ามจะใช้เวลาเท่่าไหร่ judy เดินเสร็จก็จะไปโต๊ะถัดไปเลย โดยจะใช้ เวลา 1 ชม.
# นำ 5 ไป * 24 ก็จะได้ค่า มา 120 วิ และก็ไปหาร 60 เพื่อเป็นนาที เท่ากับ 2 นาที
# นำ 2 นาที ไปคูณกับ 30 รอบ ก็จะได้ 60 นาที หรือเท่ากับ 1 ชม
# โดยจะเร็วกว่า syconus มากกว่า 12 เท่า เพราะ เวลา judy ทำงานเสร็จ ก็ไปทำโต๊ะอื่นได้เลยไม่ต้องรอ
my_compute_time = 5
opponent_compute_time = 55
opponents = 24
move_pairs = 30


# Again notice that I declare the main() function as a async function
async def main(x):
    for i in range(move_pairs):
        print(f"Thinking of making a move on board {x}")
        # Don't use time.sleep in a async function. I'm using it because in reality you aren't thinking about making a
        # move on 24 boards at the same time, and so I need to block the event loop.
        time.sleep(my_compute_time)
        print(f"Waiting on opponent on board {x}.")
        # Here our opponent is making their turn and now we can move onto the next board.
        await asyncio.sleep(opponent_compute_time)
        print(f"Opponent made move on board {x}")
    print(f"Finished board {x}")


async def async_io():
    # Again same structure as in async-io.py
    tasks = []
    for i in range(opponents):
        tasks += [main(i)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(async_io())
    print(f"Finished in {round(time.perf_counter() - start_time)} secs")