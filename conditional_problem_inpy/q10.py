pet_age = int(input("Whats your pet age (in years): "))
animal = input("Whats your animal: ").strip().lower()

if ( pet_age < 2 and animal == 'dog'):
    print("puppy food")
elif (pet_age > 5 and animal == 'cat'):
    print("senior cat food")
else:
    print("not availabe")





