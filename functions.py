def is_prime(number):
    if number>1:
        for i in range(2,number):
            if number%i==0:
                print(f"{number} is not prime\n ")
                break
        else:
            print(f"{number} is prime !\n")
    else:
        print("numbers lower than 1 are not prime :)\n") 



def find_index(string,sub):
    in_list=[]
    index=0
    while index<len(string):
        i=string.find(sub,index)
        if i==-1:
            return in_list
        in_list.append(i) 
        index=i+len(sub)
    return in_list     


user_input=int(input("please enter ur number : "))
is_prime(user_input)

string=input("enter ur string : ")
sub=input("the substring to look for : ")

print(find_index(string,sub))