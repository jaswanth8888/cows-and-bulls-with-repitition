k=7727
def cb(inl,chl):
    c,b,k=0,0,[]
    for i in range(len(chl)):
        if(inl[i]==chl[i]):
            b+=1
            k.append(i)
    for i in range(len(k)):
        if(i!=len(k)-1):
            for j in range(i+1,len(k)):
                k[j]=k[j]-1
            del inl[k[i]]
            del chl[k[i]]
        else:
            del inl[k[i]]
            del chl[k[i]]
    for i in chl:
        if i in inl:
            c+=1
            inl.remove(i)
    return (c,b)
for i in range(1,11):
    n=int(input("This is your %d  : Enter you guess"%(i)))
    if(n==k):
        print("You guessed it correctly")
        break
    else:
        inl,chl=[int(x) for x in str(n)],[int(x) for x in str(k)]
        c,b= cb(inl,chl)
        print("cows:%d bulls: %d"%(c,b))
if(i==10):
    print("Thank you for playing,try again later")

