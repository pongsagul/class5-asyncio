#1-1-simple-sync.py
import time

def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

# สร้าง ฟังชั่น sleep ให้มันวนบวกค่า computing 
# สร้าง ตัวแปร total
def sum(name, numbers) :
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        sleep()
        total += number

    #ปริ้น Task a และ B ที่ sum ผลออกมา
    print(f'Task {name}: Sum = {total}\n')

start = time.time()
# เริ่ม start และก็เขียน task เพื่อนที่จะให้จะให้มัน sum ไปเรื่่อยๆตามที่กำหนด
task = [
    sum("A", [1, 2]),
    sum("B", [1,2,3]),
]

end = time.time()
print(f'Time: {end-start:.2f} sec')