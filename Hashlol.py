# [ Abdu_Almisrati ]
# [ fb/r00tly ]
# [ Coded By Almisrati ]
# [ 4/27/2020 - Time 6:02 PM ]
# [ Encryption ]
# [ It's Working on Python 3.7 ]
#________________________


from lib.almsrati import *


En = almsrati()

while True:

    choices = input("\033[1;36m  > Enter The Encryption Number Here : \033[0m")

 
    try:
        
        choices = int(choices)
        if choices == 1:
            En.MD5()
        elif choices == 2:
            En.SHA1()
        elif choices == 3:
            En.SHA224()
        elif choices == 4:
            En.SHA256()
        elif choices == 5:
            En.SHA384()
        elif choices == 6:
            En.SHA512()
        elif choices == 7:
            En.SHA3_224()
        elif choices == 8:
            En.SHA3_256()
        elif choices == 9:
            En.SHA3_512()
        elif choices == 10:
            En.SHA3_384()
        elif choices == 11:
            En.Blake2b()
        elif choices == 12:
            En.Blake2s()
        else:
            
            print("\033[1;33m  > It's From 1 To 12, Wear a New Glasses \033[1;31mBitch! \033[0m")
    except ValueError:
            
            print("\033[1;33m  > I Said: I Wanted a Number, Not a \033[1;31mFucking\033[1;33m Word -_- \033[0m")

#Done...
#You Can Edit It, If You Want To Add Functions, I Hate It x_0
#Please Don't Remove My Name or My Copyright :D
