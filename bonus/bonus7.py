filenames = ["1.doc", "1.report", "1.representation"]

# list comprehension
filenames = [filename.replace(".", "-") + ".txt" for filename in filenames]
print(filenames)

