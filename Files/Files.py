#help(open) ##opens the help info for the inbuilt method open

openedfile = open("README.md")
print(openedfile) ## prints metadata - (open file IO type of data). Not the contents of the file!

#help(openedfile) ## will then open help for the new variable you've made - can see there is a read function in there. 
                  ## help very useful to see what you can do with the file

filecontents = openedfile.read() ## makes a variable of the contents of the file

filecontents = filecontents + "\nI'm adding some useful contents as a test" # can then add to the file, the \n adds it on a new line
filecontents = filecontents + "\nand another new line here"
print(filecontents)

## README.md is a read only file so can't save into it! Would need to copy the contents to a new file in order to save it.

#writefile = open("README.md.new","w") # this makes a new variable of the README.md file that is a new copy that is writable
writefile = open("README.md.new", "a+")
writefile.write(filecontents)
print(writefile) # prints the metadata for the file - need to read it
contentswritefile = writefile.read()
print(contentswritefile)


openedfile.close() # to close the files
writefile.close()
print("Finished")