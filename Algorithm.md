The impact of Social media usage 
Plain text  
1.	Import the tools needed to read a CSV file and calculate correlation coefficients.
2.	Open the cleaned CSV dataset.
3.	Create the lists needed to store attributes Perceived_Stress_Score, Daily_Usage_Hours, Late_Night_Usage, Social_Comparison_Frequency.
4.	Read the dataset one row at a time.
5.	Convert Social_Comparison_Frequency to a number such as Never = 1, Rarely = 2, Sometimes = 3, Frequently = 4, and Always = 5.
6.	Convert Late_Night_Usage from True or False into 1 or 0 (True = 1, False = 0).
7.	Convert two additional fields Perceived_Stress_Score and Daily_Usage_Hours to number by cast.
8.	Skip rows containing missing, invalid, or unrecognized values.
9.	Call the function for calculating the correlation between Daily_Usage_Hours  and Perceived_Stress_Score.
10.	Call the function for calculating the correlation between Late_Night_Usage  and Perceived_Stress_Score.
11.	Call the function for calculating the correlation between Social_Comparison_Frequency and Perceived_Stress_Score
12.	Compare the absolute values of the three correlation coefficients.
13.	Display the habit factor with the largest absolute correlation. Display the three correlation coefficients and the habit with the largest absolute correlation
14.	Display the statement” The result shows an association, not that the habit causes stress.”
