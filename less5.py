try:
    print("start code")
    # print(dfgh)
    print(10/0)
    print("No errors")
# except:
#     print("ooops error")
except NameError:
    print(" NAME ERROR!!!")
except ZeroDivisionError:
    print("ZeroDivision ERROR!!!")
print("after capsule")

try:
    print("start")
    # print(start)
    print("No errors")
except (SyntaxError,NameError) as error:
    print(error)
    print()
else:
    print("I am ELSE")
finally:
    print("Finally code")

    def checker(var_1):
        if type(var_1) != str:
            raise TypeError(f"Sorry, we can’t work with {type(var_1)}, "
                            f"we need class str")
        else:
            return print(var_1)


    first_var = 10
    #
    try:
        checker(first_var)
    except:
        print("не той тип даних")
    #
    checker(first_var)


    class BuildingError(Exception):
        def __str__(self):
            return "With so much material the house cannot be built!"


    def check_material(amount_of_material, limit_value):
        if amount_of_material > limit_value:
            print("enough material")
        else:
            raise BuildingError(amount_of_material)


    materials = 120
    try:
        check_material(materials, 170)
    except BuildingError as error:
           print(error)
