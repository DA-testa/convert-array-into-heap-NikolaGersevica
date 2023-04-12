# python3


def build_heap(data):
    swaps = []
   
    size=len(data)
    

    for n in range(size//2,-1,-1):
        small = n 
        while True:
            l_node = 2*n+1 
            r_node = 2*n+2 
            
            if l_node<=size-1: 
                if data[l_node]<data[small]: 
                    small = l_node 
            if r_node<=size-1: 
                if data[r_node]<data[small]: 
                    small = r_node
            if n != small: 
                swaps.append((n,small))
                (data[n],data[small])=(data[small],data[n])
                n = small 
            else:
                break
    return swaps

def main():
    
   
    letter = input()
    if "F" in letter:
        fileName = input()
        if "a" in fileName:
            return
        with open("./tests/"+fileName, mode="r") as file:
            t = int(file.readline())
            data = list(map(int, file.readline().split())) 
    if "I" in letter:
        t = int(input())
        data = list(map(int, input().split())) 

    
    assert len(data) == t

   
    swaps = build_heap(data)

   

    
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
