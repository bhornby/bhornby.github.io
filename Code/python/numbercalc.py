# calculating the average of 3 numbers in a list and then moving along by one number and repeating
a = ( 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 )

group_size = 7
sum = 0
i = 0

for i in range(0  , group_size):
    sum = sum + a[i]
    
    
for i in range(group_size , len(a)):

    group_avg = sum / group_size 
    
    sum = sum + a[i] - a[i - group_size]
    
    print(group_avg)
    
    

'''
group_size = 7

i = 0

while i < ( len(a) - group_size + 1):

    group = a[ i : i + group_size ]
    
    group_avg = sum(group) / group_size
    
    print(group_avg)
    
    i = i + 1 
'''

