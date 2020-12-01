f= open('./input_file.txt')
txt = f.read()
txt_list = txt.split()

for i in range (0, len(txt_list)):
    txt_list[i] = int(txt_list[i])


for i in range (0, len(txt_list)-1):
    for j in range (i+1, len(txt_list)):
        a = txt_list[i] + txt_list[j]
        if a == 2020:
            print(i, j)
            print(txt_list[i] * txt_list[j])

# a = range(0, 10)
# aa = [1, 3]
# aa < 3
# for i in a:
#     print(i)
# #for i in range (0, len(txt_list)) < len(txt_list[i]):


#print(len(txt_list)) #200
#    print(i + (i+1))
