# Double(" ") or single(' ') quotes both work

# Possible to use them inside the string as long as it doesn't match quotes outside

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Multi-line strings (works same with double or single quotes)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are arrays of characters

a = "Hello, World!"
print(a[1]) # prints "e"

print(len(a)) # prints length

# Looping through letters

for x in "banana":
    print(x)


# Checking if a sequence of characters is in the string 

txt = "The best things in life are free!"
print("free" in txt)

# Checking with if statement

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")


# Checking with if NOT in the string

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")