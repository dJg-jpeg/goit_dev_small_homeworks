from datetime import datetime


def factorize(*numbers):
    res = []
    for number in numbers:
        dividers = []
        for divider in range(number // 2)[1:]:
            if number % divider == 0:
                dividers.append(divider)
        if number % 2 == 0:
            dividers.append(number // 2)
        dividers.append(number)
        res.append(dividers)
    return res


if __name__ == "__main__":
    start_time = datetime.now()
    factorize(1024, 59049, 1048576, 9765625, 60466176, 282475249)
    scrypt_worktime = (datetime.now() - start_time)
    print(scrypt_worktime)
