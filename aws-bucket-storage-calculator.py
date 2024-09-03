
import subprocess
import os

buckets = ['app-log-archive',
'apps-website-dev',
'apps-website-staging',
'fa-staging-pub',
'fa-staging-pvt',
'freshapps-aws-accesslog-dev',
'freshapps-aws-accesslog-staging',
'freshapps-dev-pub',
'freshapps-dev-pvt',
'freshapps-docker-dev',
'freshapps-docker-staging',
'freshapps-fa-dev-pub',
'freshapps-fa-dev-pvt',
'freshworks-dev-portal-dev',
'freshworks-dev-portal-staging',
'freshworks-developer-cms',
'gallery-client-dev',
'gallery-client-staging',
'redis-db-dump',
'staging-marketplace-observability-s3-backup-us-west-2',
'static-dev.freshcloud.io',
'ws.freshcloud.io']

# Iterate through each bucket
for bucket in buckets:
    # Run the AWS CLI command for the bucket
    command = f"aws s3 ls --summarize --human-readable --recursive s3://{bucket}"
    try:
        # Execute the command and capture the output
        output = subprocess.check_output(command, shell=True, text=True)
        
        # Parse the output to find the total size
        total_size = None
        for line in output.split('\n'):
            if "Total Size:" in line:
                total_size = line.split()[2] + " " +line.split()[3]
                break

        # Parse the output to find the total objects
        total_objects = None
        for line in output.split('\n'):
            if "Total Objects:" in line:
                total_objects = line.split()[2]
                break
        
        # Print the total size of the bucket
        if total_size:
            print(f"Total Objects in {bucket} : {total_objects}")
            print(f"Total Size    of {bucket} : {total_size}")
        else:
            print(f"Unable to find total size for {bucket}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command for {bucket}: {e}")

