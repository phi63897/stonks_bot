import discord
import os
import pymongo
from pymongo import MongoClient
from stockDict import stockDictGen
import pandas as pd
from iexfinance.stocks import Stock
from datetime import datetime
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
from iexfinance.stocks import get_historical_data
import io

#comments to find line for each command:
# $help - Line 24
# $new - Line 51
# $resource - Line 57
'''
Pymongo Commands (For reference):
###
https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html
###
db = database
db.find({key:value}) - Can use any valid key-value pair in dict
# find_one_and_replace, find_one_and_delete... many more in documentation
db.insert({key:value}) - Must add all attributes else will auto-gen values
# Documents = the values stored in the db (ex. {"user_id" : user, "balance": 0} is one document)
db.update({key:value}, {"$set":{key:new_value}})
'''
client = discord.Client()
#generates python_dictionary used for term definitions
stockDict = stockDictGen()
#Sets up IEX api token
iex_token = os.getenv("iex_token")
# Sets up MongoClient
cluster = MongoClient(os.getenv("mongoPass"))
#set up user table
db = cluster["Users"]
users_db = db["UserData"]
#set up word table
word_db = db["word_dict"]
if not word_db.find_one({"word":"s&p 500"}) :
    print("inserted")
    word_db.insert_many(stockDict)


# User should be message.author (discord username)
def get_user_info(user):
    # returns in this format {"user_id": str, "balance": int, "shares": dict}
    query = users_db.find_one({"user_id": user})
    if not query: # if user does not exist add to users_db
        post = {"user_id": user, 
                "balance": 100000, 
                "shares": {},
                "total_assets": 100000
                } # ex. {appl: {type: type, amt: int}}
        users_db.insert_one(post)
        return post
    return query

@client.event
async def on_ready():
    print("Bot {0.user} logged in!".format(client))

