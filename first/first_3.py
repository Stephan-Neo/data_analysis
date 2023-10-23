def alertness(*silence, **params):
    heavy = params.get("heavy", "wxyz")
    unique = params.get("unique", 10)
    sort_key = params.get("sort_key")

    result = {
        'strong': [],
        'careful': [],
        'alert': []
    }

    for s in silence:
        s_upper = s.upper()

        for char in heavy:
            if char.upper() in s_upper:
                result['strong'].append(s_upper)

        letter_set = set(filter(str.isalpha, s))
        if len(letter_set) >= unique:
            result['careful'].append(s)

        words = s.split()
        if all(word.istitle() and len(word) >= 2 for word in words):
            result['alert'].append(words[-1].lower())

    if sort_key:
        for key, value in result.items():
            result[key] = sorted(value, key=sort_key)

    return result


def f(line):
    return sum(1 for x in line if x in "aoeu")


silence = ["Sand Rustling",
           "Snake Sliding",
           "wind whispering",
           "Night In The Village"]
params = {
    "sort_key": f
}

result = alertness(*silence, **params)
print(result)
