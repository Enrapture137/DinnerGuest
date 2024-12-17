import random
count = random.randint(1,5)
guests = ['Athena', 'Dota', 'Apollo', 'Blue', 'Dexter']

for i in range(count):
    cancelled_guest = random.choice(guests)
    guests.remove(cancelled_guest)

input_guests = []

response = input("Would you like to invite someone to dinner? ")

while True:  
    if response in ('y','yes'):
        guests.append(input("What is their name? "))
        response = input("Would you like to invite someone else? ")
    elif response in ('n', 'no'):
        break
    else:
        print("\nThat's not a yes OR a no. Try again.")
        response = input("Would you like to invite someone to dinner? ")  
        continue     
    
count = len(guests)

print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
print(f"Yay! We now have {count} attendees!")
print("The new guest list is: ")
for guest in guests:
    print(f"* {guest}")






