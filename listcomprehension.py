filenames = ["1.doc", "1.report", "1.presentation"]

[filename.replace('.', '-') + '.txt' for filename in filenames]

print(filenames)