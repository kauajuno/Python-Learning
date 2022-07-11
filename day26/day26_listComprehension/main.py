first_list = [line.rstrip() for line in open("one.txt")]
second_list = [line.rstrip() for line in open("two.txt")]
overlap = [item for item in first_list if item in second_list]
print(overlap)
