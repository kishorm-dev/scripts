#!/bin/bash

GITHUB_USER="freshdesk"

# Define the repositories you want to clone
REPOSITORIES=(
    "bifrost"
    "developer-platform-commons"
    "developer-platform-lambdas"
    "freshapps-configurations"
    "freshapps-toolkit"
    "freshapps_accapi"
    "freshapps_admin"
    "freshapps_api"
    "freshapps_apiwrapper_node"
    "freshapps_api_node"
    "freshapps_api_test"
    "freshapps_beworkers"
    "freshapps_central_consumer"
    "freshapps_ci_recipes"
    "freshapps_common"
    "freshapps_deployms"
    "freshapps_developer_website"
    "freshapps_devportal"
    "freshapps_devportal_backend"
    "freshapps_dp_router_ms"
    "freshapps_e2etest"
    "freshapps_gallery"
    "freshapps_misc"
    "freshapps_oauth_ms"
    "freshapps_persistence_ms"
    "freshapps_recipes"
    "freshapps_sdk"
    "freshapps_sdk_choco"
    "freshapps_sdk-test"
    "freshapps_third_party_events"
    "Frsh_client"
    "frsh_parent"
    "lemans"
    "marketplace_devportal_frontend"
    "marketplace_gallery_frontend"
    "marketplace_viewer"
    "mp-apps"
    "mp-commons"
    "mp-gateway"
    "mp-installation"
    "mp-openai"
    "mp-recommendation"
    "mp-reviews"
    "freshapps-k8s"
)

# Directory to clone the repositories into
CLONE_DIR="$HOME/Codebase/freshdesk"

# Check if the directory exists, if not create it
if [ ! -d "$CLONE_DIR" ]; then
    mkdir -p "$CLONE_DIR"
fi

# Navigate to the clone directory
cd "$CLONE_DIR"

# Clone each repository
for REPO in "${REPOSITORIES[@]}"; do
    git clone git@github.com:$GITHUB_USER/$REPO.git
done

echo "Cloning completed."

