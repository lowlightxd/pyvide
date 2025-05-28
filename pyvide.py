def divide(num: float, by: float) -> float:
    if num == by:
        return 1.0

    curnum = num
    result = 0.0
    multiplier = 1.0

    while abs(curnum - by) > 1e-7 and multiplier >= 1e-7:
        while curnum - by >= 0:
            if abs(curnum - by) < 1e-7:
                return result + (1 * multiplier)
            result += 1 * multiplier
            curnum -= by
        if curnum - by < 0:
            multiplier *= 0.1
            curnum *= 10
    return result

