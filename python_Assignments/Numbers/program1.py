#Program1---------------->
# num=105
# while num>=7:
#     print(num,end=" ")
#     num-=7
    
#program2----------------->
# num=2332
# for i in range(2,num):
#     if num%i!=0:
#             print('{} is prime number'.format(num))
#             break
#     else:
#         print('{} is not a prime number'.format(num)) 
#         break       
    
    
#program3------------------->
# count=0
# num=496
# for i in range(1,num):
#         if(num%i==0):
#             count+=i
# if(count==num):
#     print('{} num is perfect number'.format(num))
# else:
#     print('{} num is not a perfect number'.format(num))

#program4-------------------->
# num=942111423
# count=0
# while(num!=0):
#     digit=num%10
#     count+=1
#     num=num//10
                    
# print(count)  


#program5--------------------->
# num=942111423
# count=0
# while(num!=0):
#     digit=num%10
#     if(digit%2==0):
#         count+=1
#     num=num//10
    
# print(count)   


#program6---------------------->
# num=942111423
# count=0
# while(num!=0):
#     digit=num%10
#     if(digit%2==1):
#         count+=1
#     num=num//10
    
# print(count)  


#program7------------------------>
# num=43521
# output=0
# while(num!=0):
#     digit=num%10
#     output=output*10+digit
#     num=num//10
    
# print(output)    


#program8-------------------------->
# num=2332
# temp=num
# reverse=0
# while(num!=0):
#     digit=num%10
#     reverse=reverse*10+digit
#     num=num//10
    
# if(temp==reverse):
#     print('{} is plaindrome'.format(reverse))
# else:
#     print('{} is not  a palindrome'.format(reverse))
    

#program9----------------------->
# num=145
# output=0
# while(num!=0):
#     digit=num%10
        
    
num=5
count=1
for i in range(num,0,-1):
    count=count*i
        
print(count)        
               