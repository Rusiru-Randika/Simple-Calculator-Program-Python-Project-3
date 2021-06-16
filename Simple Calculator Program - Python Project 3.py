#This Project By Rusiru Randika.Please Test And Support To Next Project#

print("           This is Simple Calculator Program             ")
print("         This Python Project By Rusiru Randika           ")
print("          I Set Up This Program in 9th Grade             ")
print("   I Am Currently Modifying and Publishing This Program  ")
print("")

def main():
    yeslist = ["Y","y"]

    print("Do You Want to Add          :- Press 1")
    print("Do You Want to Reduction    :- Press 2")
    print("Do You Want to Multiply     :- Press 3")
    print("Do You Want to Split        :- Press 4")
    print("")
    z = input("Enter your want : ")
    print("")

    if z == "1":
        
        def Add():

            x=int(input("Input First Number   : "))
            print(" ")

            y=int(input("Input Seconed Number : "))
            print("")

            T=x+y

            print("Total : ",T)
            print("")
        Add()

    if  z == "2":
        
        def Reduction():
            x=int(input("Input First Number   : "))
            print(" ")

            y=int(input("Input Seconed Number : "))
            print("")

            T=x-y

            print("Total : ",T)
            print("")
        Reduction()

    if  z == "3":
        
        def Multiply():
            x=int(input("Input First Number   : "))
            print(" ")

            y=int(input("Input Seconed Number : "))
            print("")

            T=x*y

            print("Total : ",T)
            print("")
        Multiply()

    if  z == "4":
        
        def Split():
            x=int(input("Input First Number   : "))
            print(" ")

            y=int(input("Input Seconed Number : "))
            print("")

            T=x/y

            print("Total : ",T)
            print("")
        Split()


    else:        
        print("You Can Try Agin or exit")
        print("")
            
                


    restart=input("Do You Want to Start Again ?(Y/N) : ")

    print("")
    if restart in yeslist:
        main()
        print("")

    else:
        input("Goodbye...!!!")
        exit()

main()
