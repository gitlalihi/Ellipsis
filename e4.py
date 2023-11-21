#Python program that creates a list containing numbers from 1 to 10, but leaves a gap at even positions using ellipsis.
print("Containing numbers from 1 to 10, but leaves a gap at even positions:")
nums = [i if i % 2 != 0 else ... for i in range(1, 11)]
print(nums)
print("\nContaining numbers from 10 to 20, but leaves a gap at odd positions:")
nums = [i if i % 2 == 0 else ... for i in range(10, 21)]
print(nums)