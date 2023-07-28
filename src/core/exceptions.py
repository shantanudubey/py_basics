# Exception Handling
import traceback


print('-'*79)
countries = ["IN", "LK", "FR", "DE", "SE", "FI", "IS", "NO"]
test_index = len(countries)
try:
    print(countries[test_index])
except IndexError as e:
    print("Index Error : ", e, test_index)
except Exception as e:
    print("Error :", e)


try:
    num_1 = 12  #int(input("Enter first number : "))
    num_2 = 0   #int(input("Enter second number : "))
    
    result = num_1 / num_2
    print("Result of first-number / second-number :", result)
except ZeroDivisionError:
    print("Second number cannot be zero.")
except ValueError:
    print("Entered numbers have to be integers, please try again.")
except Exception as e:
    print("Error :", e)
else:
    print("Operation successful.")
finally:
    print("Operation has ended.")
print('-'*79)

# Using traceback package
PROGRAM_MODE_DEBUG = "debug"
program_mode = PROGRAM_MODE_DEBUG

try:
    num_1 = 22  #int(input("Enter first integer : "))
    num_2 = 11  #int(input("Enter second integer : "))
    result = num_1 / num_2
    result = round(result, 2)
    print("Result of first-integer / second-integer :", result)
except ZeroDivisionError:
    print("Division by zero encountred!")
except ValueError:
    print("Entered numbers have to be integers, please try again.")
except Exception as e:
    # Use for debug logs
    print("Error :", e)
    if(program_mode == PROGRAM_MODE_DEBUG):
        traceback.print_exc()
print('-'*79)

# Some more useful error types
try:
    import dummy_library
except ImportError as e:
    print("1. ImportError :", e)

try:
    list_big = [2] * (10**10)
    print("2. Result list :", list_big)
except MemoryError as e:
    print("3. MemoryError :", e)
except OverflowError as e:
    print("4. OverflowError :", e)
print('-'*79)


try:
    result = 100**10000
except OverflowError as e:
    print("5. OverflowError :", e)
except MemoryError as e:
    print("6. MemoryError :", e)
except ValueError as e:
    print("7. ValueError :", e)

try:
    print("Calculation Result :", result)
except ValueError as  e:
    print("ValueError :", e)

print('-'*79)


# Exceptions : raise is same as throw

class UnderAgeException(Exception):
    """Age is less than the minimum required."""
    pass

age_limit = 18

try:
    age = 13    #int(input("Enter age : "))
    if age < age_limit:
        raise UnderAgeException("Age is less than the minimum required")
    else:
        print("Valid voting age.")

except UnderAgeException as  e:
    print("Invalid voting age :", e)

print('-'*79)

