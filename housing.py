# storage array and quad regex
ret = []
quad_stuff = ['4', 'quad', 'four']


# open a text file to read and identify 4-single quads
with open('output.txt') as f:
    for line in f:
        if '*' not in line:
            print()
            line_arr = line.split("|")
            bad = ["---",  "--",  "-",  ' ', '\n', '']
            new_line_arr = []
            for value in line_arr:
                if value not in bad:
                    new_line_arr.append(value.lower())
            if len(new_line_arr) > 5:
                if 'single' in new_line_arr[-4] and new_line_arr[-3] in quad_stuff:
                    print(new_line_arr)
                    ret.append(new_line_arr)
                    
# write the desired quads to a text file
with open('available.txt', 'w') as f:
    for row in ret:
        f.write('\n')
        f.write(str(row))
        f.write('\n')
