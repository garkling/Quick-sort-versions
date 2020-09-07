import timeit, random

def quickSort_mid(array, i=[]):
    if len(array) < 2:
        return array
    else:
        low = 0
        high = len(array) - 1
        mid = (low + high) // 2
        core = array[mid]
        less = [i for i in array[:mid] + array[mid+1:] if i <= core]
        greater = [i for i in array[:mid] + array[mid+1:] if i >= core]
        

        return quickSort_mid(less) + [core] + quickSort_mid(greater)

def quickSort_random(array, i=[]):
    if len(array) < 2:
        return array
    else:
        core = random.choice(array)
        index = array.index(core)
        less = [i for i in array[:index] + array[index+1:] if i <= core]
        greater = [i for i in array[:index] + array[index+1:] if i >= core]


        return quickSort_random(less) + [core] + quickSort_random(greater)

def quickSort_first(array, i=[]):
    if len(array) < 2:
        return array
    else:
        core = array[0]
        less = [i for i in array[1:] if i <= core]
        greater = [i for i in array[1:] if i >= core]
        

        return quickSort_first(less) + [core] + quickSort_first(greater)


arr = [i for i in range(1, 1000001)]
random.shuffle(arr)


start_1 = timeit.default_timer()
quickSort_mid(arr)
stop_1 = timeit.default_timer()

start_2 = timeit.default_timer()
quickSort_random(arr)
stop_2 = timeit.default_timer()

start_3 = timeit.default_timer()
quickSort_first(arr)
stop_3 = timeit.default_timer()

print("Time of quickSort_mid: {} sec".format(stop_1-start_1))
print("Time of quickSort_random: {} sec".format(stop_2-start_2))
print("Time of quickSort_first: {} sec".format(stop_3-start_3))
