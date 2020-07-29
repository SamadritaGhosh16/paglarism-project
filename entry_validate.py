#entryvalidate
avoid=["'",'"','"""', "=", ">", "<",]

def quest_valid(inp):
    flag=0
    for i in inp:
        if i in avoid:
            flag=1
            break
        else:
            flag=0
    if flag==1:
        return False
    else:
        return True

def name_valid(inp):
    name_avoid=[".","/","!","@","#","$","%","^","&","*","-","=","+","`","~","(",")","{","}","|",";",":",",",".","\\","/"]
    flag=0
    for i in inp:
        if i in avoid or i in name_avoid or i.isdigit():
            flag=1
            break
        else:
            flag=0
    if flag==1:
        return False
    else:
        return True

def comp_valid(inp):
    flag=0
    for i in inp:
        if i in avoid:
            flag=1
            break
        else:
            flag=0
    if flag==1:
        return False
    else:
        return True

def call_valid(inp):
    if (len(inp)==10 and inp.isdigit() and inp!=" "):
        return True
    else:
        return False