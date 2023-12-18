#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            division_result = 0
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)) and my_list_2[i] != 0:
                division_result = my_list_1[i] / my_list_2[i]
            elif my_list_2[i] == 0:
                raise ZeroDivisionError("division by 0")
            elif not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
                raise TypeError("wrong type")
        except IndexError:
            print("out of range")
        except (TypeError, ZeroDivisionError) as e:
            print(e)
        finally:
            result.append(division_result)
    return result
