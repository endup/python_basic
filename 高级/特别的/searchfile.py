import os

rootdir="C:\\Users\s\Desktop"

for parent,dirnames,filenames in os.walk(rootdir):
	for filename in filenames:
		temp_filepath=parent+"\\"+filename
		print(temp_filepath)
