choice1=str(input('Do you have a bachelors degree?(yes/no): '))
choice2=str(input('Do you have any work experience?(yes/no): '))
if  choice1=='yes' and choice2=='yes':
    print('Congratulations, You are eligible for the job.')
elif    choice1=='yes' and choice2=='no':
    print('Congratulations, you are eligible for an internship')
elif    choice1=='no' and choice2=='yes':
    print('You may apply for a trainee role.')
elif    choice1=='no' and choice2=='no':
    print('You are not eligible at this time.')
else:
    print('None')
print('Thank you!!!')