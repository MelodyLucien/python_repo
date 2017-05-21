#!/usr/bin/python3
import pickle

example_dict={1:"3",2:"4",3:"6",5:"100"}
pickle_out=open("dict.pickle","wb")
pickle.dump(example_dict,pickle_out)
pickle_out.close()



pickle_in=open("dict.pickle","rb")
example_dictin=pickle.load(pickle_in)

print(example_dictin)

print(example_dictin[5])


