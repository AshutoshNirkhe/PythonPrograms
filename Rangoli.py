while True:
    size = int(input("Enter size of Rangoli (1 for a, 2 for b....26 for z): "))
    if 1 <= size <= 26:
        break
    else:
        print("Allowed values 1..26, try again!!")

alphabets_str = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
alphabets = alphabets_str.split(',')

rows = 2*size - 1
cols = 2*(2*size - 1) - 1
a = b = cols//2

for i in range(0, rows):
    current_char = size - 1
    for j in range(0, cols):
        if a <= j <= b:
            if j % 2 != 0:
                print("-", end='')
            else:
                print(alphabets[current_char], end='')
                if j < (cols//2):
                    current_char -= 1
                else:
                    current_char += 1
        else:
            print("-", end='')
    if i < (size-1):
        a -= 2
        b += 2
    else:
        a += 2
        b -= 2
    print()
