#Tip Calculator 
#Right now this script is rounding up the tip numbers 
raw_bill = raw_input("Total bill amount?: ") 
x = float(raw_bill)
tip10 = x*.10 
tip10 = int(tip10) 
tip15 = x*.15
tip15 = int(tip15) 
tip20 = x*.20 
tip20 = int(tip20) 
tip = int(float(raw_input("How much would you like to tip today?: ")))  

if tip == 10: 
	print "You will be tipping", tip10, "dollars today"
elif tip == 15: 
	print "You will be tipping", tip15, "dollars today" 
elif tip == 20: 
	print "You will be tipping", tip20, "dollars today. Wow so generous!" 
else: 
	print "Well, it looks you're doing the dishes today!" 

print "Thank you for coming today! I hope you all have a wonderful rest of your day!" 
raw_input() 

