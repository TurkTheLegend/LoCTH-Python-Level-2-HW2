import time
def gcd(x,y) :
    while(y) :
       x, y = y, x % y
    return x

def lcm(x,y) :
    lcm = (x*y)/gcd(x,y)
    return lcm

time1 = time.process_time()
print(gcd(137690, 298),lcm(137690, 298))
time2 = time.process_time()
print(time2 - time1)