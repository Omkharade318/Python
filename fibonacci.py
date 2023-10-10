def fibo(n):
    fibonacci=[]
    a,b = 0,1
    for _ in range(n):
        fibonacci.append(a)
        a,b = b, a+b
    return fibonacci

num=int(input("Enter the no. of terms you in fibonacci series:\t"))    
 
if (num<=0):
    print("Please Enter a postive integer")
else:
    fibonacci_series = fibo(num)
    print("Fibonacci series:")
    for terms in fibonacci_series:
        print(terms)