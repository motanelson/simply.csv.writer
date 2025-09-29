print("\033c\033[43;30m\nfile to save?")

def saves(files,arrays):
    f1=open(files,"w")
    for n in arrays:
        l=False
        for nn in n:
             if l:
                 f1.write(", "+str(nn))
             else:
                 f1.write(str(nn))
             l=True
        f1.write("\n")                
a=[['arm', 'arm6'], ['arm', 'arm7'], ['x86', '8086'], ['x86', '80186'], ['x86', '80286'], ['x86', '80386'], ['x86', '80486']]
saves("my.csv",a)