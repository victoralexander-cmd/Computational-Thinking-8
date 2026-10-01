print("You are an Alpha Comander of the Terminid Brood.")
print("A spacefaring bug race.")
print("You just woke up and are feeling optimistic.")
place = input("Do you exit the Hive or go deeper? ")
if place == "exit":
    print("You walk towards the exit. As you are about to leave, a Hive Guard releases greeting pheromones.")
    print("You greet him back and head off in search for food.")
elif place == "Go deeper":
    print("You head down into a tunnel, and enter the main Hive Plaza.")
    print("Terminids of all kinds come to this center of commerce for all sorts of activities.")
    print("A Bile Titan, hauling supplies looks down and sees you, eyeing you curiously.")
    print("He senses you are of high ranking, and instinctively releases obedience pheromones.")
else:
    print("...What?")
action = input("Do you wish to greet him, or hitch a ride?")
if action == "Greet him":
    print("You greet the Bile Titan affectionately. That seemed to have made his day.")
elif action == "Hitch a ride":
    print("You request to take a ride on the Bile Titan.")
    print("Hearing this, he nods happily.")
    print("You clamber up his leg and onto his back, securing your legs on the braces.")
    print("The bile titan slowly raises up and heads through a cargo tunnel, heading to the nearest food section.")
    print("You arrived at the food court.")
    print("You dismount the bile titan and head for a stand.")
else:
    print("Sorry, I didn't hear what you said.")
food = input ("Do you wish to have a fruit, a creature, or a sugary substance called E710?")
if food == "fruit":
    print("You eat a fruit brought here from your home planet.")
    print("It wasn't ripe so it was very bitter.")
    print("Better off just growing them yourself.")
elif food == "creature":
    print("You take the weird looking creature.")
    print("Looks strange compared to the animals seen on your home planet.")
    print("You eat it, and the taste is strange and unsatisfying.")
    print("Maybe next time you will go hunting.")
elif food == "E710":
    print("You exchange in trophalaxis with another terminid.")
    print("They regurgitate some E710 and hand it to you.")
    print("Everyone is familiar with the process and has done it before.")
    print("Apparently one time a human traveller said you were similar to an ant. What is an ant?")
    print("Anywho, it sustained you well, and now you can carry on with your day.")
else:
    print("Excuse me..?")