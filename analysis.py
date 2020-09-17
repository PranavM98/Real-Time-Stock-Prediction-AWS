

def moving_average(df):
    ma=0
    print("IN")
    ma=sum(df.iloc[-5:,3])/5
    return ma
    
def dowjones(djprice,dj):
    dj.append(djprice)
    if len(dj)==1:
        return 0
        
    else:
        return dj[len(dj)-1]-dj[len(dj)-2]+1
    