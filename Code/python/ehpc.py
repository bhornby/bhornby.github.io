#this calculates the amount of pay someone gets when they work extra hours
hrs = input("Enter Hours:")
h = float(hrs)
rt = input('Enter Rate:')
r = float(rt)
if h <= 40:
    gp = (h * r)
    print (gp)
elif h > 40:
    exh = (h - 40)
    #extra hours 
    eh = float(exh)
    #extra hours float form
    exrt = (r * 1.5)
    #extra rate
    expy = (eh * exrt)
    #extra pay
    print('extra pay =',expy)
    op = ((h - exh) * (r))
    #original pay without extra time
    print ('your original pay =',op)
    gp = (op + expy)
    #the gross pay
    print ('your gross pay =',gp)
