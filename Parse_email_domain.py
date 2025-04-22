email = ["person1@gmail.com", "person2@gmail.com", "Person3@proton.me", "Person4@yahoo.com", ]
domain = []
def get_domain(email):
    for i in email:
        if "@" in i:
            domain.append(i.split("@")[1])
            
get_domain(email)

unique_domain = set(domain)
print(unique_domain)