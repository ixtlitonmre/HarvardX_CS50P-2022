def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]
dic_coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print (total(100, 50, 25), "Knuts")
print (total(coins[0], coins[1], coins[2]), "Knuts")
print (total(galleons=100, sickles=50, knuts=25), "Kunts")
#The previous 3 lines do the same than this one but here with the * we are unpacking the coins list
print (total(*coins), "Knuts")
#Using the dictionary
print (total(dic_coins["galleons"], dic_coins["sickles"], dic_coins["knuts"]), "Kunts")
#Unpacking a dictionary requires 2 * and is the same than the previous line
print (total(**dic_coins), "Knuts")
