usernames=["Dude","Bro","Mister"]
passwords=("p@ssword","abc123","guest")
login_date=["1/1/21","1/2/21","1/3/21"]

users=zip(usernames,passwords,login_date)

for i in users:
    print(i)