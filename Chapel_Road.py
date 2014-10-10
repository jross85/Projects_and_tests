#Chapel Road
#When running the code, I have to press Enter after every input, not sure why
#Currently need to find a way to close the game if user decides not to play 
#Defined dead for certain choices
#user cannot hit spacebar after putting in their input
#my very first game/project :D
import time 

print """==============================================================================================================
                                                HOUSE ON CHAPEL ROAD
=============================================================================================================="""

time.sleep(3)
x = "..." 
for i in ("%s"): 
	print x 
	
print "This game is based on a true story. All names have been omitted from this story"
time.sleep(2)
print "To protect the identity to all those involved" 
time.sleep(2)
print "This event is still unexplained to this day..."
time.sleep(2)

time.sleep(2)
print "Are you ready to begin? (Y)es or (N)o?" 

decision = raw_input(" ")
if decision == "Y": 
	print "Ok. Be warned, this may disturb some players"
elif decision == "N": 
	print "You are too scared to play" 
else: 
	print "You have to decide..." 
	
def Ending(): 
	print "You wake up in the middle of the street...what happened?" 
	time.sleep(2)
	print "You reach into your pocket for your phone." 
	time.sleep(2)
	print "But there's a crumpled piece of paper there." 
	time.sleep(2)
	print "You pull out the piece of paper." 
	time.sleep(2)
	print " There's odd handwriting on it." 
	time.sleep(2)
	print "It reads: 'You should not have came into the home. I am now at your home, waiting...'"
	time.sleep(2)
	print "Check your documents folder. Open up the text doc home.txt" 
	time.sleep(2)
	
	f = open('home.txt', 'w') 
	f.write('I am now in your home...check the kitchen') 
def dead(): 
	print "You are now dead..."
	
def Hall(): 
	print "...As you get closer and closer to the room, you hear what sounds like a child crying." 
	time.sleep(2)
	print " Your arrive at the doorway. The room is completely dark." 
	time.sleep(2)
	print "You squint your eyes to see if you can make out anything in the room." 
	time.sleep(2)
	print " You kinda see something in the corner." 
	time.sleep(2)
	print "It looks like someone crouched in the corner." 
	time.sleep(2)
	print "It looks like someone crouched in the corner. Facing away." 	
	print "It looks like the 'person' is wearing white clothing. Like a robe. But a little dirty..."
	time.sleep(2)
	print "You go into the room." 
	time.sleep(2)
	print "You get closer to the 'person' crouching in the corner." 
	time.sleep(2)
	print "...Then the door slams right behind you." 
	time.sleep(2)
	print "Startled, you quickly turn around." 
	time.sleep(2)
	print "Hmmm, A/C must have blown the door shut..."
	time.sleep(2)
	print "You turn around. The 'person' or whatever it was is now gone." 
	time.sleep(2)
	print "What the..." 
	time.sleep(2)
	print " you quickly scan the painfully dark room..." 
	time.sleep(2)
	print "As you scan the bed, you notice what looks like someone's feet quickly slide under the bed."
	time.sleep(2)
	print " She or it is under the bed..." 	
	print " You get closer to the bed..." 
	time.sleep(2)
	print "You muster up the courage to take a peek under the bed." 
	time.sleep(2)
	print "Once you take a peek, you are face to face with an extremely pale face with glowing red eyes." 
	time.sleep(2)
	print "..." 
	time.sleep(3) 
	print """/ /         \ \
/ / -\-----/- \ \
| \/  \   /  \/ |
| /    \ /    \ |
\/ __   /   __ \/
/ /  \     /  \ \
| |   \   /   | |
| | . | _ | . | |
| \___// \\___/ |
 \     \_/     /
  \___     ___/
   \ \     / /
    \ vvvvv /
    | (   ) |
    | ^^^^^ |
    \_______/""" 
	Ending() 
	
def Upstairs(): 
	print "Once upstairs, you notice the only that has a light on is at the end of the hall to the right." 
	time.sleep(2)
	print "As you're looking down the hall to the room, the light in the room cuts off." 
	time.sleep(2)
	print "The hall is now dark."
	time.sleep(2)
	print "..." 
	time.sleep(2)
	print "You can barely see. The air gets a slight chill..." 
	time.sleep(2)
	print "Do you decide to go (Go down the hall) or (Head back downstairs)?" 
	
	choice_1 = raw_input() 
	if choice_1 == "Go down the hall": 
		print "You decide to head down the hall..."
		Hall() 
	elif choice_1 == "Head back downstairs": 
		dead() 
	else: 
		print "You must decide.."
		Upstairs() 
	
def Kitchen(): 
	print "You are now in the kitchen." 
	time.sleep(2)
	print "You look over to the right.." 
	time.sleep(2)
	print "You see someone at the table. Looks they're eating." 
	time.sleep(2)
	print "you walk over to the person..." 
	time.sleep(2)
	print "They're facing away from you." 
	time.sleep(2)
	print "As you walk to the person, the person quickly turns around to face you." 
	time.sleep(2)
	print "..."
	time.sleep(2)
	print """ / /         \ \
/ / -\-----/- \ \
| \/  \   /  \/ |
| /    \ /    \ |
\/ __   /   __ \/
/ /  \     /  \ \
| |   \   /   | |
| | . | _ | . | |
| \___// \\___/ |
 \     \_/     /
  \___     ___/
   \ \     / /
    \ vvvvv /
    | (   ) |
    | ^^^^^ |
    \_______/"""
	
	Ending() 
	

def Go_inside(): 
	print "You are now inside the home..."
	time.sleep(1) 
	print "As you step inside the home, you hear a thud upstair. Sounds like someone fell upstairs." 
	time.sleep(1) 
	print "At the same time, you hear a sound from the dimly lit kitchen." 
	time.sleep(2)
	print "The kitchen is about 20 feet ahead of you." 
	time.sleep(2)
	print "Do you go to the (Kitchen) or do you go (Upstairs?)" 
	choice_a = raw_input(" ") 
	if choice_a == "Upstairs": 
		Upstairs() 
	elif choice_a == "Kitchen": 
		Kitchen() 
		
	
print "It is Halloween. The temperature is roughly around 55 degrees."
time.sleep(1)
print "You are out trick or treating with your kids and S/O" 
time.sleep(1)
print "You come across a two-story home. Only one light on the second floor is on." 
time.sleep(1)
print "As you approach the house you notice the front door is ajar.."
time.sleep(2)
print "You notice a shadow-like figure quickly flash past the doorway." 
time.sleep(1)
print "Your kids tell you that they've got enough candy and they're ready to head home."
time.sleep(1)
print "Something about the house intrigues you."
time.sleep(1) 
print "You hear the kids but all you can do is stare at the home." 
print "Your S/O all of a sudden, gets a little queasy and light-headed and needs to head to the restroom and fast." 
time.sleep(1) 
print "Your S/O agrees to take the kids home while you agree to catch up with them." 
time.sleep(1) 
print "You think something is odd about the home." 
print "You're tempted to investigate. Just in case no one is in danger inside the home." 
time.sleep(1) 

print "What do you do? (Go to the door) or (head home)?" 
choice = raw_input(" ") 
if choice == "Go to the door": 
	print "You head to the door when you hear a faint scream. Sounds like it came from upstairs."
	Go_inside() 
elif choice == "head home": 
	print "You decide to just head home with the family when you hear a blood curdling scream come from the house." 
	print "Something bolts out of the house. It heads towards you..." 
	print "..." 
	dead() 
	 
	


