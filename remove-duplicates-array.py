def remove_duplicates(input_list):
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


# Example usage:
input_list = [
    "freshapps_dp_router_ms",
    "freshapps_beworkers",
    "bifrost",
    "marketplace_gallery_frontend",
    "marketplace_gallery_frontend",
    "freshapps_api_test",
    "freshapps-toolkit",
    "freshapps_deployms",
    "freshapps-configurations",
    "freshapps_deployms",
    "freshapps-toolkit",
    "freshapps-configurations",
    "freshapps_e2etest",
    "freshapps_devportal",
    "freshapps_deployms",
    "freshapps_api",
    "freshapps_admin",
    "freshapps_ci_recipes",
    "freshapps_common",
    "freshapps-integration",
    "freshapps_deployms",
    "freshapps_e2etest",
    "freshapps_devportal",
    "freshapps_api",
    "freshapps_ci_recipes",
    "freshapps_admin",
    "freshapps_misc",
    "freshapps_common",
    "freshapps_ci_recipes",
    "freshapps_misc",
    "freshapps_ci_recipes",
    "freshapps_misc",
    "freshapps-toolkit",
    "freshapps_e2etest",
    "freshapps_api_test",
    "freshapps_deployms",
    "freshapps-configurations",
    "bifrost",
    "freshapps_deployms",
    "freshapps-toolkit",
    "freshapps_e2etest",
    "freshapps-configurations",
    "bifrost",
    "freshapps_misc",
    "marketplace_devportal_frontend",
    "freshapps_recipes",
    "marketplace_devportal_frontend",
    "freshapps_recipes",
    "marketplace_devportal_frontend",
    "freshapps_recipes",
    "marketplace_gallery_frontend",
    "freshapps_recipes",
    "marketplace_gallery_frontend",
    "frsh_parent",
    "mp-openai",
    "marketplace_viewer",
    "frsh_parent",
    "freshapps_sdk-test",
]
output_list = remove_duplicates(input_list)
print(output_list)
