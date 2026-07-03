shopping_cart=[40, 70, 60, 80]
total= 0
gst= [.15, .20, .40, .70]
for i in shopping_cart:
    for j in i:
        k= i +j
        total= total+k
print(total)
