def average(class_scores):
    if not class_scores:
        return 0.0
    total_score = sum(class_scores.values())
    num_students = len(class_scores)
    return total_score / num_students

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")