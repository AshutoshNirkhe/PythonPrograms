# https://us-central1-faas-270704.cloudfunctions.net/Rangoli?size=10

def draw_rangoli(request):

    try:
        size = int(request.args.get("size"))
    except ValueError:
        return "Not an int value, please pass int between 1 and 26...exiting!!"

    if not (1 <= size <= 26):
        return "Size must be within 1 to 26...exiting !!"

    alphabets_str = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
    alphabets = alphabets_str.split(',')

    rows = 2*size - 1
    cols = 2*(2*size - 1) - 1
    a = b = cols//2
    rangoli = ""

    for i in range(0, rows):
        current_char = size - 1
        for j in range(0, cols):
            if a <= j <= b:
                if j % 2 != 0:
                    rangoli += "&#8209;"
                else:
                    rangoli += alphabets[current_char]
                    if j < (cols//2):
                        current_char -= 1
                    else:
                        current_char += 1
            else:
                rangoli += "&#8209;"

        if i < (size-1):
            a -= 2
            b += 2
        else:
            a += 2
            b -= 2

        rangoli += "<br/>"

    return rangoli
