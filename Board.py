def boardGame():
    BOARD_ROWS = 6
    BOARD_COLUMNS = 7
    result = ""
    for row in range(BOARD_ROWS):
        for column in range(BOARD_COLUMNS):
            result += "0 "
        result += "\n"
    return result

