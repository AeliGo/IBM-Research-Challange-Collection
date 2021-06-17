def StringMatching(pattern, text):
    m = len(pattern)
    n = len(text)
    compareCount = 0
    for i in range(0, n - m + 1):
        j = 0
        while j < m:
            compareCount += 1
            if pattern[j] == text[i + j]:
                j = j + 1        
                if j == m:
                    print("number of character comparisons is ", compareCount)
                    return i
            else:
                break

    print("number of character comparisons is ", compareCount)   
    return -1
    

print(StringMatching("lido", "supercalifragilisticexpialidocious"))