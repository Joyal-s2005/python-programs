my_dict={'a':3,'b':1,'c':2}
ascending=dict(sorted(my_dict.items(),key=lambda x:x[1]))
descending=dict(sorted(my_dict.items(),key=lambda x:x[1],reverse=True))
print("Ascending:",ascending)
print("Descending:",descending)