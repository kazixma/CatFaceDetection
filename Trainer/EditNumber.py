
text_file = open('log4.txt',"a")
with open('log.txt') as fp:
    for line in fp:
        oldline = line
        templine = line.split()
        newline = templine[0]+"  "+"1"+"  "+templine[2]+" "+templine[3]+" "+templine[4]+" "+templine[5]+"\n"
        text_file.write(newline)
