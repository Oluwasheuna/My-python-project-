# GPA Calculator
# progam to calculate the grade point average attained by a student
num = int(input('Enter number of courses offered:'))
points = [5,4,3,2,1,0]

L = []
u = []
for i in range(num):
    code = input('Enter course code:')
    units = eval(input('Enter course unit(s):'))
    score = eval(input('Enter course score:'))
    
    if 70<= score <=100:
        print('Your grade is:' 'A')
        L.append(points[0]*units)
        u.append(units)
        
    elif 60<= score <=69:
        print('Your grade is:', 'B')
        L.append(points[1]*units)
        u.append(units)
        
    elif 50<= score <=59:
        print('Your grade is:', 'C')
        L.append(points[2]*units)
        u.append(units)
        
    elif 43<= score <=49:
        print('Your grade is:', 'D')
        L.append(points[3]*units)
        u.append(units)
        
    elif 40<= score <=42:
        print('Your grade is:', 'E')
        L.append(points[4]*units)
        u.append(units)
        
    elif 0<= score <=39:
        print('Your grade is:', 'F')
        L.append(points[5]*units)

gpa = sum(L)/sum(u)
print('Your Grade point averge(GPA) is:', gpa)
        
        
