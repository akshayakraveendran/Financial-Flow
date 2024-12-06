import csv
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
# print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
# print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from tabulate import tabulate
from datetime import datetime
i = 1
l_ist = []
user = 0


parsed_date=datetime.min
today=datetime.today()
print(today)
header=["Date","Type","Category","Salary","Payment","Amount"]
while (i > 0):
    user = int(input("Select any of the options: \n 1.Add Expenses \n 2.View Expenses \n 3.View Summary \n 4.Exit\n"))
    if (user == 1):
        date = input("Enter Date(dd/mm/yy):")
        parsed_date = datetime.strptime(date, "%d/%m/%y")

        type = input("Enter Type[In/Out]:")
        if (type == "Out"):
            category = input("Enter Category[Food/Rent/Groceries]:")
        desc = input("Enter Salary:")
        payment = input("Enter Payment Method[Cash/UPI/Credit]:")
        amount = input("Enter Amount:")
        l_ist.clear()
        l_ist.insert(0, parsed_date)
        l_ist.insert(1, type)
        if (type == "Out"):
            l_ist.insert(2, category)
        l_ist.insert(3, desc)
        l_ist.insert(4, payment)
        l_ist.insert(5, amount)
        print(l_ist)

        with open('expenses.csv', 'a') as f:

            writer = csv.writer(f)
            #writer.writerow(header)
            writer.writerow(l_ist)
            print("Added Successfully")
    if user == 2:
        with open('expenses.csv', mode='r') as f_ile:
            csv_lst = csv.reader(f_ile)
            listt = []
            len1 = list(csv_lst)
            for x, line in enumerate(len1, 0):
                listt.append(line)
                '''print(listt)
                print("x"+str(x))
                print("len"+str(len(len1)))'''
                if (x < len(len1) - 1):
                    if (listt[x] != []):
                        if (listt[x][1] == "In"):
                            line.append("-")

                            print(listt)
                            listt[x][5]=listt[x][4]
                            listt[x][4]=listt[x][3]
                            listt[x][3]=listt[x][2]
                            listt[x][2]="-"
                        table = tabulate(listt,
                             headers=["Date", "Type", "Category", "Desription", "Payment Method", "Amount"],
                             tablefmt="grid"
                        )
            print(table)
    if user == 3:
        with open('expenses.csv', mode='r') as f_ile:
            csv_lst = csv.reader(f_ile)
            listt = []
            totIncome = 0
            expenses = 0
            avgExp = 0
            burnRate = 0
            lftAmt=0
            salary=0
            len1 = list(csv_lst)
            print("len11111"+str(len1))
            # print("len"+str(len(len1)))
            for x, line in enumerate(len1, 0):
                '''if(x>0):
                    x+=1'''
                print("lineee"+str(line))
                print("listtttt"+str(listt))
                listt.append(line)
                '''print(listt)
                print("x"+str(x))
                print("len"+str(len(len1)))'''
                if (x < len(len1) - 1):
                    # print("hjhhh"+str(listt[x][1]))
                    if (listt[x] != []):
                        if (listt[x][1] == "In"):
                            totIncome += int(listt[x][4])
                            lftAmt = totIncome - expenses
                            # print("Total Income:" +str( totIncome))
                        else:
                                '''print(listt[x][4])
                                print(listt)'''

                                expenses += int(listt[x][5])
                                #salary+=desc
                                lftAmt = totIncome - expenses
                                expDate = today - parsed_date
                                expDate1=expDate.days
                                print("Exp Date:" + str(expDate1))
                                burnRate=expenses/expDate1

            print("Average Expense:" + str(burnRate))
            print("Total Income:" + str(totIncome))
            print("Expenses:" + str(expenses))
            print("Amount Left:" + str(lftAmt))
    if(user==4):
        break