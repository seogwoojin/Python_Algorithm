import math

x1, y1, r1, x2, y2, r2=map(float,input().split())

distance=((x1-x2)**2+(y1-y2)**2)**(1/2)

def print_r(num):
    print("{:.3f}".format(num))

if distance>=r1+r2:
    print_r(0)
    
elif distance+r2<=r1:
    print_r(r2**2)
elif distance+r1<=r2:
    print_r(r1**2)
elif distance<=r2:
    s=(r1+r2+distance)/2
    S1=(s*(s-r1)*(s-r2)*(s-distance))**(1/2)
    
    h=2*S1/distance
    t1=math.asin(h/r1)
    t2=math.asin(h/r2)
    theta1=360-180*t1/math.pi*2
    theta2=180*t2/math.pi*2
    answer1=r1*r1*theta1*math.pi/360
    answer2=r2*r2*theta2*math.pi/360
    print_r(answer1+answer2-2*S1)    

elif distance<=r1:
    s=(r1+r2+distance)/2
    S1=(s*(s-r1)*(s-r2)*(s-distance))**(1/2)
    
    h=2*S1/distance
    t1=math.asin(h/r1)
    t2=math.asin(h/r2)
    theta1=180*t1/math.pi*2
    theta2=360-180*t2/math.pi*2
    answer1=r1*r1*theta1*math.pi/360
    answer2=r2*r2*theta2*math.pi/360
    print_r(answer1+answer2-2*S1)
    
    
else:
    s=(r1+r2+distance)/2
    S1=(s*(s-r1)*(s-r2)*(s-distance))**(1/2)
    
    h=2*S1/distance
    t1=math.asin(h/r1)
    t2=math.asin(h/r2)
    theta1=180*t1/math.pi*2
    theta2=180*t2/math.pi*2
    answer1=r1*r1*theta1*math.pi/360
    answer2=r2*r2*theta2*math.pi/360
    print_r(answer1+answer2-2*S1)
    
