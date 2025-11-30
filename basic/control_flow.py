status = "running"

if status == "running":
    print("The process is currently running.")
elif status == "stopped":
    print("The process is not currently running.")
else:
    print("Unknown process status.")


count = 0
match count:
    case 0:
        print("Count is zero.")
    case 1:
        print("Count is one.")
    case 2:
        print("Count is two.")
    case _:  #default case or wildcard
        print("Count is something else.")