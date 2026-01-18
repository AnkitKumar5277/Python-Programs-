def print_mul_arguments(*args):
    # *args -> List
    for i in args:
        print(i)


print_mul_arguments("pramod1\n")

print_mul_arguments("pramod", "amit", "lucky")
print_mul_arguments("amit", 10, True, False, "PRAMOD")

# Pizza Lovers

# Toppings -  mushroom, paneer, olives, corn, pineapple, jalapeno

def make_pizza(*toppings):
    print(toppings)
    for i in toppings:
        print(i)

pramod = make_pizza("tomato","olives")
jayati = make_pizza("pineapple","olives","corn","paneer")
vinay = make_pizza("tomato")

def max(*args):
    for i in args:
        print(i)

r1 = max(1, 2, 3, 4, 6)
r2 = max(1, 2, 3)
r2 = max(2, 3)
