#f-strings (modern, preferred)
app="nginx"
version="1.18"
print(f"Running {app} version {version}")

#.format() method

print("Running {} version {}".format(app, version))

# %-formatting (old style, not recommended)
print("Running %s version %s" % (app, version))

# Padding and alignment with f-strings
number=7
print(f"Number padded with zeros: {number:05}")
print(f"Left aligned: {number:<5}")
print(f"Right aligned: {number:>5}")
print(f"Centered: {number:^5}")

# Formatting numbers with f-strings
pi=3.14159265359
print(f"Pi rounded to 2 decimal places: {pi:.2f}")
print(f"Pi in scientific notation: {pi:e}")
print(f"Pi in percentage: {pi:.2%}")

# multi line string
multi_line ="""This is a multi-line string.
It can span multiple lines. """
print(multi_line)