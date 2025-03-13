def rotate_board_90(board):
    """
    หมุนกระดานหมากรุก 90 องศาทวนเข็มนาฬิกา
    """
    size = len(board)
    rotated = []

    # สร้างกระดานใหม่โดยการหมุนทีละคอลัมน์
    for x in range(size):
        new_row = [board[y][x] for y in range(size-1, -1, -1)]
        rotated.append(new_row)

    return rotated

def is_attacked(board, king_x, king_y):
    """
    ตรวจสอบว่า King อยู่ในสถานะ 'in check' หรือไม่
    """
    size = len(board)

    # การเคลื่อนที่ของหมากรุกแต่ละตัว
    moves = {
        "P": [(1, -1), (1, 1)],  # Pawn (เดินเฉียงไปข้างหน้า)
        "B": [(1, 1), (1, -1), (-1, 1), (-1, -1)],  # Bishop (เดินแนวทแยง)
        "R": [(1, 0), (-1, 0), (0, 1), (0, -1)],  # Rook (เดินแนวตรง)
        "Q": [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)],  # Queen (Bishop + Rook)

        #Knight (เดินเป็นตัว L: 2 ช่องตรง + 2 ช่องข้าง)
        "N": [
            (2, 2), (2, -2), (-2, 2), (-2, -2),
            (2, 2), (2, -2), (-2, 2), (-2, -2)
        ]
    }

    for piece, directions in moves.items():
        for dx, dy in directions:
            x, y = king_x + dx, king_y + dy

            if 0 <= x < size and 0 <= y < size and board[y][x] == piece:
                return True  # พบหมากที่สามารถโจมตี King ได้

            # สำหรับ R, B, Q ที่เดินได้หลายช่อง
            while piece in "RBQ" and 0 <= x < size and 0 <= y < size:
                if board[y][x] == piece:
                    return True
                elif board[y][x] != ".":  # มีหมากขวาง
                    break
                x += dx
                y += dy

    return False

def checkmate(board_str):
    """
    รับกระดานหมากรุกเป็น string แล้วตรวจสอบว่าราชาอยู่ในสถานะ 'in check' หรือไม่
    """
    board = [list(row) for row in board_str.split("\n")]

    #ค้นหาตำแหน่งของ King (K)
    king_x = king_y = -1
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == "K":
                king_x, king_y = x, y
                break

    if king_x == -1 or king_y == -1:
        print("Error")  # ไม่มี King บนกระดาน
        return "Error"

    if is_attacked(board, king_x, king_y):
        print("Success")
        return "Success"
    else:
        print("Fail") 
        return "Fail" 