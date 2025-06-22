# Python program to illustrate
# *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
# so argv is 

#nested functions

#random functions like lamda func to represent non named functions

#recursive functions
def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
      
print(factorial(4))

#return functions

# In py every variable is a reference, when we pass a variable to a function in py
# a new reference to the object is created

#pass by value and pass by reference
    #Immutable objects (like integers, strings): Passing them to a function doesn’t allow
        # you to modify the original value outside the function.
    #Mutable objects (like lists, dictionaries): Passing them to a 
        # function allows you to modify the original object within the function.

# *args (Non-Keyword Arguments), here we can pass n-number of arguments, without values
def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# **kwargs (Keyword Arguments)
# One can think of the kwargs as being a dictionary that 
# maps each keyword to the value that we pass alongside it.
def myFun(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} == {value}')

# Driver code
myFun(first='Geeks', mid='for', last='Geeks')

#using both *args and **kwargs
def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)
kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)

###creating a sample program 
def calculate_total(*args, **kwargs):
    # Step 1: Add up all the item prices
    total = sum(args)
    
    # Step 2: Apply discount (if provided)
    discount = kwargs.get('discount', 0)  # Default is 0% discount if not provided
    if discount:
        total -= (total * discount / 100)
    
    # Step 3: Apply tax (if provided)
    tax = kwargs.get('tax', 0)  # Default is 0% tax if not provided
    if tax:
        total += (total * tax / 100)
    
    # Step 4: Return the final total
    return total

# Example usage
final_total = calculate_total(100, 200, 50, discount=10, tax=5)
print(f"Final Total: {final_total}")

