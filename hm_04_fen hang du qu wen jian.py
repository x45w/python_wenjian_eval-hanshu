
file = open("README")

while True:
    text = file.readline()

    # pan duan shi fou du qu dao nei rong
    if not text:
        break
    print(text)


file.close()