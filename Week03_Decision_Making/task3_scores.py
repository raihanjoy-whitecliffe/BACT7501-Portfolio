scores=[65, 72, 80, 55, 90, 68, 77]
count=0
for i in scores:
    if i>70:
        count+=1
print('Student scoring above 70: ', count)
for i in scores:
    if i >= 60:
        print(i, 'pass')
    else:
        print(i, 'fail')