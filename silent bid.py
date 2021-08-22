
print("LETS THE AUCTION BEGIN")

is_next_player = True

store =  {}
case_list = []
while is_next_player:
  player = input("Enter Your Name: ")
  bid = int(input("Enter Bid Amount Rs "))
  store[player]=bid
  next_player = input("Next Player?  Yes or No: ").lower()
  if next_player =="no":
    is_next_player= False
  elif next_player=="yes":
    print("Lets do it again!")
    

maxval =0
winner = ""
print(store)
for item in store:
  if store[item] > maxval:
    maxval = store[item]
    winner=item
print(f"highest bidder is {winner} --- With Bid of Rs{maxval}")


