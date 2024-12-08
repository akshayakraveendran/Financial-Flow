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
TODAY=datetime.today()
HEADER=["Date","Type","Category","Salary","Payment","Amount"]
csv_list = []
user_input = 0
parsed_date=datetime.min

while (True):
    user_input = int(input("Select any of the options: \n 1.Add Expenses \n 2.View Expenses \n 3.View Summary \n 4.Exit\n"))
    def AddExpenses():
        date = input("Enter Date(dd/mm/yy):")
        parsed_date = datetime.strptime(date, "%d/%m/%y")
        type = input("Enter Type[In/Out]:")
        if type == "Out":
            category = input("Enter Category[Food/Rent/Groceries]:")
        desc = input("Enter Salary:")
        payment = input("Enter Payment Method[Cash/UPI/Credit]:")
        amount = input("Enter Amount:")
        csv_list.clear()
        csv_list.insert(0, parsed_date)
        csv_list.insert(1, type)
        if type == "Out":
            csv_list.insert(2, category)
        csv_list.insert(3, desc)
        csv_list.insert(4, payment)
        csv_list.insert(5, amount)
        with open('expenses.csv', 'a') as f:

            writer = csv.writer(f)
            writer.writerow(csv_list)
            print("Added Successfully")
    def ViewExpenses():
        with open('expenses.csv', mode='r') as f_ile:
            csv_lst = csv.reader(f_ile)
            read_list = []
            csv_length = list(csv_lst)
            for x, line in enumerate(csv_length, 0):
                read_list.append(line)
                if (x < len(csv_length) - 1):
                    if (read_list[x] != []):
                        if (read_list[x][1] == "In"):
                            line.append("-")
                            read_list[x][5]=read_list[x][4]
                            read_list[x][4]=read_list[x][3]
                            read_list[x][3]=read_list[x][2]
                            read_list[x][2]="-"
                        table = tabulate(read_list,
                             headers=["Date", "Type", "Category", "Desription", "Payment Method", "Amount"],
                             tablefmt="grid"
                        )
            print(table)
    def ViewSummary():
        with open('expenses.csv', mode='r') as f_ile:
            csv_lst = csv.reader(f_ile)
            summary_list = []
            date_list = []
            tot_income = 0
            expenses = 0
            summary_length = list(csv_lst)
            for x, line in enumerate(summary_length, 0):
                summary_list.append(line)
                if (x < len(summary_length) - 1):
                    if (summary_list[x] != []):
                        summary_date=summary_list[x][0]
                        date_list.append(summary_date)
                        min_date = min(date_list)
                        date_object = datetime.strptime(min_date, "%Y-%m-%d %H:%M:%S")
                        if (summary_list[x][1] == "In"):
                            tot_income += int(summary_list[x][4])
                            lft_amt = tot_income - expenses
                        else:
                                expenses += int(summary_list[x][5])
                                lft_amt = tot_income - expenses
                                expDate = TODAY - date_object
                                exp_date_in_days=expDate.days
                                burn_rate=expenses/exp_date_in_days
            print("Formatted date" + str(date_list))
            print("Average Expense:" + str(burn_rate))
            print("Total Income:" + str(tot_income))
            print("Expenses:" + str(expenses))
            print("Amount Left:" + str(lft_amt))

    if user_input == 1:
        AddExpenses()
    if user_input == 2:
        ViewExpenses()
    if user_input == 3:
        ViewSummary()
    if user_input==4:
        print("Exiting the program!! Thank you")
        break



