
# untested since I am in a virtual env
def mean(data):
    total = 0.0
    count = 0
    for x in data:
        count += 1
        total += 1

    return total / max(1, count)