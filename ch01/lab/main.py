import random
weeks = 16
print("Weeks: ", weeks, type(weeks))
classes = 5
print("Classes: ", classes, type(classes))
tuition = 6000
print("Tuition: ", tuition, type(tuition))
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 7
print("Classes per week: ", classes_per_week, type(classes_per_week))
cost_per_class = (cost_per_week / classes_per_week)
print("Cost per class: ", cost_per_class, type(cost_per_class))
apples = [
    "Canada",
    "orange juice",
    78,
    "Tinker Bell",
    3.14159265358979323
]
print("List: ", apples, type(apples))
print(random.choice(apples))