

def moving_average(df):
    ma=0
    print("IN")
    ma=sum(df.iloc[-5:,2])/5
    return ma
    