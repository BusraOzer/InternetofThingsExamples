import lirc

sockid=lirc.init("lircApp", blocking = False)
codeIR=lirc.nextcode()
print(codeIR[0])
