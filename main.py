import csv
import matplotlib.pyplot as plt
from tabulate import tabulate
from datetime import datetime



TODAY = datetime.today()
HEADER = ["Date", "Type", "Category", "Salary", "Payment", "Amount"]


def parse_date(date_str):
    return datetime.strptime(date_str, "%d/%m/%y")


def add_expenses():
    try:
        date = input("Enter Date(dd/mm/yy): ")
        parsed_date = parse_date(date)
        type = input("Enter Type[In/Out]: ")

        if type == "Out":
            category = input("Enter Category[Food/Rent/Groceries]: ")
        else:
            category = "-"

        salary = input("Enter Salary: ")
        payment = input("Enter Payment Method[Cash/UPI/Credit]: ")
        amount = input("Enter Amount: ")

        with open('expenses.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([parsed_date, type, category, salary, payment, amount])
        print("Added Successfully")
    except Exception as e:
        print(f"Error: {e}")


def view_expenses():
    with open('expenses.csv', mode='r') as f:
        csv_lst = csv.reader(f)
        read_list = []
        income=0
        category=["Food","Rent","Groceries"]
        colors = ['gold', 'lightblue', 'lightgreen']
        f_amt=0
        r_amt=0
        g_amt=0
        explode = (0.1, 0, 0)
        for line in csv_lst:
             if(line!=[]):
                if(line[1]=="In"):
                   income=income+int(line[5])
                else:
                   if(line[2]=="Food"):
                      f_amt+=int(line[5])
                   elif(line[2]=="Rent"):
                      r_amt+=int(line[5])
                   elif (line[2] == "Groceries"):
                      g_amt += int(line[5])
        
        f_amt=(f_amt/income) * 100
        read_list.append(f_amt)
        r_amt = (r_amt / income) * 100
        read_list.append(r_amt)
        g_amt = (g_amt / income) * 100
        read_list.append(g_amt)
        plt.pie(read_list, labels=category, colors=colors, explode=explode, autopct='%1.1f%%', startangle=140)
        plt.title('Sample Pie Chart')
        plt.show()

def view_summary():
    try:
        with open('expenses.csv', mode='r') as f:
            csv_lst = csv.reader(f)
            summary_list = []
            date_list = []
            total_income = 0
            total_expenses = 0
            burn_rate = 0

            for line in csv_lst:
                # Skip empty or malformed rows
                if not line or len(line) < 6:
                    continue

                # Append dates to calculate the range
                date_list.append(datetime.strptime(line[0], "%Y-%m-%d %H:%M:%S"))

                # Calculate total income and expenses
                if line[1] == "In":
                    total_income += int(line[5])  # Assuming Amount column is at index 5 for "In"
                elif line[1] == "Out":
                    total_expenses += int(line[5])  # Assuming Amount column is at index 5 for "Out"

            # Compute additional metrics if there are any valid entries
            if date_list:
                min_date = min(date_list)
                exp_date = (TODAY - min_date).days or 1  # Avoid division by zero
                burn_rate = total_expenses / exp_date

            # Calculate leftover amount
            left_amount = total_income - total_expenses

            # Display the summary
            print(f"Average Expense per Day: {burn_rate:.2f}")
            print(f"Total Income: {total_income}")
            print(f"Total Expenses: {total_expenses}")
            print(f"Amount Left: {left_amount}")

    except FileNotFoundError:
        print("The file 'expenses.csv' does not exist. Please add expenses first.")
    except ValueError as ve:
        print(f"Invalid data encountered: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
def main():
    while True:
        try:
            user_input = int(input(
                "Select any of the options: \n 1. Add Expenses \n 2. View Expenses \n 3. View Summary \n 4. Exit\n"))
            if user_input == 1:
                add_expenses()
            elif user_input == 2:
                view_expenses()
            elif user_input == 3:
                view_summary()
            elif user_input == 4:
                print("Exiting program!")
                break
            else:
                print("Invalid Input. Please select again.")
        except ValueError:
            print("Please enter a valid number.")


main()