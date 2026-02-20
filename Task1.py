print("="*50)
print(" AI TECH TROUBLESHOOTING EXPERT SYSTEM ")
print("="*50)

facts = set(input("Enter symptoms separated by comma: ").lower().replace(" ", "").split(","))

rules = [
    ({"slow", "overheating"}, "dust_issue"),
    ({"dust_issue"}, "clean_laptop"),
    
    ({"fannoise"}, "fan_problem"),
    ({"fan_problem"}, "clean_fan"),
    
    ({"slow", "lowstorage"}, "storage_issue"),
    ({"storage_issue"}, "delete_temp_files"),
    
    ({"notstarting"}, "power_issue"),
    ({"power_issue"}, "check_charger")
]

problems = {"dust_issue","fan_problem","storage_issue","power_issue"}
solutions = {"clean_laptop","clean_fan","delete_temp_files","check_charger"}

derived = set()
logs = []

changed = True
while changed:
    changed = False
    for condition, result in rules:
        if condition.issubset(facts) and result not in facts:
            facts.add(result)
            derived.add(result)
            logs.append(f"Rule applied: {condition} → {result}")
            changed = True


print("\nDetected Problems:")
for f in derived:
    if f in problems:
        print("-", f.replace("_"," "))

print("\nSuggested Solutions:")
for f in derived:
    if f in solutions:
        print("-", f.replace("_"," "))


print("\nReasoning Steps:")
for log in logs:
    print(log)