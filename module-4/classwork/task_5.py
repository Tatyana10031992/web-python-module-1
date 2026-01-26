def func(filename):
    return filename.rsplit(".", 1)[-1] if "." in filename else ""

print(func("filename.pdf")) 
