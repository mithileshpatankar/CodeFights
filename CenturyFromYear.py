def centuryFromYear(year):
    if len(str(year))==4:
        if year%100==0:
            return (int(str(year)[:2]))
        else:return(int(str(year)[:2])+1)
    elif len(str(year))==3:
        if year%100==0:
            return (int(str(year)[:1]))
        else:return(int(str(year)[:1])+1)
    elif len(str(year))==2:
        if year%10==0:
            return (int(str(year)[0]))
        else:return(int(str(year)[0])+1) 
    elif len(str(year))==1 and year!=0:
        return 1
    elif year==0:
        return 0
    elif len(str(year))==5:
        if year%100==0:
            return (int(str(year)[:3]))
        else:return(int(str(year)[:3])+1)
