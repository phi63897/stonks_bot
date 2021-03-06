
#function to generate dicitonary of terms
def stockDictGen():
    stockDict = []
    stockDict.append({"word": "stock", "definition": "the capital raised by a business or corporation through the issuing of shares"})
    stockDict.append({"word":"share",  "definition": "the piece of paper that signifies ownership of the company"})
    stockDict.append({"word":"position" ,  "definition": "another term for owning stock. Ex: I have a position in Jim’s Coffee Company."})
    stockDict.append({"word":"stock price" ,  "definition": "the public price at which buyers and sellers trade shares"})
    stockDict.append({"word":"market price" ,  "definition": "the public price at which buyers and sellers trade shares"})
    stockDict.append({"word":"buyer" ,  "definition": "Someone who wants to purchase shares of a stock, gaining ownership"})
    stockDict.append({"word":"seller" ,  "definition": "Someone who wants to sell their shares of a stock, losing ownership"})
    stockDict.append({"word":"stock broker" ,  "definition": "Person/Company who executes trades for you. Example: E-trade, Scottrade, Edward Jones, etc."})
    stockDict.append({"word":"stock account" ,  "definition": "Holds your different shares/positions in stocks, usually set up through a broker"})
    stockDict.append({"word":"bid" ,  "definition": "Current highest price someone’s willing to pay for a stock"})
    stockDict.append({"word":"ask" ,  "definition": "Current lowest price someone’s willing to sell the stock at"})
    stockDict.append({"word":"spread" ,  "definition": "Difference between current bid and ask price of the stock"})
    stockDict.append({"word":"volume" ,  "definition": "Amount of shares being traded"})
    stockDict.append({"word":"volatility" ,  "definition": "How quickly stock prices move"})
    stockDict.append({"word":"liquidity" ,  "definition": "Ease of getting in and out of a position, volume level of a stock"})
    stockDict.append({"word":"buy" ,  "definition":  "Purchasing a stock. Increases the demand for a stock"})
    stockDict.append({"word":"sell",  "definition": "Selling a stock. Increases the supply for a stock"})
    stockDict.append({"word":"short sell" ,  "definition": "Borrowing shares from broker, selling them and holding the money in your account hoping stock price falls and then you buy back the borrowed shares for a cheaper price and keep the difference"})
    stockDict.append({"word":"short",  "definition": "Borrowing shares from broker, selling them and holding the money in your account hoping stock price falls and then you buy back the borrowed shares for a cheaper price and keep the difference"})
    stockDict.append({"word":"buy to cover" ,  "definition": "Buying back the borrowed shares, ending your short sell trade"})
    stockDict.append({"word":"cover" ,  "definition": "Buying back the borrowed shares, ending your short sell trade"}) 
    stockDict.append({"word":"market order" ,  "definition": "An order placed at current market price, executes quickly usually" })
    stockDict.append({"word":"limit order" ,  "definition":  "An order placed to trade stock at a certain specified price or else order doesn’t get filled"})
    stockDict.append({"word":"limit" ,  "definition":  "An order placed to trade stock at a certain specified price or else order doesn’t get filled"})
    stockDict.append({"word":"stop loss order" ,  "definition":  "Order placed to liquidate/sell position when a specified price is reached or passed to stop any further losses."})
    stockDict.append({"word":"stop loss" ,  "definition":  "Order placed to liquidate/sell position when a specified price is reached or passed to stop any further losses."})
    stockDict.append({"word":"trailing stop loss order" ,  "definition":  "A stop loss order that adjusts as stock price changes to lock in more and more profit potential"})
    stockDict.append({"word":"trailing stop loss" ,  "definition":  "A stop loss order that adjusts as stock price changes to lock in more and more profit potential"})
    stockDict.append({"word":"moving average" ,  "definition":  "Average volume for the past X days. Helps you know how a stock’s price is behaving compared to volume in a term period."})
    stockDict.append({"word":"moves on low volume" ,  "definition":  "When a stock is thinly traded meaning there is low volume, price movement can’t be taken as serious because little trading volume leaves people less options for prices to buy and sell to the spread is bigger usually."})
    stockDict.append({"word":"moves on high volume" ,  "definition":  "A heavily traded stock gives more proof that a price move is legit as a lot of people are trading and interested in buying or selling the stock for some reason. This should cause you to take a closer look at why."})
    stockDict.append({"word":"market valuation" ,  "definition":  "Company Value (Shares x Stock Price)"})
    stockDict.append({"word":"market cap" ,  "definition":  "Company Value (Shares x Stock Price)"})
    stockDict.append({"word":"shares outstanding" ,  "definition":  "the # of shares issued by the company."})
    stockDict.append({"word":"outstanding shares" ,  "definition":  "the # of shares issued by the company."})
    stockDict.append({"word":"float" ,  "definition":  "# of shares available to public to trade"})
    stockDict.append({"word":"restricted shares" ,  "definition":  "shares owned by the company insiders still, not trade-able by the public. Insiders can sell these to raise more capital causing the float to increase."})
    stockDict.append({"word":"micro cap" ,  "definition":  "company valued under $250 million (most penny stocks)"})
    stockDict.append({"word":"small cap" ,  "definition":  "company valued between $250 million and $1 billion"})
    stockDict.append({"word":"mid cap" ,  "definition":  "company valued between $1 billion and $10 billion"})
    stockDict.append({"word":"large cap" ,  "definition":  "company valued over $10 billion"})
    stockDict.append({"word":"independent investors" ,  "definition":  "Traders who use personal capital/leverage to trade"})
    stockDict.append({"word":"independent traders" ,  "definition":  "Traders who use personal capital/leverage to trade"})
    stockDict.append({"word":"institutional investors" ,  "definition":  "Traders working for firms"})
    stockDict.append({"word":"institutional traders" ,  "definition":  "Traders working for firms"})
    stockDict.append({"word":"distressed investors" ,  "definition":  "Traders who buy suffering companies and turn them around"})
    stockDict.append({"word":"distressed traders" ,  "definition":  "Traders who buy suffering companies and turn them around"})
    stockDict.append({"word":"value investors" ,  "definition":  "Invest in stocks that have solid fundamentals"})
    stockDict.append({"word":"value traders" ,  "definition":  "Invest in stocks that have solid fundamentals"})
    stockDict.append({"word":"growth investors" ,  "definition":  "Invest in fast growing companies. High % growth seen in the EPS of recent quarter compared to year ago quarter."})
    stockDict.append({"word":"growth traders" ,  "definition":  "Invest in fast growing companies. High % growth seen in the EPS of recent quarter compared to year ago quarter."})
    stockDict.append({"word":"penny stocks" ,  "definition":  "Investing in stocks under $5 but usually stocks under $1"})
    stockDict.append({"word":"hedge funds" ,  "definition":  "Huge million and billion dollar funds made up of high net worth individuals. Usually focus on high priced stocks and less risk so not anything to worry about in penny stocks."})
    stockDict.append({"word":"mutual funds" ,  "definition":  "Pooled money by many investors used on higher priced stocks usually. Mutual funds can have down years and the managers still reap huge gains unlike hedge fund managers who only do well when they perform well."})
    stockDict.append({"word":"sec" ,  "definition":  "They regulate the stock market and can hault stocks and eliminate scam companies."})
    stockDict.append({"word":"securities exchange commission" ,  "definition":  "They regulate the stock market and can hault stocks and eliminate scam companies."})
    stockDict.append({"word":"ipo" ,  "definition":  "Private company sells shares to public for first time to raise capital."})
    stockDict.append({"word":"initial public offering" ,  "definition":  "Private company sells shares to public for first time to raise capital."})
    stockDict.append({"word":"merger" ,  "definition":  "two companies combine to cut costs and get rid of wasted labor and resources. More efficient"})
    stockDict.append({"word":"ipo share lock up" ,  "definition":  "After an IPO, insiders are restricted from trading for 6 months usually but sometimes up to a year or two. They can’t sell their shares until the lock up period ends."})
    stockDict.append({"word":"secondary offering" ,  "definition":  "When insiders and executives of the company sell stock for personal gain like if they received stock as part of compensation package or bonus. Capital goes to them personally and not the company."})
    stockDict.append({"word":"margin " ,  "definition":  "using money borrowed from broker to trade stocks"})
    stockDict.append({"word":"short squeeze" ,  "definition":  "Short seller buys to cover position when price is going up and not down like they wanted. Short squeeze results in more demand to buy stock raising the price."})
    stockDict.append({"word":"pre borrow" ,  "definition":  "Ability to reserve shares from your broker ahead of time to borrow when you short sell"})
    stockDict.append({"word":"pink sheets" ,  "definition":  "tiny companies, penny stock type companies, very volatile"})
    stockDict.append({"word":"otc bulletin board" ,  "definition":  "Non Nasdaq listed stocks that rarely trade over $5"})
    stockDict.append({"word":"otcbb" ,  "definition":  "Non Nasdaq listed stocks that rarely trade over $5"})
    stockDict.append({"word":"nasdaq" ,  "definition":  "American stock exchange at One Liberty Plaza"})
    stockDict.append({"word":"russell 2000" ,  "definition":  "represents the 2000 smallest publicly traded companies but doesn’t include pink sheet and OTCBB stocks"})
    stockDict.append({"word":"s&p 500" ,  "definition":  "The 500 biggest companies by market cap"})
    stockDict.append({"word":"dow jones industrial average" ,  "definition":  "A price weighted index of 30 significant and actively traded blue chip stocks."})

    return stockDict
