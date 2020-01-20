#*USER ENTERS IN GRADE PERCENTAGE*

grade = float(input("Enter your grade"))

    #Fail
if grade > 0 and grade <= 60 :
    print('F')

    #D Range
elif grade > 60 and grade <= 62 :
    print('D-')
elif grade > 63 and grade <= 66:
    print('D')
elif grade > 67 and grade <= 69:
    print('D+')
elif grade > 70 and grade <= 72 :
    print('C-')
elif grade > 73 and grade <= 76 :
    print('C')
elif grade > 77 and grade <= 79 :
    print('C+')
elif grade > 80 and grade <= 82 :
    print('B-')
elif grade > 83 and grade <= 86 :
    print('B')
elif grade > 87 and grade <= 89 :
    print('B+')
elif grade > 90 and grade <= 92 :
    print('A-')
elif grade > 93 and grade <= 96 :
    print('A')
elif grade >= 97 :
    print('A+')
