from checkmate import checkmate  # นำเข้าฟังก์ชัน checkmate

def main():
    board = """\
R...
.K..
....
....\
"""
    result = checkmate(board)  # เรียกใช้ฟังก์ชัน
    print("Checkmate result:", result)  # พิมพ์ผลลัพธ์

if __name__ == "__main__":
    main()