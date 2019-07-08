job = input("enter the job type(private,govermnet,bussines)")

if job == "private":
        a = input("tell me about yousel....!!\n")
        sal = int(input("what is your  anual income:?"))
        if sal > 50000:
            print(" 'congratulation' you are approval for loan")
        else:
            print("sorry u are not approval for loan")
elif job == "govermnet":
    b = input("are you a govermnt worker:\n")
    sal_anul = int(input("what is your salary\n"))
    if sal_anul >= 60000 :
        print("you are granted for \b'loan'")
        
    elif sal_anul > 40000:
        print("show me your cradit limit \n")
        credit_limit  = int(input("credit limit\n"))       
        if credit_limit >= 40000:
            print("loan granted\n")
        else:
            print("not granted .. sorry...!!")                
                            
        print("thanku")
