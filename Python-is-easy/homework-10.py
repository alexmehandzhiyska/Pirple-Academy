import string

# string module constants
print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.ascii_lowercase)

print(string.digits)
print(string.hexdigits)
print(string.capwords('Hello world IT\'s me'))

text = string.Template('$name is $age years old.')
new_text = text.substitute(name='Ivan', age=20)
print(new_text)
