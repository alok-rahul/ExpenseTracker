import calendar
import datetime
from expense import Expense

def main():
    print(f"💶Running Expense Tracker 🧾!")
    expense_file_path = "expenses.csv"
    budget = 2000   #Amount to be spent this month
    # Get User Input for the Expense
    expense = get_user_expense()

    #Write their expense to a file
    save_expense_to_file(expense, expense_file_path)

    #Read file and summarize the expense
    summarize_expense(expense_file_path, budget)

    
def get_user_expense():
    print(f"💶Obtaining the User's Input🧾!")
    expense_name = input("Enter the Expense Name : ")
    expense_amount = float(input("Enter the Expense Amount : "))
    expense_categories = [
        "🏡 Rent",
        "🚗 Transport",
        "🎯 Subscriptions",
        "🍽️ Food",
        "🥳 Fun",
        "✍🏼 Misc"
    ]    
    while True:          # We will use while becuase it will keep getting the input
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i+1}. {category_name} ")
        value_range = f"[1- {len(expense_categories)}]"
        category_index = int(input(f"Enter the category number {value_range}")) - 1

        if category_index in range(len(expense_categories)):
            selected_category = expense_categories[category_index]
            new_expense = Expense(
                name=expense_name , category=selected_category, amount=expense_amount
            )
            return new_expense
        else:
            print("Invalid Input, please try again ! ")


#Write their expense for to a file
def save_expense_to_file(expense:Expense , expense_file_path):
    print(f"{expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding="utf-8") as mf:
        mf.write(f"{expense.name},{expense.amount},{expense.category}\n")

# Read file and summarize the expense
def summarize_expense(expense_file_path, budget):
    print(f"💶summarize User Expense🧾!")
    read_expenses = []
    with open(expense_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            strip_line = line.strip()
            expense_name, expense_amount, expense_category = strip_line.split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category
            )
            #print(line_expense)
            read_expenses.append(line_expense)
    #print(read_expenses)
    amount_by_category = {}
    for expense in read_expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    #print(amount_by_category)
    print("Expenses done by Category: ")
    for key, amount in amount_by_category.items():
        print(f" {key}: {amount:.2f} Euro ")
#Calculate the total amount spent till now
    total_amount_spent = sum(x.amount for x in read_expenses)
    print(f"You have spent {total_amount_spent:.2f} Euro till now ! ")
#Calculate remainig budget
    remaining_budget = budget - total_amount_spent
    print(f"Your remaining budget amount is {remaining_budget:.2f} Euro")
    #Get the current date from the System
    present_date = datetime.datetime.now()
    #Find the number of days in current month
    total_days_in_this_month = calendar.monthrange(present_date.year, present_date.month)[1]
    #print(total_days_in_this_month)
    #Calculate the remaining number of days in current month
    remaining_days = (total_days_in_this_month) - (present_date.day)
    print(f"Remaining number of days in this month: {remaining_days}")

    daily_budget = remaining_budget / remaining_days
    print(f"Your daily Budget for this month is : 💶 {daily_budget:.2f}")

if __name__ == "__main__":
    main()


