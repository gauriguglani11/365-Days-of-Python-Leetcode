Q. There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i]. You have a car with an unlimited gas tank and it costs cost[i] of gas 
to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.Given two integer arrays gas and cost, return the 
starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

Logic-
a. Initialize total_gas to be the sum of all elements in the gas array, and deficit to be the sum of the difference between corresponding elements of gas and cost arrays.
b. If total_gas is less than deficit, then return -1, because it is not possible to complete the circuit.
c. Otherwise, try starting at each gas station in turn and check if it is possible to complete the circuit. To do this, initialize current_gas to be the amount of gas at that station, 
and iterate through the stations in the circuit. At each station, do the following:
d. Subtract the cost of going from that station to the next station from current_gas.
e. If current_gas is less than 0, then start over at the next station with an empty tank.
f. If you make it all the way around the circuit and current_gas is greater than or equal to 0 at the starting station, then return the index of the starting station.

code:

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if (sum(gas) - sum(cost) < 0):
            return -1
        
        gas_tank, start_index = 0, 0
        
        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]
            
            if gas_tank < 0:
                start_index = i+1
                gas_tank = 0
            
        return start_index