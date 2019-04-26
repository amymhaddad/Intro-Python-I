nums = 5

#check first function to make sure it's working
#update second function to check if len of factors is LESS than 2

def get_factors(nums):
    factors = []
    for num in range(1, nums + 1):
        for factor in range(1, num + 1):
            if num * factor == nums:
                factors.append(num)
    return factors

def is_prime(number): 
    return len(get_factors(number)) 

print(is_prime(5))