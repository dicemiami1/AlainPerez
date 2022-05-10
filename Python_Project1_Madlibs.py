# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to _______"
#youtuber = "Alain Perez" # some string variable

#print("subscribe to " + youtuber)
#print("subscribe to {}".format(youtuber))
#print(f"subscribe to {youtuber}")

adj = input("adjective: ")
verb1 = input("verb: ")
verb2 = input("verb: ")
verb3 = input("verb: ")


madlib = f"Computer programming is an {adj} experience for me because \
I like to find {verb1} to difficult problems. DevSecOps is my new found {verb2} and advanced \
neural networks such as {verb3}"

print(madlib)