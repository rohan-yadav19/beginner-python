def freq_counter(lst):
    freq = {}
    for x in lst:
        freq[x] = freq.get(x, 0) + 1
    return freq

print(freq_counter([1,2,2,3,3,3,4]))
