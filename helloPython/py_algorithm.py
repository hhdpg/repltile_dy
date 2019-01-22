def quick_sort(lists):
    for i in range(len(lists)):
        for j in range(i+1, len(lists)):
            if lists[j] < lists[i]:
                lists[i], lists[j] = lists[j], lists[i]
a = [3,9,6,8,5,1,2]
quick_sort(a)
print(a)