# implementation of string matching solved by Horspool's algorithm
# complementarity of DNA base pair, which has great similarity to string matching
# method `shift_table` builds a shift table from a given pattern
# method `convert` is for converting A to T, T to A, C to G and G to C
# time complexity: Θ(mn) for the worst case, even worse than brute-force approach,
# e.g. text = 000000000000000000, pattern = 10000
# Θ(n) for the average case


def shift_table(p, m):
    table = {}
    for i in range(m):
        table[p[i]] = m
    for j in range(m-1):
        table[p[j]] = m-1-j
    return table
    

def Horspool(text, pattern):
    n = len(text); m = len(pattern)
    table = shift_table(pattern, m)
    print(table,"table")
    i = m - 1
    compareCount = 0

    while i < n:
        k = 0
        while k < m:
            compareCount += 1
            if pattern[m-1-k] == text[i-k]:
                k += 1
            else:
                break
        if k == m:
            print("number of character comparisons is ", compareCount)
            return i - m + 1
        else:
            i += (table[str(text[i])] if str(text[i]) in table else m)
    print("number of character comparisons is ", compareCount)
    return -1


plain_text = "THE_WEATHER_LOOKS_FANTASTIC_TODAY"
pattern = "LOOKS"
print("String matching solved by Horspool's algorithm:\n")
print("The plain text is %s" % plain_text)
print("The pattern string is %s\n" % pattern)

status = Horspool(plain_text, pattern)
if status != -1:
    print("String matching is successful, the index of first occurrence is %d." % status)
else:
    print("String matching in unsuccessful.")
