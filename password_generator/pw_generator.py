import string
import random
from csv import writer

def pw_generator():
    lower_case=string.ascii_lowercase
    upper_case=string.ascii_uppercase
    symbol=string.punctuation
    num=string.digits
    platform=input("Enter the platform name:-")
    pw_length=int(input("Enter the length of the password you need:-"))
    create_pw=[]
    create_pw.extend(lower_case)
    create_pw.extend(upper_case)
    create_pw.extend(num)
    create_pw.extend(symbol)
    random.shuffle(create_pw)
    generated_password=("".join(create_pw[0:pw_length]))
    pass_data=[platform+":-",generated_password]
    with open('pwd.csv','a') as f:
        writedata=writer(f)
        writedata.writerow(pass_data)
    print(pass_data)

pw_generator()