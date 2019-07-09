# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

library(stringi)
palindrome = function (string) {
  if (string == stri_reverse(string)) {
    return (TRUE)
  } else {
    return (FALSE)
  }
}
empty_list = list()
counter = 999
while (counter > 99) {
  for (num in 999:100) {
    temp_res = counter * num
    if (palindrome(temp_res)) {
      empty_list = append(empty_list, temp_res)
    }
  }
  counter = counter - 1
}

indice = which.max(empty_list)
print (empty_list[indice])