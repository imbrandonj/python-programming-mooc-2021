# Binary Chessboard

def chessboard(length):
    """Prints out a binary chessboard
        Of alternating 1s and 0s
        Length is an integer argument that also specifies width""" 

    if length == 1:
        print(1)

    elif length % 2 == 0:
        for i in range(1, length + 1): # So i begins as an odd number
            if i % 2 == 0:
                print("01" * (length // 2))
            else:
                print("10" * (length // 2))

    else:
       for i in range(1, length + 1):
            if i % 2 == 0:
                print("01" * (length // 2) + "0")
            else:
                print("10" * (length // 2) + "1")

chessboard(7)