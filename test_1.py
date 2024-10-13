myـfamily = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011},
}

for key, child in myـfamily.items():
    # print(child)
    main_key = key
    print (key , end=' ')
    for data_key in child:
        
        if key:
            print (data_key ,child[data_key] , end=' ')
            


# str_test="salam"
# for word in str_test:
#     print(word)
# for i in range(len(str_test)):
#     print(str_test[i])
