import glob

text_file = open("neg.txt","w")
for filename in glob.glob('./image/neg/*.jpg'):  # assuming gif
    text_file.write(filename+"\n")