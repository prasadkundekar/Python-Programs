def is_palindrome(s):
  s = s.lower().replace(" ", "")
  return s == s[::-1]

string1 = "madam"
string2 = "A man a plan a canal Panama"
string3 = "hello"

print(f"'{string1}' is a palindrome: {is_palindrome(string1)}")
print(f"'{string2}' is a palindrome: {is_palindrome(string2)}")
print(f"'{string3}' is a palindrome: {is_palindrome(string3)}")