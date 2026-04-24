import json
# Read "romeo_and_juliet.txt" (The full text of Shakespeare's Romeo and Juliet)
with open("romeo_and_juliet.txt", "r") as f:
    dwhndhn = f.read()
j = dwhndhn.split(" ")
jwis = {}
for word in j:
    if word in jwis:
        jwis[word] += 1
    else:
        jwis[word] = 1
print(jwis["Juliet"])
    
####
#### YOUR CODE HERE 
####

# Count how many times the word "Juliet" appears

####
#### YOUR CODE HERE 
####
