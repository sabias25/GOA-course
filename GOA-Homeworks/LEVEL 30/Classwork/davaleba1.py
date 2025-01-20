# საკლასო დავალება:
# მომხმარებელს შემოატანინეთ სახელი და შეინახეთ name ცვლადში.
# შემდეგ ემოატანინეთ არჩევანი (რომელიც იქნება "u" ან "l") და შეინახეთ ეს ინფორმაცია choice ცვლადში.
# თუ choice ტოლია "u"-სი, მაშინ მომხმარებლის სახელი გამოიტანეთ uppercase-ში.
# თუ choice ტოლია "l"-ის, მაშინ მომხმარებლის სახელი გამოიტანეთ lowercase-ში.
# სხვა შემთხვევაში, დაუბეჭდეთ wrong information.


name = input("შეიყვანეთ თქვენი სახელი: ")

choice = input("'u' დიდისთვის  ხოლო  'l' პატარისთვის: ")

if choice == "u":
    print(name.upper())
elif choice == "l":
    print(name.lower())
else:
    print("wrong information")
