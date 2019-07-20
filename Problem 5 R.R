# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

  max_number = 2.432902e+17
  
  counter = 2.32e+08
  counter2 = 2.33e+08
  repeat {
    if ((counter %% 11 == 0) & (counter %% 12 == 0) & (counter %% 13 == 0) & (counter %% 14 == 0) & (counter %% 15 == 0) & (counter %% 16 == 0) & (counter %% 17 == 0) & (counter %% 18 == 0) & (counter %% 19 == 0) & (counter %% 20 == 0)) {
      print (paste("FINAL STOP: ", counter))
      break
    } else {
      if (counter >= counter2) {
        print (paste0("STOP: " , counter))
        counter2 = counter2 + 1.0e+06
      }
      counter = counter + 1}
  }
  
  
#FINAL STOP:  232792560"
