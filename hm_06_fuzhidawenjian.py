# 1.da kai
file_read = open("README")
file_write = open("README[fu jian]", "w")

# 2.du xie
while True:
    # du qu yi hang nei rong
    text = file_read.readline()

    # pan duan shi fou du qu dao nei rong
    if not text:
        break
    file_write.write(text)

# 3.guan bi
file_read.close()
file_write.close()