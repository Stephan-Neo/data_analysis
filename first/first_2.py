holiday = ("hat",)
data = ["veltusac", "dqrazuiwb",
        "tahqu", "dulroqw",
        "byretusym"]


def ideas(*args, letters="ae",):
    global holiday
    max_len = 0

    for arg in args:
        reversed_arg = arg[::-1]
        filtered_arg = ''.join([c for c in reversed_arg if c not in letters])

        if filtered_arg not in holiday:
            added_word = filtered_arg
            holiday += (added_word,)

            if len(reversed_arg) > max_len:
                max_len = len(reversed_arg)

    return max_len


result = ideas(*data, letters="quvb")
print("result =", result)
print("holiday =", holiday)
