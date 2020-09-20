

def moving_average(df):
    ma=0
    ma=sum(df.loc[-5:,'Price'])/5
    return ma
    
def price_difference(ind_price,ind):
    ind.append(ind_price)

    if len(ind)==1:
        return 0
        
    else:
        return ind[len(ind)-1]-ind[len(ind)-2]