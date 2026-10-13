product1Name = "Green Tea"
product2Name = "Black Tea"
product3Name = "White Tea"

#print(product1Name)
#print(product2Name)
#print(product3Name)

productsNames = ["Green Tea", "Black Tea", "White Tea"]

#ctrl + k, så c for å kommentere ut flere

# print(productsNames[0])
# print(productsNames[1])
# print(productsNames[2])

#for productName in productsNames:
#   print(productName)

#print(productNames[3]) Indexerror: list index out of range

#for i in range(3):
#    print(f"{i+1}. {productsNames[i]}")

mixed_list = ["Name", 25]

#for item in mixed_list:
 #   print(item)

productsNames.append("Brown Tea")
productsNames.insert(2, "Yellow Tea")

productsNames[0] = "Purple Tea"

#for productName in productsNames:
#    print(productName)

#print(len(productsNames))
#print(min(productsNames))
#print(max(productsNames))

#print(productsNames[1:4:2])
#print(productsNames[::-1])

print("White Tea" in productsNames)
print("Orange Tea" not in productsNames)