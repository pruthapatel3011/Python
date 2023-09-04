#def add(*args):
 #   total=0
  #  for arg in args:
   #     total+=arg
   # return total

#print(add(1))

#def display_name(*args):
 #   for arg in args:
  #      print(arg,end=" ")

#display_name("prutha","d","patel")

#def print_add(**kwargs):
 #   for key,value in kwargs.items():
  #      print(f"{key}: {value}")

#print_add(street="123 fake",
 #         apt="100",
  #        city="detroit",
   #       state="MI",
    #      zip="54321")

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()

    if "apt" in kwargs:
       print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
       print(f"{kwargs.get('street')}")
       print(f"{kwargs.get('pobox')}")
    else:
       print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("dr.","spongebob","squarepants",
         street="123 fake",
         pobox="PO box #1001",
         city="detroit",
         state="MI",
         zip="54321")