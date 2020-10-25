myVar = input("What is your answer to my 1st question? (yes/no) ")  
if myVar == "yes":
  myNextVar = input("What is your answer to my 2nd question? (yes/no) ")
  if myNextVar == "yes":
    [another 1st "then" clause]
  elif myNextVar == "no":
    [another 2nd "then" clause]
  else:
    print("Answer my question! You didn't type yes or no.")
elif myVar == "no":
  [our 2nd "then" clause here]
else:
  print("Answer my question! You didn't type yes or no.")