"""
In this excersice an IP address is taken and the dots/periods
within the address are changed to be surrounded by opening and
closing brackets
"""

def defange (address):
    new_add = []
    final_add = list(address)
    new_add = list(address)
    my_string = ""
    print(new_add)
    for alpha in range(len(new_add)):
        if (new_add[alpha] == '.'):
            new_add[alpha] = '[.]'
    final_add = new_add
    print(final_add)

    for num in final_add:
        my_string += num

    return my_string


def create_address():
    print('enter an address with "." in between numbers')
    my_address = input()
    return my_address

new_address = create_address()
print(defange(new_address))
print('short cheeky way')
print(new_address.replace('.','[.]'))