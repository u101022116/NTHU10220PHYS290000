prime=[2,3,5,7]
def showPrime(num):
    for i in range(prime[-1]+2,num+1,2):
        notPrime=False
        for j in prime:
            if i%j==0:
                notPrime=True
                break
        if not notPrime:
            prime.append(i)
    print prime

showPrime(500)
