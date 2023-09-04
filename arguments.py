import time

def net_price(list_price,discount=0,tax=0.05):
    return list_price * (1-discount) *(1+tax)

#print(net_price(500))
print(net_price(500,0.1,0))

def count(end,start=0):
    for x in range(start,end+1):
        print (x)
        time.sleep(1)
    print("Done!")

count(2)

def hello(greeting,title,first,last):
    print(f"{greeting} {title} {first} {last}")

hello("gm",title="ms.",last="patel",first="prutha")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num=get_phone(country=1,area=416,first=789,last=9023)

print(phone_num)