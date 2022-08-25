def count_words(str):
    str = str.split()
    dict = {}
    for i in str:			
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    return dict	

print(count_words("oh what a day what a lovely day"))
print(count_words("don't stop believing"))

