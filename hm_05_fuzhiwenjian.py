# 1.da kai
file_read = open("README")
file_write = open("README[fu jian]", "w")

# 2.du xie
text = file_read.read()
file_write.write(text)
# 3.guan bi
file_read.close()
file_write.close()