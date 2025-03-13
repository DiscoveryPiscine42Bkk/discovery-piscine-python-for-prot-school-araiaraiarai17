import checkmate

def read_board_from_file(filename):
    """ อ่านกระดานหมากรุกจากไฟล์ """
    try:
        with open(filename, "r") as f:
            board = f.read().strip()
        return board
    except FileNotFoundError:
        print("Error: File not found")
        return None

def main():
    filename = "valid_board.chess"  # เปลี่ยนเป็นชื่อไฟล์ที่ต้องการอ่าน
    board = read_board_from_file(filename)

    if board is None:
        return

    result = checkmate(board)
    print(result)

if __name__ == "__main__":
    main()