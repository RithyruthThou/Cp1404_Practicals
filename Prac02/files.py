# Write some data to the file first.
f = open('file.txt', 'w')
for s in ['This\n', "is a\n", "test\n"]:
    f.write(s)
f.close()

# The file now looks like this:
# file.txt
# >This
# >is a
# >test

# Now overwrite

new_lines = ['Some\n', 'New data\n']
f = open('file.txt', 'w+')
# Get the previous contents
lines = f.readlines()
# Overwrite
for i in range(len(new_lines)):
    f.write(new_lines[i])
f.close()