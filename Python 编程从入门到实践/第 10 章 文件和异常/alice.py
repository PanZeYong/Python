filename = 'alice.txt'

try:
    with open(filename) as file:
        contents = file.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    number_words = len(words)
    print("The file " + filename + " has about " + str(number_words) + " words.")