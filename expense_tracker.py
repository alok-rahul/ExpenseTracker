from expense import Expense


def main():
    print(f"💶Running Expense Tracker 🧾!")
    # Get User Input for the Expense
    expense = get_user_expense()
    print(expense)

    #Write their expense to a file
    save_expense_to_file()

    #Read file and summarize the expense
    summarize_expense()
    
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
def save_expense_to_file():
    print(f"💶Saving the expense to a file🧾!")



# Read file and summarize the expense
def summarize_expense():
    print(f"💶summarize User Expense🧾!")

if __name__ == "__main__":
    main()


