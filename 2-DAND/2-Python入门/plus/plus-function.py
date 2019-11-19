# https://cn.udacity.com/course/shell-workshop--ud206
def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2
print(cylinder_volume(10,3))

def readable_timedelta(days):
    """Print the number of weeks and days in a number of days."""
    #to get the number of weeks we use integer division
    weeks = days // 7
    #to get the number of days that remain we use %, the modulus operator
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)
print(readable_timedelta(20))

# https://classroom.udacity.com/nanodegrees/nd002-cn-basic-vip/parts/37aa085f-a2c7-48ac-8070-f17f5be7f2dd/modules/f0fc5dc7-15a0-41ea-acae-66eb3b761ae1/lessons/ee5eb8d0-dc89-4b42-8feb-9fbe35a5fecd/concepts/6f282eeb-c6fe-4ef3-a80b-c1fde200daeb

def population_density(population, land_area):
    """Calculate the population density of an area.

    population: int. The population of the area
    land_area: int or float. This function is unit-agnostic, if you pass
               in values in terms of square km or square miles the
               function will return a density in those units.
    """
    return population / land_area

print(population_density(10000, 444))

print(population_density(1000, 4))

# print(help(population_density))
# 上面这个会卡在terminal的输出（vscode）
print(population_density.__doc__)

# 函数如果没有return可以以输出内容（根据函数内容）
# 但是如果print函数的话会发现输出是None
# 解释见 https://classroom.udacity.com/nanodegrees/nd002-cn-basic-vip/parts/37aa085f-a2c7-48ac-8070-f17f5be7f2dd/modules/f0fc5dc7-15a0-41ea-acae-66eb3b761ae1/lessons/ee5eb8d0-dc89-4b42-8feb-9fbe35a5fecd/concepts/6f282eeb-c6fe-4ef3-a80b-c1fde200daeb#

# 文件读取
# https://classroom.udacity.com/nanodegrees/nd002-cn-basic-vip/parts/37aa085f-a2c7-48ac-8070-f17f5be7f2dd/modules/f0fc5dc7-15a0-41ea-acae-66eb3b761ae1/lessons/0d7cfb06-4a38-4dde-b6df-aae686ab3bf0/concepts/d2d034b0-5c87-4572-bac4-b9508755609d#
camelot_lines = []

with open("flying_circus_cast.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(type(camelot_lines))
# print(camelot_lines[:3])


def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    with open(filename) as f:
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
        for l in f:
            # t = l.split(',')[0]
            # print(t)
            cast_list.append(l.split(',')[0].strip())
    return cast_list

print(create_cast_list('flying_circus_cast.txt')[:3])