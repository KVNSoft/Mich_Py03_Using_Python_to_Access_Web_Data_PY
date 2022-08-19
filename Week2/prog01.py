import re

#NAME_FILE01 = r"Week 1 Sample Text.txt"
NAME_FILE01 = r"D:\Prog001\Mich_Py03_Using_Python_to_Access_Web_Data_PY\Week2\regex_sum_1629165.txt"
my_list01 = list()

try:
    with open(NAME_FILE01) as my_file01:
        for line in my_file01:
            line02 = line.rstrip()
            my_list02 = re.findall(r"([0-9]+)", line)

            for var01 in my_list02:
                my_list01.append(float(var01))

    print(sum(my_list01))
            
except FileNotFoundError as e:
    print("We can not find this file!!!", e)
except Exception as e:
    print("ERROR!!!", e)