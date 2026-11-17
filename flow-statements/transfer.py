# for i in range(10):
    # if i == 7:
    #     print("processing is enouggh please break")
    #     break
    # print(i)


cart = [10,20,40, 600, 700 ,801]
for item in cart:
    if item > 800:
        print('to place this order insurence must be required')
        break
    print(item)
else:
    print("congrats all items processed successfully")
