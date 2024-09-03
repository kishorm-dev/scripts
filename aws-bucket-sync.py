from datetime import datetime
import subprocess

def sync_buckets(bucket_mapping):
    f = open("sync_logs.txt", "a")

    for source_bucket, dest_bucket in bucket_mapping.items():
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        command = f"aws s3 sync s3://{source_bucket} s3://{dest_bucket}"
        try:
            subprocess.run(command, shell=True, check=True)
            log_message = f"{timestamp} Synced {source_bucket} to {dest_bucket}\n"
            f.write(log_message)
            print(log_message)
        except subprocess.CalledProcessError as e:
            log_message = f"{timestamp} An error occurred while syncing {source_bucket} to {dest_bucket}:\n{e}\n"
            f.write(log_message)
            print(log_message)


bucket_mapping = {
    'app-log-archive':'app-log-archive-us-east-1',
    'apps-website-dev' : 'apps-website-dev-us-east-1',
    'apps-website-staging' : 'apps-website-staging-us-east-1',
    'fa-staging-pub' : 'fa-staging-pub-us-east-1',
    'fa-staging-pvt' : 'fa-staging-pvt-us-east-1',
    'freshapps-aws-accesslog-dev' : 'freshapps-aws-accesslog-dev-us-east-1',
    'freshapps-aws-accesslog-staging' : 'freshapps-aws-accesslog-staging-us-east-1',
    'freshapps-dev-pub' : 'freshapps-dev-pub-us-east-1',
    'freshapps-dev-pvt' : 'freshapps-dev-pvt-us-east-1',
    'freshapps-docker-dev' : 'freshapps-docker-dev-us-east-1',
    'freshapps-docker-staging' : 'freshapps-docker-staging-us-east-1',
    'freshapps-fa-dev-pub' : 'freshapps-fa-dev-pub-us-east-1',
    'freshapps-fa-dev-pvt' : 'freshapps-fa-dev-pvt-us-east-1',
    'freshworks-dev-portal-dev' : 'freshworks-dev-portal-dev-us-east-1',
    'freshworks-dev-portal-staging' : 'freshworks-dev-portal-staging-us-east-1',
    'freshworks-developer-cms' : 'freshworks-developer-cms-us-east-1',
    'gallery-client-dev' : 'gallery-client-dev-us-east-1',
    'gallery-client-staging' : 'gallery-client-staging-us-east-1',
    'redis-db-dump' : 'redis-db-dump-us-east-1',
    'staging-marketplace-observability-s3-backup-us-west-2' : 'staging-marketplace-observability-s3-backup-us-east-1',
    'static-dev.freshcloud.io' : 'static-dev-us-east-1.freshcloud.io',
    'ws.freshcloud.io' : 'ws-us-east-1.freshcloud.io'
}

sync_buckets(bucket_mapping)
