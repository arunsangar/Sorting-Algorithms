def counting_sort(list):
    max_element = int(max(list))
    min_element = int(min(list))
    element_range = max_element - min_element + 1
    count = [0 for _ in range(element_range)]
    output = [0 for _ in range(len(list))]
    for i in range(len(list)):
        count[list[i]-min_element] += 1
    for i in range(1, len(count)):
        count[i] += count[i-1]
    for i in range(len(list)-1, -1, -1):
        output[count[list[i]-min_element]-1] = list[i]
        count[list[i]-min_element] -= 1
    for i in range(len(list)):
        list[i] = output[i]
    return list
