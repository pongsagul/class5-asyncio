import time
#ถ้าตามนี้ ตัวโปรแกรมจะ run ให้เสร็จ จะต้องใช้เวลา 12 โดยคำนวนจาก นำ 5+55 = 60 มาคูณกับ 30 และ คูณ 24 
# จากนั้นมาหาร 60 วิ เพื่อเป็นนาที และนำไปหาร 60 นาที ก็จะได้ ชม.ในการ run
# โดย syconus จะไม่สามารถทำอะไรต่อได้นอกจากรอ 1 โต๊ะทำงานเสร็จ จึงใช้เวลอยู่ที่ 12 ชม
my_compute_time = 5
opponent_compute_time = 55
opponents = 24
move_pairs = 30

def main(x):
    # Loops 30 times to simulate both players making a move
    for i in range(move_pairs):
        print(f"Thinking of making a move on board {x}")
        # We think for 5 seconds
        time.sleep(my_compute_time)
        print(f"Made a move on board {x}.")
        # The opponent thinks for 5 seconds.
        time.sleep(opponent_compute_time)
        print(f"Opponent made move on board {x}")
    print(f"Finished board {x}")


if __name__ == "__main__":
    start_time = time.perf_counter()
    # Loops 24 times because we are playing 24 opponents.
    for j in range(opponents):
        main(j)
    print(f"Finished in {round(time.perf_counter() - start_time)} secs")

    #ถ้าตามนี้ ตัวโปรแกรมจะ run ให้เสร็จ จะต้องใช้เวลา 12