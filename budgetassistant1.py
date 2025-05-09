a=int(input('What is your total monthly income?: Rs. '))
b=int(input('How much do you spent on rent?: Rs. '))
c=int(input('How much do you spent on grocery?: Rs. '))
d=int(input('How much do you spent on travel?: Rs. '))
e=int(input('What is your miscellaneous expenses?: Rs. '))
f=a-(b+c+d+e)
if  b+c+d+e==a:
    print("You have fully spent your income. You didn't make any savings. You have to cut your expenses.")
    g = str(input("Are you willing to reduce your expenses?(yes/no): "))
    if g == 'yes':
        print("Great!!!")
        h = str(input('In which category do you want your expenses to be reduced?(rent/grocery/travel/miscellaneous): '))
        if h == 'rent':
            print("Great!!!")
            i = int(input('How much?: '))
            j = a - (b + c + d + e - i)
            if b + c + d + e - i < a:
                print('Great, now you can save', j, 'every month.')
        elif h == 'grocery':
                print("Great!!!")
                i = int(input('How much?: '))
                j = a - (b + c + d + e - i)
                if b + c + d + e - i < a:
                    print('Great, now you can save', j, 'every month.')
        elif h == 'travel':
            print("Great!!!")
            i = int(input('How much?: '))
            j = a - (b + c + d + e - i)
            if b + c + d + e - i < a:
                print('Great, now you can save', j, 'every month.')
        elif h == 'miscellaneous':
                print("Great!!!")
                i = int(input('How much?: '))
                j = a - (b + c + d + e - i)
                if b + c + d + e - i < a:
                    print('Great, now you can save', j, 'every month.')
                else:
                    print('none')
    elif g == 'no':
        print('Good luck with your finances!!!')
    else:
        print('none')

elif    b+c+d+e>a:
    print("That is way out of your income. You have to seriously cut down your expenses.")
    g=str(input("Are you willing to reduce your expenses?(yes/no): "))
    if  g=='yes':
      print("Great!!!")
    h=str(input('In which category do you want your expenses to be reduced?(rent/grocery/travel/miscellaneous): '))


    if  h=='rent':
        print("Great!!!")

        i=int(input('How much?: '))
        j = a - (b + c + d + e - i)
        if  b+c+d+e-i<a:
              print('Great, now you can save', j,'every month.')
        else:
            print('This is not sufficient.')
            k=str(input('Do you want to increase the amount?(yes/no):'))
            if  k=='yes':
                l=int(input('How much?: '))
                m=a-(b + c + d + e - i-l)
                if  b+c+d+e-i-l<a:
                    print('Great, now you can save',m,'every month.')
                else:
                    print('none')
            elif k == 'no':
                    print('You will be broke soon.')
            else:
                    print('none')

    elif    h=='grocery':
        print("Great!!!")
        i=int(input('How much?: '))
        j = a - (b + c + d + e - i)
        if  b+c+d+e-i<a:
            print('Great, now you can save', j,'every month.')
        else:
            print('This is not sufficient.')
            k = str(input('Do you want to increase the amount?(yes/no):'))
            if k == 'yes':
                l = int(input('How much?: '))
                m = a - (b + c + d + e - i - l)
                if b + c + d + e - i - l < a:
                    print('Great, now you can save', m, 'every month.')
                else:
                    print('none')
            elif k == 'no':
                    print('You will be broke soon.')
            else:
                    print('none')


    elif    h== 'travel':
        print("Great!!!")
        i = int(input('How much?: '))
        j = a - (b + c + d + e - i)
        if  b+c+d+e-i<a:
            print('Great, now you can save', j,'every month.')
        else:
            print('This is not sufficient.')
            k = str(input('Do you want to increase the amount?(yes/no):'))
            if k == 'yes':
                l = int(input('How much?: '))
                m = a - (b + c + d + e - i - l)
                if b + c + d + e - i - l < a:
                    print('Great, now you can save', m, 'every month.')
                else:
                    print('none')
            elif    k=='no':
                print('You will be broke soon. ')
            else:
                print('none')

    elif h == 'miscellaneous':
        print("Great!!!")
        i = int(input('How much?: '))
        j = a - (b + c + d + e - i)
        if  b+c+d+e-i<a:
            print('Great, now you can save', j,'every month.')
        else:
            print('This is not sufficient.')
            k = str(input('Do you want to increase the amount?(yes/no):'))
            if k == 'yes':
                l = int(input('How much?: '))
                m = a - (b + c + d + e - i - l)
                if b + c + d + e - i - l < a:
                    print('Great, now you can save', m, 'every month.')
                else:
                    print('none')
            elif    k=='no':
                print('You will be broke soon.')
            else:
                print('none')
elif    b+c+d+e<a:
    print("You have made a total savings of", f, "in this month. Invest the money wisely.")

else:
    print('none')