@client.event
async def on_message(message):
    #do nothing on bot's own messages
    if message.author == client.user:
        return
    #handle $help command (provides help menu)
    elif message.content == "$help":
        #save channel 
        channel = message.channel
        mention = "<@{}>".format(message.author.id)

        #create embed object for help menu
        toEmbed = discord.Embed(title="investBot Help Menu", description= "{} please respond with a number 1-3".format(mention)) 
        #format and add help options
        options = "1. `about` \n"
        options+= "2. `commands` \n"
        options+= "3. `third field`\n"
        toEmbed .add_field(name = "Help options", value= options)

        #send embeded help menu to channel
        await message.channel.send(embed=toEmbed)

        def toCheck(mes):
            optionNum = ["1","2","3"]
            return (mes.content in optionNum) and mes.channel == channel
        
        #wait for user response to help menu
        msg = await client.wait_for('message', check=toCheck)

        #respond to appropriate 
        if msg.content == "1":
            await channel.send("{0.user} is a bot for helping beginner investors! We plan to add paper trading and helpful reference material for beginners!".format(client))
        elif msg.content == "2":
            temp = """1. `$dbuy ticker dollar_amount` \n 2. `$resource` \n 3. `$def term` 
            4. `$dsell ticker dollar_amount` \n 5. `$price ticker`\n 6. `$portfolio` \n 7. `$leaderboard` \n`$sbuy ticker shares` \n `$dsell ticker shares`"""
            toEmbed = discord.Embed(title="Commands", description = temp)
            await channel.send(embed=toEmbed)
        elif msg.content == "3":
            return
        
    #handle $new command (introduction to bot, should create account)
    elif message.content == "$new":
        get_user_info(message.author.id)
        mention = "<@{}>".format(message.author.id)
        await message.channel.send("Hello {}, I'm {1.user} and I'm here to help you start investing! ".format(mention, client))
        await message.channel.send("All of my commands can be found through the $help menu!")
    
    #handle $resource command (provides resource links)
    elif message.content == "$resource":
        #save channel 
        channel = message.channel
        mention = "<@{}>".format(message.author.id)
        #create embed object for help menu
        toEmbed = discord.Embed(title="investBot Resources", description= "{} please respond with a number 1-3".format(mention)) 
        #format and add resource options
        options = "1. `New investor!` \n"
        options+= "2. `Online brokers` \n"
        options+= "3. `third field`\n"
        toEmbed.add_field(name = "Help options", value= options)

        #send embeded help menu to channel
        await message.channel.send(embed=toEmbed)

        def toCheck(mes):
            optionNum = ["1","2","3"]
            return (mes.content in optionNum) and mes.channel == channel
        
        #wait for user response to help menu
        msg = await client.wait_for('message', check=toCheck)

        #respond to appropriate 
        if msg.content == "1":
            toEmbed = discord.Embed(title="General Resources") 
            #format and add general resources
            options = "1. `Investopedia:` https://www.investopedia.com/articles/basics/06/invest1000.asp#what-kind-of-investor-are-you \n"
            options+= "2. `NerdWallet:` https://www.nerdwallet.com/article/investing/how-to-start-investing \n"
            options+= "3. `NerdWallet:` https://www.nerdwallet.com/article/investing/how-to-invest-in-stocks\n"
            options+= "4. `Investors.com:` https://www.investors.com/how-to-invest/how-to-invest-in-stocks-stock-market-for-beginners \n"
            toEmbed.add_field(name = "Help options", value= options)
            #send embedded general resources
            await channel.send(embed=toEmbed)
        elif msg.content == "2":
            toEmbed = discord.Embed(title="Online Brokers")
            #format and add online brokers
            options = "1. `NerdWallet's Top 11 Online Brokers:` https://www.nerdwallet.com/best/investing/online-brokers-for-beginners \n"
            options+= "2. `StockBrokers.com Top 5 Online Brokers:` https://www.stockbrokers.com/guides/beginner-investors \n"
            options+= "3. `Motley Fool's The Ascent Top 8 Online Brokers:` https://www.fool.com/the-ascent/buying-stocks/best-online-stock-brokers-beginners \n"
        elif msg.content == "3":
            return
    
    #handle $def command (defining terms)
    elif message.content.startswith("$def"):
        #check that the command follows format '$def term'
        if len(message.content) < 6 or message.content[4] != " ":
            return
        else:
            term = message.content[4::]
            term = term.strip()
            lookup = word_db.find_one({"word": term})
            if not lookup:
                await message.channel.send( "{}: Sorry I don't have a definition for that term :(".format(term))
            else:
                definition = lookup["definition"]
                await message.channel.send( "{}: ".format(term) + definition)
    
    #handle $price command (providing historical data for ticker)
    elif message.content.startswith("$price"):
        command = message.content.strip().split()
        mention = "<@{}>".format(message.author.id)
        if len(command) != 2:
            return

        channel = message.channel

        #create embed object for price menu
        toEmbed = discord.Embed(title="Price History", description= "{} please respond with a number 1-4".format(mention)) 
        #format and add history options
        options = "1. `52 week history!` \n"
        options+= "2. `26 week history!` \n"
        options+= "3. `1 month history!`\n"
        options+= "4. `1 week history!`"
        toEmbed.add_field(name = "History options", value= options)
        
        #send embeded history menu to channel
        await message.channel.send(embed=toEmbed)

        def toCheck(mes):
            optionNum = ["1","2","3", "4"]
            return (mes.content in optionNum) and mes.channel == channel
        
        #wait for user response to history menu
        msg = await client.wait_for('message', check=toCheck)

        ticker = command[1]
        if msg.content == "1":
            weekNum = "52"
            start =  datetime.now() - relativedelta(years=1)
        elif msg.content == "2":
            weekNum = "26"
            start =  datetime.now() - relativedelta(days=182)
        elif msg.content == "3":
            weekNum = "4"
            start =  datetime.now() - relativedelta(days=30)
        elif msg.content == "4":
            weekNum = "1"
            start =  datetime.now() - relativedelta(days=7)

        end = datetime.now() - relativedelta(days=1)
        try:
            stock = Stock(ticker, token = iex_token)
            cur_price = stock.get_price().iat[0,0]
            df = get_historical_data(ticker, start, end, output_format='pandas', token=iex_token)
            df['close'].plot()
            plt.figure(figsize=(10,10))
            plt.plot(df.index, df['close'])
            plt.xlabel("date")
            plt.ylabel("$ price")
            plt.title("{} {}-Week Stock Price".format(ticker.upper(), weekNum))
            plt.savefig('price.png')
            with open('price.png', 'rb') as f:
                file = io.BytesIO(f.read())
            image = discord.File(file, filename='price.png')

            toEmbed = discord.Embed(title='{} {} Week Closing Price History'.format(ticker.upper(), weekNum))
            toEmbed.add_field(name = "{}".format(ticker.upper()), value = "Current Price: {}".format(cur_price))
            toEmbed.set_image(url=f'attachment://price.png')
            await message.channel.send(file=image, embed=toEmbed)
        except:
            await message.channel.send("Sorry {} is an invalid ticker".format(ticker.upper()))
        
    
    # handle $portfolio command (View own or another's portfolio)
    elif message.content.startswith("$portfolio"):
        user_id = message.author.id
        command = message.content.strip().split()
        mention = "<@{}>".format(message.author.id)
        if len(command) == 1:
            # show user's portfolio
            lookup = get_user_info(message.author.id)
        elif len(command) == 2:
            # show selected user's portfolio
            mention = command[1]
            command[1] = command[1][3:-1]
            user_id = int(command[1])
            lookup = users_db.find_one({"user_id": int(command[1])})
            if not lookup:
                await message.channel.send("{}: Sorry that user does not exist :(".format(mention)) 
        else:
            return
            
        toEmbed = discord.Embed(title="Portfolio", description= "{}'s portfolio".format(mention))
        toEmbed.add_field(name = ":moneybag: Balance", value = "${:,.2f}".format(lookup["balance"]), inline=False)
        new_total = lookup["balance"]
        if (len(lookup["shares"]) == 0):
            info = "None \n"
        else:
            info = ""
            for ticker, shares in lookup["shares"].items():
                stock = Stock(ticker, token = iex_token)
                cur_price = stock.get_price().iat[0,0]
                info += "`{}`: {:.3f} | ${:,.2f}\n".format(ticker.upper(), shares, shares*cur_price )
                new_total += shares*cur_price
        users_db.update_one({'user_id':user_id}, {'$set': {"total_assets": new_total}})
        toEmbed.add_field(name = ":bank: Total Assets", value = "${:,.2f}".format(new_total), inline=False)
        toEmbed.add_field(name = ":chart_with_upwards_trend: Shares", value = info, inline=False)
        await message.channel.send(embed=toEmbed)
        return
    
    # handle $buy ticker amount; command to buy stock with $amount
    elif message.content.startswith("$dbuy"):
        command = message.content.strip().split()
        mention = "<@{}>".format(message.author.id)
        lookup = get_user_info(message.author.id)
        if len(command) != 3:
            await message.channel.send("Please use format $buy <ticker> <amount>")
            return
        ticker = command[1]
        amount = float(command[2])

        try:
            stock = Stock(ticker, token = iex_token)
            cur_price = stock.get_price().iat[0,0]
            if cur_price == None:
                await message.channel.send("Sorry the requested stock {} is unavailable".format(ticker.upper()))
            elif amount > lookup["balance"]:
                await message.channel.send("Sorry the requested buy exceeds your balance!")
            else:
                shares = amount / float(cur_price)
                new_balance = lookup["balance"] - amount
                if ticker in lookup["shares"]:
                    lookup["shares"][ticker] += shares
                else:
                    lookup["shares"][ticker] = shares

                users_db.update_one({'user_id':message.author.id}, {'$set': {"shares": lookup["shares"]}})
                users_db.update_one({'user_id':message.author.id}, {'$set': {"balance": new_balance }})
                await message.channel.send("Success! You bought {:.3f} shares of {}".format(shares, ticker.upper()))
        except:
            await message.channel.send("Sorry the requested stock does not exist!")
    # handle $buy ticker shares; command to buy stock with # of shares
    elif message.content.startswith("$sbuy"):
        command = message.content.strip().split()
        mention = "<@{}>".format(message.author.id)
        lookup = get_user_info(message.author.id)
        if len(command) != 3:
            await message.channel.send("{} Please use format $buy <ticker> <shares>".format(mention))
            return
        ticker = command[1]
        shares = float(command[2])

        try:
            stock = Stock(ticker, token = iex_token)
            cur_price = stock.get_price().iat[0,0]
            if cur_price == None:
                await message.channel.send("Sorry the requested stock {} is unavailable".format(ticker.upper()))
            elif shares*cur_price > lookup["balance"]:
                await message.channel.send("Sorry the requested buy exceeds your balance!")
            else:
                new_balance = lookup["balance"] - shares*cur_price
                if ticker in lookup["shares"]:
                    lookup["shares"][ticker] += shares
                else:
                    lookup["shares"][ticker] = shares

                users_db.update_one({'user_id':message.author.id}, {'$set': {"shares": lookup["shares"]}})
                users_db.update_one({'user_id':message.author.id}, {'$set': {"balance": new_balance }})
                await message.channel.send("Success! You bought {:.3f} shares of {}".format(shares, ticker.upper()))
        except:
            await message.channel.send("Sorry the requested stock does not exist!")


    # handle $dsell ticker amount; command to sell stock by $amount
    elif message.content.startswith("$dsell"):
        command = message.content.strip().split()
        lookup = get_user_info(message.author.id)
        if len(command) != 3:
            await message.channel.send("Please use format $sell <ticker> <amount>")
            return
        ticker = command[1]
        amount = float(command[2])
        try:
            stock = Stock(ticker, token = iex_token)
            cur_price = stock.get_price().iat[0,0]
            # shares: {{appl: amount}, {nvda: amount}}
            # check if amount is valid (cannot sell more than you have)
            if ticker not in lookup["shares"]:
                await message.channel.send("Sorry you do not own any shares of {}!".format(ticker.upper()))
            elif amount > lookup["shares"][ticker] * cur_price:
                await message.channel.send("Sorry the requested sell exceeds your amount of shares!")
            else:
                shares = float(amount) / float(cur_price)
                new_balance = lookup["balance"] + (shares * float(cur_price))
                lookup["shares"][ticker] -= shares
                if lookup["shares"][ticker] == 0:
                    lookup["shares"].pop(ticker)

                users_db.update_one({'user_id':message.author.id}, {'$set': {"shares": lookup["shares"]}})
                users_db.update_one({'user_id':message.author.id}, {'$set': {"balance": new_balance }})
                await message.channel.send("Success! You sold {:.3f} shares of {}".format(shares, ticker.upper()))
        except:
            await message.channel.send("Sorry the requested stock does not exist!")

    # handle $ssell ticker shares; command to sell stock by shares
    elif message.content.startswith("$ssell"):
        command = message.content.strip().split()
        lookup = get_user_info(message.author.id)
        if len(command) != 3:
            await message.channel.send("Please use format $sell <ticker> <amount>")
            return
        ticker = command[1]
        shares = float(command[2])
        try:
            stock = Stock(ticker, token = iex_token)
            cur_price = stock.get_price().iat[0,0]
            # shares: {{appl: amount}, {nvda: amount}}
            # check if amount is valid (cannot sell more than you have)
            if ticker not in lookup["shares"]:
                await message.channel.send("Sorry you do not own any shares of {}!".format(ticker.upper()))
            elif shares > lookup["shares"][ticker]:
                await message.channel.send("Sorry the requested sell exceeds your amount of shares!")
            else:
                new_balance = lookup["balance"] + (shares * float(cur_price))
                lookup["shares"][ticker] -= shares
                if lookup["shares"][ticker] == 0:
                    lookup["shares"].pop(ticker)

                users_db.update_one({'user_id':message.author.id}, {'$set': {"shares": lookup["shares"]}})
                users_db.update_one({'user_id':message.author.id}, {'$set': {"balance": new_balance }})
                await message.channel.send("Success! You sold {:.3f} shares of {}".format(shares, ticker.upper()))
        except:
            await message.channel.send("Sorry the requested stock does not exist!")
            
    elif message.content.startswith("$leaderboard"):
        # Create a new field -> total assets
        for x in users_db.find():
            print(x)
        top_10 = []
        # for k,v in users_db["shares"].items()
        toEmbed = discord.Embed(title="Leaderboard", description= "Highest amount of assets (balance + shares)")
        options = "Under Construction"
        count = 1
        #for x in top_10:
        #    options += "{}. <@{}> : ${:,.2f} \n".format(count, x["user_id"], x["total_assets"])
        #    count+=1
        toEmbed.add_field(name = "TOP 10", value= options)
        await message.channel.send(embed=toEmbed)
        

            

#connect to discord bot using bot token
client.run(os.getenv('discordToken'))
