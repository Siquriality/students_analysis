INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"
subjects = ["math", "python", "english"]
sums = [0, 0, 0]
count = 0
best_name = None
best_avg = -1
with open(INPUT_FILE, encoding="utf-8") as f:
    next(f)
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        name = parts[0]
        grades = [int(x) for x in parts[1:4]]
        for i in range(3):
            sums[i] += grades[i]
        count += 1
        student_avg = sum(grades) / 3
        if student_avg > best_avg:
            best_avg = student_avg
            best_name = name
averages = [s / count for s in sums]
result = "Середній бал по класу:\n"
for i in range(3):
    result += f"{subjects[i]}: {averages[i]:.1f}\n"
result += "\n"
result += f"Найкращий студент: {best_name} ({best_avg:.1f})\n"
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(result)
print(result)
