def merge_sort_return(arr):
    if len(arr) > 2:
        m = len(arr) // 2
        left = arr[:m]
        r = arr[m:]

        lreturn = merge_sort_return(left)
        rreturn = merge_sort_return(r)

        i = j = 0
        output = []
        while i < len(lreturn) and j < len(rreturn):
            if lreturn[i] <= rreturn[j]:
                output.append(lreturn[i])
                i += 1
            else:
                output.append(rreturn[j])
                j += 1
        while i < len(lreturn):
            output.append(lreturn[i])
            i += 1
        while j < len(rreturn):
            output.append(rreturn[j])
            j += 1
        return output

    elif len(arr) == 2:
        left = arr[0]
        r = arr[1]

        if left > r:
            return [r, left]
        return [left, r]
    return arr


def merge_sort(input_array):
    if len(input_array) > 1:
        middle = len(input_array) // 2
        left = input_array[:middle]
        right = input_array[middle:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0

        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                input_array[k] = left[i]
                i += 1
            else:
                input_array[k] = right[j]
                j += 1
            k += 1
            # print(f'Merging: {input_array}')

        while i < len(left):
            input_array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            input_array[k] = right[j]
            j += 1
            k += 1
