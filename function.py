number=10
def display_sum():
    sum_value=2
    print(f"local variable value is:{sum_value}")
    print(f"global variable value is:{number}")
#def display():
display_sum()
print(f"local variable value is second time:{sum_value}")
print(f"global variable value is second time:{number}")
