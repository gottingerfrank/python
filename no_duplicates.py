def remove_duplicates(work):
    nodupes = []
    for i in range(len(work)):
        if work[i] in work[i+1:]:
            pass
        else:
            nodupes.append(work[i])
    return nodupes
            

work = [1, 2, 4, 2, 3, 5, 1, 6, 2, 7, 2, 4, 8, 8]

print(remove_duplicates(work))

