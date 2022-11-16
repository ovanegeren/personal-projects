/*  
https://www.interviewcake.com/question/c/stock-price

First, I wanna know how much money I could have made yesterday if I'd been trading Apple stocks all day.

So I grabbed Apple's stock prices from yesterday and put them in an array called stockPrices, where:

The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
The values are the price (in US dollars) of one share of Apple stock at that time.
So if the stock cost $500 at 10:30am, that means stockPrices[60] = 500.

Write an efficient function that takes stockPrices and returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.

For example:
    int stockPrices[6] = {10, 7, 5, 8, 11, 9};
    size_t numStockPrices = 6;

    getMaxProfit(stockPrices, numStockPrices);
    // returns 6 (buying for $5 and selling for $11)


No "shorting"—you need to buy before you can sell. Also, you can't buy and sell in the same time step—at least 1 minute has to pass.
*/
#include <stddef.h>
#include <stdio.h>

#define NUM_STOCK_PRICES 10

int getMaxProfit(int *stocks_prices, size_t minutes){
    int i;
    if(!minutes){
        return 0;
    }

    int buy = stocks_prices[0];
    int sell = stocks_prices[0];
    int max_profits = 0;
    int profits = 0;

    for(i = 0; i < minutes; i++){
        if(stocks_prices[i] > buy){                    
            if(stocks_prices[i] > sell){            //if ticker price > sell price, sell at ticker price instead
                sell = stocks_prices[i];
            }
        }else{                          // if ticker price > buy price, retry buying and reset sell price
            buy = stocks_prices[i];         
            sell = stocks_prices[i];
        }

        profits = sell - buy;
        if (profits > max_profits)
            max_profits = profits;
    }

    return max_profits;
}

/* Self-Evaluation:
Correct answer, generally. Only real issue is that the function would return 0 profit if stock prices fall all day.
Function should either abort, or return negative profit if stocks always fall.
The solutions choose to to do the latter, as it allows for better data collection. 
*/



/* FULL SOLUTION */
/*
#define MAX(a, b) (((a) > (b)) ? (a) : (b))
#define MIN(a, b) (((a) < (b)) ? (a) : (b))

int getMaxProfit(const int *stockPrices, size_t length)
{
    int minPrice, maxProfit;
    size_t i;

    // make sure we have at least 2 prices
    assert(length >= 2);

    // we'll greedily update minPrice and maxProfit, so we initialize
    // them to the first price and the first possible profit
    minPrice = stockPrices[0];
    maxProfit = stockPrices[1] - stockPrices[0];

    // start at the second (index 1) time
    // we can't sell at the first time, since we must buy first,
    // and we can't buy and sell at the same time!
    // if we started at index 0, we'd try to buy *and* sell at time 0.
    // this would give a profit of 0, which is a problem if our
    // maxProfit is supposed to be *negative*--we'd return 0.
    for (i = 1; i < length; i++) {
        int currentPrice = stockPrices[i];

        // see what our profit would be if we bought at the
        // min price and sold at the current price
        int potentialProfit = currentPrice - minPrice;

        // update maxProfit if we can do better
        maxProfit = MAX(maxProfit, potentialProfit);

        // update minPrice so it's always
        // the lowest price we've seen so far
        minPrice = MIN(minPrice, currentPrice);
    }

    return maxProfit;
}
*/



int main(){
    int stock_prices[NUM_STOCK_PRICES] = {10, 11, 15, 13, 12, 9, 8, 10, 12, 14};
    size_t num_stock_prices = NUM_STOCK_PRICES;
    int returns;

    returns = getMaxProfit(stock_prices, num_stock_prices);
    printf("returns: $%d\n", returns);
    return 0;
}