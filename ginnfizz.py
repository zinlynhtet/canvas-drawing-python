def gin_fizz_ingredients(num_drinks):

    gin_per_drink = 45  # ml
    lemon_juice_per_drink = 30  # ml
    simple_syrup_per_drink = 10  # ml
    lemon_slices_per_drink = 1
    
    total_gin = gin_per_drink * num_drinks
    total_lemon_juice = lemon_juice_per_drink * num_drinks
    total_simple_syrup = simple_syrup_per_drink * num_drinks
    total_lemon_slices = lemon_slices_per_drink * num_drinks
    
    return total_gin, total_lemon_juice, total_simple_syrup, total_lemon_slices

def main():
    try:
        num_drinks = int(input())
        
        gin, lemon_juice, simple_syrup, lemon_slices = gin_fizz_ingredients(num_drinks)
        
        print(f"{gin} ml gin")
        print(f"{lemon_juice} ml fresh lemon juice")
        print(f"{simple_syrup} ml simple syrup")
        
        if lemon_slices == 1:
            print(f"{lemon_slices} slice of lemon")
        else:
            print(f"{lemon_slices} slices of lemon")
            
    except ValueError:
        print("Please enter a valid number of drinks.")

if __name__ == "__main__":
    main()
