def unique_preserve(lst):
    seen = set()
    out = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

print(unique_preserve([3,1,2,3,2,4,1]))
