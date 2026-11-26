import os
import shutil

SRC = os.path.join(os.path.dirname(__file__), "entry.png")
MAX_BYTES = 1048576

if not os.path.isfile(SRC):
    raise FileNotFoundError("entry.png is missing from the repository")
if os.path.getsize(SRC) > MAX_BYTES:
    raise ValueError("entry.png must be at most 1 MiB")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
dest = os.path.join(out_dir, "entry.png")
shutil.copyfile(SRC, dest)
if os.path.getsize(dest) != os.path.getsize(SRC):
    raise ValueError("copied entry.png does not match the source")
