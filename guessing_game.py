import random 
r_n = random.randint(1,100)
g_n = int(input("Enter the number that you have guessed:"))
count = 1
while(r_n != g_n):
    if( g_n > r_n):
        print("Number you have guessed is greater than the actual number")
        g_n = int(input("Please guess another number:"))
        count += 1
    else:
        print("Number you have guessed is smaller than the actual number")
        g_n = int(input("Please guess another number:"))
        count += 1
print("Congratulations you have guessed the number right which is {} and it took {} attempts to guess it.".format(r_n,count))

        
        
