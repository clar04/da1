import mean_var_std
from unittest import main

# Test the function with the example
print("Testing calculate([0,1,2,3,4,5,6,7,8]):")
result = mean_var_std.calculate([0,1,2,3,4,5,6,7,8])
print(result)

print("\n" + "="*50 + "\n")

# Test with different input
print("Testing calculate([1,2,3,4,5,6,7,8,9]):")
result2 = mean_var_std.calculate([1,2,3,4,5,6,7,8,9])
print(result2)

print("\n" + "="*50 + "\n")

# Test the problematic case
print("Testing calculate([9,1,5,3,3,3,2,9,0]):")
result3 = mean_var_std.calculate([9,1,5,3,3,3,2,9,0])
print(result3)

print("\n" + "="*50 + "\n")

# Test error case
print("Testing error case with less than 9 elements:")
try:
    mean_var_std.calculate([1,2,3,4,5])
    print("No error raised - this shouldn't happen!")
except ValueError as e:
    print(f"Correctly raised ValueError: {e}")

# This will run any unit tests when available
if __name__ == "__main__":
    main()