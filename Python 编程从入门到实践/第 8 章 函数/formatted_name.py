def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
        
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix', 'lee')
print(musician)

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def city_country(city, country):
    print(city + ", " + country)

def make_album(name, album, count=0):
    singer = {
        "name": name,
        "album": album
    }

    if count > 0:
        singer['count'] = count

    return singer

while True:
    print("Please input the singer's name: ")
    print("(enter 'q' at any time to quit)")

    name = input("name: ")
    if name == 'q':
        break

    print("Please input the singer's album: ")
    print("(enter 'q' at any time to quit)")
    album = input("album: ")
    if album == 'q':
        break

    print(make_album(name, album))
# city_country("深圳", "中国")
# city_country("上海", "中国")
# city_country("纽约", "美国")