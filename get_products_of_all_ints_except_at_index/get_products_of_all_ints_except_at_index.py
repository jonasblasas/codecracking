def get_products_of_all_ints_except_at_index(arr):
    ret = []
    for i in range(0, len(arr)):
        val = 1
        for j in range(0, len(arr)):
            if i != j:
                val *= arr[j]
        ret.append(val)
    return ret

a = [1, 7, 3, 4, 0]
print(get_products_of_all_ints_except_at_index(a))