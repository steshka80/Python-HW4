# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
stepen = ["⁰","¹","²","³","⁴","⁵","⁶","⁷","⁸","⁹"]
dict1 = {}
dict2 = {}
result = ""
def bigdigit_to_stepen (digit):
    temp_step = ""
    for i in digit:
        temp_step += stepen[int(i)]
    return(temp_step)
def file_to_dict(xstr, dict):
    st_with_minus = xstr.replace("-","+-")
    temp_str = st_with_minus.split("+")
    for item in temp_str:
        if item != "":
            sub_temp_str=item.split("x")
            temp_stepen = ""
            for i in sub_temp_str[1]:
                temp_stepen += str(stepen.index(i))
def result_string(dictionary1, dictionary2):
    max1 = max(dictionary1.keys())
    max2 = max(dictionary2.keys())
    res=""
    for i in range (max(max1, max2), 0, -1):    
        a, b = 0, 0
        if i in dictionary1:
            a = dictionary1[i]
        if i in dictionary2:
            b = dictionary2[i]
        if (a+b) != 0:
            res=res+(str(a+b)+"x"+bigdigit_to_stepen(str(i))+"+")
    return(res)

with open("firstfile.txt") as file1:
    first_string = file1.readline()
with open("secondfile.txt") as file2:
    second_string = file2.readline()
file_to_dict(first_string, dict1)
file_to_dict(second_string, dict2)
result=result_string(dict1,dict2)
total_result=result.replace("+-","-")[:-1]
print(total_result)
with open ("sumfile.txt","w") as data:
    data.write(total_result)