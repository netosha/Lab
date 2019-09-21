p = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
x = [-0.5667179987742976, -5.816386671938037, -1.40509272951717, -5.510490110557921, 3.809282985871631, -4.1050481823380505, -7.290724057912376, -7.576280777574006, 4.2701742821615944, 1.6104416645147115, -8.20172523570486, -5.70748966316219, -8.353483349564296, -9.476126789913916, 3.628328521613879, -3.0462173055300585, -11.599568193183842, -5.870240364448224, -6.128217415248262, 2.7818991155551913]
import math as Math

k = [ [0 for i in range(0,20)] for j in range(0,10)]

for i in range(0,10):
    for j in range(0,20):
        value = x[j]
        try:
            if(p[i] == 22):
                """
                In java.lang.StrictMath we can calculate cube root from negative number without any issues.
                In python we have some cases, when powering float number gives us a complex number.
                
                For ex: 
                -0.5667179987742976 ** (1/3) are complex number in python
                StrictMath.cbrt(-0.5667179987742976) are negative float number.

                To prevent that we should abs value to powering.
                """
                sin_value = Math.sin(value)**(1./3.) if Math.sin(value) > 0 else -(abs(Math.sin(value))**(1./3.))
                if type(sin_value) == complex:
                    print(value)
                k[i][j] = Math.atan(Math.cos(sin_value))
            elif p[i] in [6, 8, 10, 16, 20]:

               k[i][j] = ((Math.cos(value)/1)/(2/1)/3)**2;
            else:
                k[i][j] =  Math.e**(Math.tan(value)**(Math.tan(value)/(Math.cos(value)-1)+1));
            if type(k[i][j]) == complex:
                k[i][j] == None
        except:
            k[i][j] = None

for i in k:
    for j in i:
        if j and (type(j) != complex):
            print("%.2f " % j,  sep=' ', end='')
        else:
            print("NaN", end=' ');

    print("\n",end='')