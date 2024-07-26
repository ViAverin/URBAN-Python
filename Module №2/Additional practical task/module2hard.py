def ancient_cipher(number: int):
    if number < 3 or number > 20:
        return
    first_insert = number
    result = ''
    if number > 15:
        first_insert = 9
        for i in range(1, first_insert + 1):
            for j in range(i + 1, number):
                if number % (i + j) == 0:
                    result += str(i) + str(j)
        return result


print(ancient_cipher(20))

