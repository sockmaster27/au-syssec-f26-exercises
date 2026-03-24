from contextlib import redirect_stdout
import io
from subprocess import call, run, PIPE

while True:
    x = run(["toctou", "t.txt"], stdout=PIPE, stderr=PIPE)
    out = x.stdout.decode() + x.stderr.decode()
    print(out)
    if "=" in out:
        break
