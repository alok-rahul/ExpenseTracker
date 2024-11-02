def main():
    print(f"💶Running Expense Tracker 🧾!")

    # Get User Input for the Expense
def get_user_input():
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

    # We will use while becuase it will keep getting the input until user provides the valid input from the mentioned list

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i+1}. {category_name} ")
        
        value_range = f"[1- {len(expense_categories)}]"
        selected_categ = int(input(f"Enter the category number {value_range}")) - 1

        if selected_categ in range(len(expense_categories)):
            break
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
    get_user_input()
    save_expense_to_file()
    summarize_expense()


