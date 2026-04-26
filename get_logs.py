import urllib.request
import json
import zipfile
import io

url = "https://api.github.com/repos/nihalshx/prompt-playbook/actions/runs"
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode())
    
runs = data.get("workflow_runs", [])
for run in runs:
    if run.get("name") == "Deploy Jekyll site to Pages":
        jobs_url = run.get("jobs_url")
        print(f"Found run: {run['id']}, status: {run['conclusion']}")
        
        req_jobs = urllib.request.Request(jobs_url)
        with urllib.request.urlopen(req_jobs) as response_jobs:
            jobs_data = json.loads(response_jobs.read().decode())
            for job in jobs_data.get("jobs", []):
                print(f"Job: {job['name']}, status: {job['conclusion']}")
                for step in job.get("steps", []):
                    if step['conclusion'] == 'failure':
                        print(f"  Step failed: {step['name']}")
        
        # We can't get logs without auth if it's a ZIP, but we can see the steps!
        break
