text = open('./Directories_and_Files4.txt', 'r')
cnt = 0

file_content = text.read()
lines = file_content.split("\n")
  
for i in lines:
    if i:
        cnt += 1
          
print(cnt)

text.close()