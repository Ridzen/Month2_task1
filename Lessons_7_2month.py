text = [1, 1, 3, 2, 1, 3, 4]

summary = {}
for all in set(text):
    summary[all] = text.count(all)
print(summary)
