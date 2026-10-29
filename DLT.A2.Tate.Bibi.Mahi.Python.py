import csv
import math
import statistics
from itertools import groupby

# Define variables for file path  
#Please change the path to your own path where the dataset is stored in your computer
filename = r"Cleaned dataset.csv"

# create dictionary list and associate numbers to the values for Social_Comparison_Frequency
comparison_codes = {
    "never": 1,
    "rarely": 2,
    "sometimes": 3,
    "frequently": 4,
    "always": 5,
}
# create dictionary list and associate numbers to the values for Late_Night_Usage attribute
late_night_codes = {
    "true": 1,
    "yes": 1,
    "1": 1,
    "false": 0,
    "no": 0,
    "0": 0,
}

	  
#The load_records function reads the CSV dataset, converts categorical values into numbers, and skips invalid records
def load_records(path):
    records = []
    with open(path, encoding="utf-8-sig", newline="") as file:
        for row in csv.DictReader(file):
            try:
                stress = float(row["Perceived_Stress_Score"])
                hours = float(row["Daily_Usage_Hours"])
                late = late_night_codes[row["Late_Night_Usage"].strip().lower()]
                comparison = comparison_codes[row["Social_Comparison_Frequency"].strip().lower()]
            except (ValueError, TypeError, KeyError, AttributeError):
                continue

            if all(map(math.isfinite, (stress, hours, late, comparison))):
                records.append((stress, hours, late, comparison))

    return records

#The average_ranks function assigns ranks to values and calculates average ranks for tied values. 
# It uses two times for two attributes Social_Comparison_Frequency and Late_Night_Usage from the dataset
def average_ranks(values):
    ranked = [0.0] * len(values)
    ordered = sorted(enumerate(values), key=lambda item: item[1])

    start = 0
    for _, tied_values in groupby(ordered, key=lambda item: item[1]):
        tied_values = list(tied_values)
        average_rank = (start + 1 + start + len(tied_values)) / 2
        for index, _ in tied_values:
            ranked[index] = average_rank
        start += len(tied_values)

    return ranked
#The correlation_or_none function calculates Pearson correlation. 
# It uses three times to Calcultae three correlations: 1) Daily_Usage_Hours and Perceived_Stress_Score
# 2)Late_Night_Usage and Perceived_Stress_Score,  3) Social_Comparison_Frequency and Perceived_Stress_Score
	  
def correlation_or_none(x, y):
    if len(x) < 2 or len(set(x)) < 2 or len(set(y)) < 2:
        return None
    return statistics.correlation(x, y)

	  
#the main program calculates the three correlations between social media habits and perceived stress,
#displays the results
#Main program			
records = load_records(filename)

if len(records) < 2:
    print("Not enough valid data.")
else:
	# Create a dictionary list and add three correlation coefficients to it.
    stress, daily_hours, late_night, comparison = map(list, zip(*records))
    correlations = [
        correlation_or_none(daily_hours, stress),
        correlation_or_none(average_ranks(late_night), stress),
        correlation_or_none(average_ranks(comparison), stress),
    ]
    names = [
        "Daily usage Hours",
        "Late-night usage",
        "Social comparison frequency",
    ]
	#Display the number of records(students)
    print("Valid students:", len(records))
    print()
    print("Below shows three correlation's coefficients")
    print()
	#Display all correlation values 
    for name, value in zip(
        ("Daily usage Hour", "Late-night usage", "Social comparison frequency"),
        correlations,
    ):
        print(f"{name}: {value}")

    available = [
        (index, value)
        for index, value in enumerate(correlations)
        if value is not None and math.isfinite(value)
    ]
	# If statement is to find the maximum Correlation's value between three correlation that find in the program
    if not available:
        print("Could not calculate the correlations.")
    else:
        best_index, best_value = max(available, key=lambda item: abs(item[1]))
        print()
        print("Strongest observed association:", names[best_index])
        print("Correlation coefficient:", round(best_value, 3))
