import sys
import random

number = random.randint(1,20)

question = raw_input("What is your question for the all knowing Magic 8 Ball?: \n")

if question=="":
	sys.exit()
elif len(question)<2:
	print "Type a legit question to get a magic answer"
elif number == 1:
	print "As I see it, yes"
elif number == 2:
	print "Ask again later"
elif number == 3:
	print "Better not tell you now"
elif number == 4:
	print "Cannot predict now"
elif number == 5 :
	print "Concentrate and ask again"
elif number == 6 :
	print "Don't count on it"
elif number == 7 :
	print "It is certain"
elif number == 8 :
	print "It is decidedly so"
elif number == 9 :
	print "Most likely"
elif number == 10 :
	print "My reply is no"
elif number == 11 :
	print "My sources say no"
elif number == 12 :
	print "Outlook good"
elif number == 13 :
	print "Outlook not so good"
elif number == 14 :
	print "Reply hazy, try again"
elif number == 15 :
	print "Signs point to yes"
elif number == 16 :
	print "Very doubtful"
elif number == 17 :
	print "Without a doubt"
elif number == 18 :
	print "Yes"
elif number == 19 :
	print "Yes, definitely"
elif number == 20 :
	print "You may rely on it"