# You are given an m x n integer grid accounts where accounts[i][j] is the amount
# of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the 
# richest customer has.

# A customer's wealth is the amount of money they have in all their bank 
# accounts. The richest customer is the customer that has the maximum wealth.


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        # variable for keeping track of highest wealth so far
        highest_wealth = 0
        
        # loop through each customer
        for cust_acc in accounts:
            
            # sum up bank balance
            wealth = sum(cust_acc)
            
            # update variable for highest wealth
            highest_wealth = max(wealth, highest_wealth)
            
        return highest_wealth