def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        pass
        # msg = "Sorry, the file " + filename + " does not exist."
        # print(msg)
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        number_words = len(words)
        print("The file " + filename + " has about " + str(number_words) + " words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dict.txt', 'little_women.txt', 'little_man.txt']
for filename in filenames:
    count_words(filename)