import os


filename = raw_input("What is the filename?    \n")
name = raw_input("What would you like to name the shortcut?    \n")
URL = raw_input("What is the URL of the link?   \n")


input_file = {'0_header': '[Desktop Entry]',
			   '1_format': 'Encoding=UTF-8',
			   '2_name': 'Name=' + name,
			   '3_type': 'Type=Link',
			   '4_url': 'URL=' + URL,
			   '5_icon': 'Icon=text-html'}

f = open(filename + ".desktop", "w+")

for key in sorted(input_file.keys()):
	print(input_file[key])
	f.write(input_file[key] + '\n')

f.close()



