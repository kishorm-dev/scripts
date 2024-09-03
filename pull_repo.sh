
#!/bin/bash

# Path to the folder containing all your repositories
parent_dir="/Users/kmuruganandham/Codebase/freshdesk"

# Navigate to the parent directory
cd $parent_dir

# Loop through each subdirectory
for repo in */ ; do
    echo "Processing $repo"
    cd "$repo"
    
    # Fetch the default branch name (assuming the repository has a remote named 'origin')
    default_branch=$(git remote show origin | grep 'HEAD branch' | awk '{print $NF}')
    
    # Checkout to the default branch
    git checkout $default_branch
    
    # Pull the latest changes
    git pull
    
    # Return to the parent directory
    cd ..
done

