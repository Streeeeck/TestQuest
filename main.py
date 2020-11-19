dct = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
def CheckCorrect(str):
    sum = 0
    for iter in dct:
        sum += str.count(iter)
    if sum == len(str):
        return True
    else:
        return False
def ConvertToRome(str):
    if not CheckCorrect(str):
        return -1
    m = list(str)
    sub_sum = 0
    sum = 0
    for iter in range(len(m)):
        if iter == len(m) - 1:
            if dct[m[iter]] == dct[m[iter - 1]]:
                sum += sub_sum + dct[m[iter]]
            else:
                sum += dct[m[iter]]
        elif dct[m[iter]] == dct[m[iter + 1]]:
            sub_sum += dct[m[iter]]
        elif dct[m[iter]] > dct[m[iter + 1]]:
            sum += sub_sum + dct[m[iter]]
            sub_sum = 0
        elif dct[m[iter]] < dct[m[iter + 1]]:
            sub_sum += dct[m[iter]]
            sum -= sub_sum
            sub_sum = 0
    return sum

if __name__ == '__main__':
    s = input("Введите число римскими цифрами(при вводе некорректных симвлолов ответ будет -1) ")
    print(ConvertToRome(s))
