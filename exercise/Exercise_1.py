List_Nums = []

while True:
    try:
        iNumStr = input("请输入以'#'结束的一些数: ")
        if iNumStr == "#":
            break
        Num = int(iNumStr) 
        List_Nums.append(eval(iNumStr))
    except ValueError:
        print("wrong") 

max_value = max(List_Nums)
min_value = min(List_Nums)
s = sum(List_Nums)
m = s/len(List_Nums)

print("总和为:{},平均数为:{},最大数为:{},最小数为:{}".format(s,m,max_value,min_value))
print(List_Nums)
