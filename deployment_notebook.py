import requests
import json

# Model variables from the model registry
endpoint_name = "churn-model-endpoint"
model_name = "churn-model"
model_version = "1"

# Get API token info from notebook context
ctx = dbutils.notebook.entry_point.getDbutils().notebook().getContext()
token = ctx.apiToken().getOrElse(None)
url = ctx.apiUrl().getOrElse(None)

# Define the API endpoint URL
endpoint_url = f"{url}/api/2.0/serving-endpoints"

# Define the request payload
payload = {
    "name": endpoint_name,
    "config": {
        "served_models": [{
            "model_name": model_name,
            "model_version": model_version,
            "workload_size": "Small",
            "scale_to_zero_enabled": True
        }]
    }
}

# Set the headers and authentication token
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Make the API request
response = requests.post(endpoint_url, headers=headers, data=json.dumps(payload))

# Check the status code of the response
if response.status_code == 200:
    print("Endpoint created successfully")
else:
    print("Error creating endpoint:", response.content)
