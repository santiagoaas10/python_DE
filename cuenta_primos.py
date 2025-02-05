def count_primes(n):
    # your code here
    def is_prime(number):
        if number==1:
            return 'NO'
        for i in range(2,number,1):
            if number%i==0:
                return 'NO'
        return 'YES'
    counter=0
    primes=[]
    for i in range(1,n):
        if is_prime(i)=='YES':
            primes.append(i)
            counter+=1 
    
    return counter