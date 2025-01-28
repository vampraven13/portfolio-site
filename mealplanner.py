import random

def get_meal_plan(weeks):
    breakfast_options = [
        "Chia Pudding with Fruit\n"
        "Prep chia pudding (chia seeds + unsweetened almond milk) the night before.\n"
        "Add frozen berries or a sliced banana before eating.\n"
        "WW Points: Chia seeds (2 tbsp): 3 points\n"
        "Unsweetened almond milk (1/2 cup): 0 points\n"
        "Frozen berries/banana: 0 points\n"
        "Total: 3 points\n"
        "Cost: $0.75\n",
      
        "Microwave Egg Muffins\n"
        "Beat eggs, add diced veggies (like bell peppers or spinach), and microwave in a silicone muffin mold.\n"
        "WW Point: Eggs (2): 0 points\n"
        "Diced Veggies: 0 points\n"
        "Total: 0 points\n"
        "Cost: $0.50\n",
      
        "Overnight Oats\n"
        "Combine oats, unsweetened almond milk, cinnamon, and fresh apple slices.\n"
        "WW Points: Oats (1/2 cup): 0 points\n"
        "Apple: 0 points\n"
        "Cinnamon: 0 points\n"
        "Total: 0 points\n"
        "Cost: $0.80\n",

        "Greek Yogurt and Honey or Fruit\n"
        "Mix plain nonfat Greek yogurt with a drizzle of honey and a sprinkle or granola or some frozen fruit. You can thaw the fruit in the microwave for a little extra fruity coverage.\n"
        "WW Points: Plain nonfat Greek yogurt (1 cup): 0 points\n"
        "Honey (1 tsp): 1 point\n"
        "Granola (optional, 1 tbsp): 2 points\n"
        "Fruit: 0 points\n"
        "Total: 0-3 points\n"
        "Cost: $0.75\n",
      
        "Eggs and Toast\n", 
      
        "Oatmeal with Berries\n",
        
        "Smoothie Bowl\n", 
      
        "Peanut Butter Banana Toast\n", 
      
        "Avocado Toast\n"
    ]
    
    lunch_options = [
        "Grilled Chicken Salad\n", 
      
        "Turkey Wrap\n", 
      
        "Veggie Stir-Fry\n", 
      
        "Quinoa Bowl\n",

        "Soup and Crackers\n"
        "Make a batch of vegetable soup (use canned tomatoes, frozen veggies, and broth). Pair with a few whole-grain crackers.\n"
        "WW Points: Homemade vegetable soup: 0 points\n"
        "Whole-grain crackers (5): 3 points\n"
        "Total: 3 points\n"
        "Cost: $2.50\n",
      
        "Soup and Sandwich\n",
        
        "Chickpea Salad\n"
        "Toss canned chickpeas, diced tomatoes, diced avocado, and lite italian dressing.\n"
        "WW Points: Chickpeas: 0 points\n"
        "Avocado (1/4): 2 points\n"
        "Tomatoes: 0 points\n"
        "Lite dressing: 1 point\n"
        "Total: 3 points per serving\n"
        "Cost: $4.50\n", 
      
        "Pasta with Vegetables\n", 
      
        "Rice and Beans\n", 
      
        "Microwave Baked Potato with Toppings\n"
        "Microwave the pierced potato in 5 minute increments. Top the potato with canned chili beans (fat-free) and a sprinkle of cheese.\n"
        "WW Points: Baked potato: 0 points\n"
        "Fat-free chili beans (1/2 cup): 0 points\n"
        "Shredded Cheese (1 tbsp): 1 point\n"
        "Total: 5 points\n"
        "Cost: $2.50\n",
        
        "Tuna Salad\n"
    ]
    
    dinner_options = [
        "Grilled Salmon with Rice\n", 
      
        "Chicken Stir-Fry\n", 
      
        "Vegetable Curry\n", 
      
        "Spaghetti with Meat Sauce\n",
      
        "Tacos\n", 
      
        "Sheet Pan Chicken and Vegetables\n"
        "Roast chicken, broccoli, and carrots with olive oil and seasoning in the oven.\n"
        "WW Points: Chicken thighs (3 oz): 4 points\n"
        "Roasted veggies (olive oil, 1 tsp): 1 point\n"
        "Total: 5 points\n"
        "Cost: $9.00\n", 
      
        "Sheet Pan Shrimp and Asparagus\n", 
      
        "Stuffed Peppers\n",
      
        "Chili\n", 
      
        "Pasta Primavera\n", 
      
        "Instant Pot Stir-Fried Tofu and Veggies\n"
        "Cook frozen stir-fry veggies and tofu or chicken in an Instant Pot with soy sauce and garlic.\n"
        "Serve over pre-cooked rice.\n"
        "WW Points: Tofu (3 oz): 2 points\n"
        "Frozen veggies: 0 points\n"
        "Soy sauce/rice (1/2 cup): 3 points\n"
        "Total: 5 points\n"
        "Cost: $6.00\n",

        "Air Fryer Salmon and Green Beans\n"
        "Air fry salmon fillets and green beans, pair with a side of microwaveable rice.\n"
        "WW Points: Salmon (3 oz): 0 points\n"
        "Green beans: 0 points\n"
        "Rice (1/2 cup): 3 points\n"
        "Total: 3 points\n"
        "Cost: $9.50\n",

        "Rotisserie Chicken Tacos\n"
        "Use leftover chicken with tortillas, salsa, lettuce, and a sprinkle of cheese.\n"
        "WW Points: Rotisserie chicken (3 oz): 0 points\n"
        "Tortillas (2 small): 4 points\n"
        "Salsa/Lettuce: 0 points\n"
        "Total: 4 points\n"
        "Cost: $4.50\n",

        "Breakfast for Dinner\n"
        "Scrambled eggs, whole wheat toast, and sautéed spinach or frozen veggies.\n"
        "WW Points: Scrambled eggs (2): 0 points\n"
        "Whole wheat toast (1 slice): 2 points\n"
        "Sautéed spinach: 0 points\n"
        "Total: 2 points\n"
        "Cost: $2.50\n",

        "Frozen Pizza Night\n"
        "Pair a frozen cheese pizza with a simple salad on the side.\n"
        "WW Points: Cheese pizza (1/4): 8 points\n"
        "Simple salad with dressing: 1 point\n"
        "Total: 9 points\n"
        "Cost: $5.00\n",

        "Baked Potato Bar\n"
        "Top baked potatoes with shredded chicken, steamed broccoli, and a dollop of Greek yogurt.\n"
        "WW Points: Baked potato (medium): 0 points\n"
        "Shredded chicken: 0 points\n"
        "Broccoli/Greek Yogurt Topping: 0 points\n"
        "Total: 0 Points\n"
        "Cost: $2.50\n",
        
        "Homemade Pizza\n"
    ]
    
    meal_plan = {}
    
    for week in range(1, weeks + 1):
        meal_plan[f"Week {week}"] = {
            "Breakfast": random.sample(breakfast_options, 2),
            "Lunch": random.sample(lunch_options, 5),
            "Dinner": random.sample(dinner_options, 7)
        }
    
    return meal_plan

def display_meal_plan(meal_plan):
    for week, meals in meal_plan.items():
        print(f"{week}:")
        print("Breakfast")
        for i, meal in enumerate(meals["Breakfast"], 1):
            print(f"{i}. {meal}")
        print("\nLunch")
        for i, meal in enumerate(meals["Lunch"], 1):
            print(f"{i}. {meal}")
        print("\nDinner")
        for i, meal in enumerate(meals["Dinner"], 1):
            print(f"{i}. {meal}")
        print("\n")

if __name__ == "__main__":
    weeks = int(input("Enter the number of weeks for the meal plan: "))
    meal_plan = get_meal_plan(weeks)
    display_meal_plan(meal_plan)
    input("Press the enter key to exit.")
