import subprocess


def migrate_lambda(source_region, destination_region, function_names):
    for function_name in function_names:
        print(
            f"Migrating function '{function_name}' from {source_region} to {destination_region}..."
        )
    # Get function configuration from the source region
    get_function_cmd = f"aws lambda get-function --function-name {function_name} --region {source_region}"
    function_config = subprocess.run(
        get_function_cmd, capture_output=True, text=True, shell=True
    )

    if function_config.returncode == 0:
        # Save function configuration to a temporary file
        with open("function-config.json", "w") as temp_file:
            temp_file.write(function_config.stdout)

        # Create function in the destination region using the configuration from the temporary file
        create_function_cmd = f"aws lambda create-function --function-name {function_name} --region {destination_region} --cli-input-json file://function-config.json"
        create_function_result = subprocess.run(
            create_function_cmd, capture_output=True, text=True, shell=True
        )

        if create_function_result.returncode == 0:
            print(f"Function '{function_name}' migrated successfully.")
        else:
            print(
                f"Error migrating function '{function_name}': {create_function_result.stderr}"
            )

        # Remove temporary file
        # subprocess.run("rm function-config.json", shell=True)
    else:
        print(
            f"Error retrieving function '{function_name}' configuration: {function_config.stderr}"
        )


if __name__ == "__main__":
    # Set your source and destination regions
    source_region = "us-west-2"
    destination_region = "us-east-1"

    # List of Lambda function names to migrate
    function_names = ["digital-turk-staging"]

    # Migrate Lambda functions
    migrate_lambda(source_region, destination_region, function_names)
