import numpy as np  # Importing numpy for numerical operations

# Function to simulate N coin flips and calculate the percentage of heads
def coinflip(N):
    # Generate N random numbers from a standard normal distribution
    # Treat numbers > 0 as "heads" and <= 0 as "tails"
    random_numbers = np.random.randn(N)
    
    # Calculate the proportion of heads (where random_numbers > 0)
    propCoinFlips = np.mean(random_numbers > 0)
    
    # Print the result: number of flips and the percentage of heads
    print(str(N) + ' coin flips had ' + str(100 * propCoinFlips) + '% heads.')

# Example usage
coinflip(1000)  # Simulate 1000 coin flips
