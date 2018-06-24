name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

print("\tPython")
print("Languages:\nPython\nC\nJavaScript")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = ' python '
print(favorite_language)
print(favorite_language.rstrip())    # 移除末尾空白
print(favorite_language.lstrip())    # 移除开头空白
print(favorite_language.strip())    # 移除两端空白