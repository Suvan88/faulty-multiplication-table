def rohandastable(a):
    import random

    r = random.randint(1,10)


    m=[i*a for i in range(11) if i!=0 ]

    m[r]=m[r]+10
    return m
def iscorrect(b):
    mc = [i * b for i in range(11) if i != 0]

    return mc







if __name__ == '__main__':
   n=int(input("enter the number"))
   a=rohandastable(n)
   b=iscorrect(n)
   for i in range(10):
       if b[i]!=a[i]:

           print(f"{n}*{i+1}={a[i]} is faulty")
           a[i] = b[i]
       else:
           print(f"{n}*{i+1}={a[i]}")
print(f"The correct table is {a}")


