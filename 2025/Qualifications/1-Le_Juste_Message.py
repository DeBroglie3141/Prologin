N, message, juste_message, truc = int(input()), str(input()), '', 0

for i in range(N) :
    l = message[i]
    if l in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] :
        if int(l) > truc :
            juste_message += l
        truc = int(l)
    else :
        juste_message += l

print(juste_message)


