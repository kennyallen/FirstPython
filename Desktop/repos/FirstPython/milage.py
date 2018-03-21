print("How many kilometers did you walk today?")
kms = input()
miles = float(kms)/1.60934
miles = round(miles, 2)
print(f"Ok, your {kms}km ride is {miles} miles. Great job!")

