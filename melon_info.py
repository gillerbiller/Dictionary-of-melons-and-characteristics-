"""Print out all the melons in our inventory."""


from melons import all_melons_dict 


def melon_information_report(melons):
    """Print each melon with corresponding attribute information."""
    for name_of_melon, characteristics in all_melons_dict.items():

        print(name_of_melon.upper())

        print("-----------")

        for characteristics, details in characteristics.items():
            print(f"{characteristics}:{details}")

            print(" ")

         

        


        



'''have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


for i in melon_names:
    print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
'''