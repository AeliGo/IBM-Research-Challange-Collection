def BottomUp(H):
    n = len(H) - 1
    for i in range(n // 2, 0, -1):
        print(i)
        k = i        
        v = H[k]
        heap = False        
        while not heap and 2 * k <= n:            
            j = 2 * k            
            if j < n:                
                if H[j] < H[j + 1]:                    
                    j = j + 1            
            if v >= H[j]:                
                heap = True            
            else:                
                H[k] = H[j]                
                k = j        
        H[k] = v

def test():    
    a = [0, 2, 9, 7, 6, 5, 8, 3]    
    BottomUp(a)    
    print(a)

test()