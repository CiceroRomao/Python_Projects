def compara_str(a,b):
    i = 0
    while i < len(a):
        if(a[i] != b[i]):
            return False
        i+=1
    return True


g = "A2"
h = "1 ((a>a)>(a>a))>(((a>a)>a)>((a>a)>a)) A2 p=(a>a);q=a;r=a;"

print(h.find(g))


if(h.find(g) != -1):
    print("AERW")
else:
    print("uiui")