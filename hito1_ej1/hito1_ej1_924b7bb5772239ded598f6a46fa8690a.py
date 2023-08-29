# Ask the user for the four grades
PT = float(input("Enter the grade for Tareas (PT): "))
PI = float(input("Enter the grade for Interrogaciones (PI): "))
NE = float(input("Enter the grade for Examen (NE): "))
PP = float(input("Enter the grade for Presentacion (PP): "))

# Calculate the final average
final_average = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

# Round the final average to one decimal place
rounded_average = round(final_average, 1)

# Print the rounded average
print("The final average is:", rounded_average)