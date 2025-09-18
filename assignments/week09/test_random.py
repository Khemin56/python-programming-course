import random

def test_random():
    #สุ่มเลขระหว่าง0-9
    test_random = random.randint(0, 9)
    print("-- เกมทายตัวเลข มาเดาใจคอมพิวเตอร์กันเถอะ")
    #รับค่าการทายจากผู้ใช้
    guess_random = int(input("What is your guess number (0-9)?: "))
    #condition ==> if-elif-else
    if test_random == guess_number:
       print("ยูเก่งมาก มั่วถูกตั้งแต่ครั้งแรกเลย เทพจริงๆ")

    if guess_number < test_random:
        print("ผิดจ้า น้ายไปเนอะ")

    if guess_number > test_random:
        print("ผิดจ้า มากไปเนอะ")  