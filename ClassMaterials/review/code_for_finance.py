import numpy as np
import pandas as pd
import pandas_datareader.data as web
from datetime import date



class RiskRatios:
    def __init__(self,symbol):
        self.symbol = symbol
        self.start_date = date(2017,1,1)
        self.end_date = date.today()
        self.data = self.get_data()
        self.returns = self.calculate_return()
        self.covariance = self.covariance()
        self.beta = self.calculate_beta()
        self.alpha = self.calculate_alpha()
    def get_data(self):
        portfolio = ['SPY', self.symbol]
        data = pd.DataFrame()
        for s in portfolio:
            data[s] = web.DataReader(s, 'google',self.start_date,self.end_date)['Close']
        print(data)
        return data
    def calculate_return(self):
        returns = np.log(self.data/self.data.shift(1))
        returns = returns.dropna()
        return returns
    def covariance(self):
        covariance = np.cov(self.returns.SPY, self.returns[self.symbol])
        return covariance
    def calculate_beta(self):
        beta = self.covariance[0, 1] / np.var(self.returns.SPY)
        return beta 
    def calculate_alpha(self):
        alpha = np.mean(self.returns[self.symbol])-(self.beta*np.mean(self.returns.SPY))
        return alpha



def main():
    TMPL = '''
    Stock: %s
    Beta: %s
    Alpha: %s
    '''
    stock_symbol = input("Please enter the symbol you want to see: ")
    b = RiskRatios(stock_symbol)
    alfa = (b.calculate_alpha())*12
    print(TMPL % (stock_symbol, b.calculate_beta(),alfa))





if __name__ == "__main__":
    main()
b = RiskRatios("AAPL")
print(b.get_data())