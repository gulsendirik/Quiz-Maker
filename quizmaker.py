#!/usr/bin/python


import random

filename=open("questions.txt",'r')
f=set(filename.readlines())
filename.close()

filename=open("movie_questions.txt",'r')
m=set(filename.readlines())
filename.close()

answer=open("answer.txt")
answer2=open("answer2.txt")
answer3=open("answer3.txt")


question = raw_input("Would you like to create Quiz Questions?(Yes or No)\n")
number = raw_input("How many questions do you get in the quiz?(10,15,20)\n")
ans = raw_input("Would you like to get answer key?(Yes or No)\n")
sub = raw_input("Which subject about do you want to create a quiz? (General,Movie or Music)\n")

if question == "Yes":
	print "Questions\n"
	if number == "10" and sub == "General":	
		print "You have selected 10 question"
		print(list(f)[0],list(f)[1],list(f)[2],list(f)[3],list(f)[4],list(f)[5],list(f)[6],list(f)[7],list(f)[8],list(f)[9])
		if ans == "Yes":
			print "Answers"
			print(answer.read())
	elif number == "10" and sub == "Movie":
		print "You have selected 10 question"
		print(list(m)[0],list(m)[1],list(m)[2],list(m)[3],list(m)[4],list(m)[5],list(m)[6],list(m)[7],list(m)[8],list(m)[9])
		if ans == "Yes":
			print "Answers"
			print(answer.read())
	elif number == "15":	
		print "You have selected 15 question"
		print(list(f)[0],list(f)[1],list(f)[2],list(f)[3],list(f)[4],list(f)[5],list(f)[6],list(f)[7],list(f)[8],list(f)[9],list(f)[10],list(f)[11],list(f)[12],list(f)[13],list(f)[14])
		if ans == "Yes":
			print "Answers"
			print(answer2.read())
	elif number == "20":	
		print "You have selected 20 question"
		print(list(f)[0],list(f)[1],list(f)[2],list(f)[3],list(f)[4],list(f)[5],list(f)[6],list(f)[7],list(f)[8],list(f)[9],list(f)[10],list(f)[11],list(f)[12],list(f)[13],list(f)[14],list(f)[15],list(f)[16],list(f)[17],list(f)[18],list(f)[19])
		if ans == "Yes":
			print "Answers"
			print(answer3.read())
	else:
		print "Quit"
		
else: 
	print "Quit"


