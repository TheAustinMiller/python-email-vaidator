def find_at_index(email):
  for i in range(len(email)):
    if email[i] == "@":
      return i

def find_period_index(email):
  for i in range(len(email)):
    if email[i] == ".":
      return i

def no_special(msg):
  if "*" in msg:
    return False
  if "-" in msg:
    return False
  if "&" in msg:
    return False
  if "!" in msg:
    return False
  if "#" in msg:
    return False
  if "$" in msg:
    return False
  if "%" in msg:
    return False
  if "^" in msg:
    return False
  if "(" in msg:
    return False
  if ")" in msg:
    return False
  if "[" in msg:
    return False
  if "]" in msg:
    return False
  if "{" in msg:
    return False
  if "}" in msg:
    return False
  if "_" in msg:
    return False
  if "'" in msg:
    return False
  if "\"" in msg:
    return False
  if "\\" in msg:
    return False
  if ":" in msg:
    return False
  if ";" in msg:
    return False
  return True

def is_valid(email):
  if not "@" in email:
    return False
  if " " in email:
    print("space")
    return False
  atIndex = find_at_index(email)
  if not "." in email[atIndex:]:
    print(".")
    return False
  periodIndex = find_period_index(email)
  body = email[:atIndex]
  prefix = email[atIndex + 1:periodIndex]
  domain = email[periodIndex + 1:]
  flag = True
  if not len(body) >= 4 and not no_special(body):
    flag = False
  if not len(prefix) >= 3 and not no_special(prefix):
    flag = False
  if not len(domain) >= 1 and not no_special(domain):
    flag = False
  return flag

print("AJ's Email Validation Service:")
x = input("Please enter an email: ")
flag = is_valid(x)
if flag:
  print("This email is valid")
else:
  print("This email is not valid")
