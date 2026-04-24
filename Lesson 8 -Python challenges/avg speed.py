a=int(input("Enter a value:"))
b=int(input("Enter second value:"))
c=int(input("Enter third va;ue:"))
avg=(a + b + c) / 3
print("avg=" , avg)

if avg>a and avg> b and avg>c:
    print("%d is hgher than %d , %d , %d" %(avg, a , b , c))
elif avg> a and avg>b:
    print("%d is hgher than %d , %d " %(avg, a , b , c))
elif avg> a and avg>c:
    print("%d is hgher than %d , %d " %(avg, a , c))
elif avg>b and avg>c:
    print("%d is hgher than %d , %d " %(avg, b , c))
elif avg>a:
    print("%d is hgher than %d " %(avg, a ))
elif avg>c:
    print("%d is hgher than %d " %(avg, c))
else:
    print("Invalid input")