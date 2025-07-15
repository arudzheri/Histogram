import tkinter as tk

# Initialize outcome counters
outcomes = {
    "Progress": 0,
    "Trailer": 0,
    "Retriever": 0,
    "Excluded": 0
}

# Classification logic
def classify(pass_credits, defer_credits, fail_credits):
    total = pass_credits + defer_credits + fail_credits
    if total != 120:
        return "Invalid"

    if pass_credits == 120:
        return "Progress"
    elif pass_credits == 100:
        return "Trailer"
    elif fail_credits >= 80:
        return "Excluded"
    else:
        return "Retriever"

# Input loop
while True:
    try:
        pass_credits = int(input("Enter your total PASS credits: "))
        defer_credits = int(input("Enter your total DEFER credits: "))
        fail_credits = int(input("Enter your total FAIL credits: "))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        continue

    result = classify(pass_credits, defer_credits, fail_credits)
    if result == "Invalid":
        print("Total incorrect. The sum must be 120.")
        continue
    else:
        print(result if result != "Trailer" else "Progress (module trailer)")
        outcomes[result] += 1

    cont = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ").lower()
    if cont == 'q':
        break

# Show histogram using Tkinter
categories = ["Progress", "Trailer", "Retriever", "Excluded"]
values = [outcomes["Progress"], outcomes["Trailer"], outcomes["Retriever"], outcomes["Excluded"]]
colors = ['lightgreen', 'yellow', 'orange', 'red']
total_outcomes = sum(values)

# Create window
root = tk.Tk()
root.title("Histogram w1990315")

# Create canvas
canvas = tk.Canvas(root, width=500, height=400, bg='skyblue')
canvas.pack()

# Draw bars
bar_width = 80
spacing = 20
x_start = 50
y_base = 300
scale = 40

for i, (category, value, color) in enumerate(zip(categories, values, colors)):
    x1 = x_start + i * (bar_width + spacing)
    y1 = y_base - (value * scale)
    x2 = x1 + bar_width
    y2 = y_base

    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
    canvas.create_text((x1 + x2) / 2, y1 - 10, text=str(value), font=("Arial", 12))
    canvas.create_text((x1 + x2) / 2, y_base + 15, text=category, font=("Arial", 12))

canvas.create_text(250, 30, text="Histogram Results:", font=("Arial", 14, "bold"))
canvas.create_text(250, 350, text=f"Outcomes: {total_outcomes}", font=("Arial", 12))

# Run
root.mainloop()

