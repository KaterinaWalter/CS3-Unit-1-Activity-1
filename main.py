# DEFINE YOUR FUNCTIONS HERE!

# PART A: Function with no args + no return
def welcome_message():
    print("Welcome to my virtual kitchen!")
    print("Today, we're gonna make some pasta 🍝")

# PART B: Function with args + no return
def list_ingreds(main_ingredient, side_dish):
    print(f"Main Ingredient: {main_ingredient}")
    print(f"Side Dish: {side_dish}")

# PART C: Function with args + return

# PART D: Functions with optional arguments


def main():
    # CALL YOUR FUNCTIONS in the main here
    welcome_message()
    list_ingreds("Cheese", "Broccoli")
    list_ingreds("Beef", "Garlic Bread")


if __name__ == "__main__":
    main()

