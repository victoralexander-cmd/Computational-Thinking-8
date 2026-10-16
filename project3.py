medieval_points = 0
modern_points = 0
futuristic_points = 0

answer1 = input("Do you A, like medieval armor, B, multicam equipment, or C, a plasteel exosuit? ")
if answer1 == "A" or answer1 =="a":
    medieval_points += 1
elif answer1 == "B" or answer1 == "b":
    modern_points += 1
elif answer1 == "C" or answer1 == "c":
    futuristic_points += 1
answer2 = input ("Next question, do you like A, the aesthetics of a book, B, a phone, or C, a hologram? ")
if answer2 == "A" or answer2 == "a":
    medieval_points += 2
if answer2 == "B" or answer2 == "b":
    modern_points += 2
if answer2 == "C" or answer2 == "c":
    futuristic_points += 2
answer3 = input("Next, do you like A, a stylized sword, B, a slim attachment setup, or C, an onboard AI? ")
if answer3 == "A" or answer3 == "a":
    medieval_points += 3
if answer3 == "B" or answer3 == "b":
    modern_points += 3
if answer3 == "C" or answer3 == "c":
    futuristic_points += 3
answer4 = input("Next, do you like A, cumbersome but durable, B, light but weak, or C, cumbersome but flexible? ")
if answer4 == "A" or answer4 == "a":
    medieval_points += 2
if answer4 == "B" or answer4 == "b":
    modern_points += 2
if answer4 == "C" or answer4 == "c":
    futuristic_points += 2
answer5 = input ("And finally, do you like A, honor, B, tactics, or C, strategy? ")
if answer5 == "A" or answer5 == "a":
    medieval_points += 4
if answer5 == "B" or answer5 == "b":
    modern_points += 4
if answer5 == "C" or answer5 == "c":
    futuristic_points += 4

print(f"Here are the results: {medieval_points} Medieval points, {modern_points} Modern points, and {futuristic_points} Futuristic points.")

if medieval_points > modern_points and medieval_points > futuristic_points:
    print("You enjoy the knights of old. For king and country!")
if modern_points > medieval_points and modern_points > futuristic_points:
    print("You enjoy the technology we have today. Hoorah!")
if futuristic_points > modern_points and futuristic_points > medieval_points:
    print("You like Sci-Fi and slick materials. Godspeed!")