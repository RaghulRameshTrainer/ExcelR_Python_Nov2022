"""
clauses:
try
except
else
finally
"""

try:
    with open('days.txt') as obj:
        print(obj.read())
    res=10/2
    print(f"Division of 10 and 2 is : {res}")

    r=5+6
    print(f"Sum of 5 and 6 is :{r}")

    #print("Trainer Name :", trainer[0])

    age=int(input("Enter your age:"))
    if age<0 or age>100:
        raise ValueError("Age should be between 0-100")
    age_next_year=age+1
    print("Your age by next year is :",age_next_year)
except FileNotFoundError as e:
    print("Issue with reading the file.",e)
except ZeroDivisionError as e:
    print("Division by zero Error.",e)
except TypeError as e:
    print("Issue in addition.",e)
except NameError as e:
    print("List Error,", e)
except ValueError as e:
    print("AGE ISSUE:",e)
except Exception as e:
    print("Caught by general exception.",e)
else:
    print("ELSE :- I run since there is no exception")
finally:
    print("FINALLY :- Runs always")
print("----------------- NEXT LINE ---------------------")























