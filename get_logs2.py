import urllib.request
import json
import zipfile
import io
import sys

url = "https://api.github.com/repos/nihalshx/prompt-playbook/actions/runs"
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode())
    
runs = data.get("workflow_runs", [])
run_id = None
for run in runs:
    if run.get("name") == "Deploy Jekyll site to Pages" and run.get("conclusion") == "failure":
        run_id = run['id']
        break

if not run_id:
    print("No failed run found")
    sys.exit(0)

logs_url = f"https://api.github.com/repos/nihalshx/prompt-playbook/actions/runs/{run_id}/logs"
req = urllib.request.Request(logs_url)
# No auth needed for public repos usually, but let's see. If it fails with 401, we know.
try:
    with urllib.request.urlopen(req) as response:
        zip_data = response.read()
        with zipfile.ZipFile(io.BytesIO(zip_data)) as z:
            for filename in z.namelist():
                if "Build with Jekyll" in filename or "build" in filename.lower():
                    print(f"--- {filename} ---")
                    lines = z.read(filename).decode('utf-8').split('\n')
                    for line in lines[-50:]:  # last 50 lines
                        print(line)
except Exception as e:
    print(f"Error fetching logs: {e}")
