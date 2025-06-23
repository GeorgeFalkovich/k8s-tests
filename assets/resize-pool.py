from googleapiclient.discovery import build
from google.oauth2 import service_account

# Replace these variables with your GCP details
PROJECT_ID = "georgef-sandbox"
ZONE = "us-central1-a"  # e.g., "us-central1-a"
CLUSTER_ID = "my-gke-cluster"
NODE_POOL_ID = "alpha-pool"

# Path to your service account key file
SERVICE_ACCOUNT_FILE = "key.json"


def resize_node_pool(project_id, zone, cluster_id, node_pool_id, size):
    """
    Resizes a GKE node pool to the specified size.
    """
    # Authenticate using the service account
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE)
    service = build('container', 'v1', credentials=credentials)

    # Build the request to resize the node pool
    request = service.projects().zones().clusters().nodePools().setSize(
        projectId=project_id,
        zone=zone,
        clusterId=cluster_id,
        nodePoolId=node_pool_id,
        body={"nodeCount": size}
    )

    # Execute the API call
    try:
        response = request.execute()
        print(f"Node pool '{node_pool_id}' resized to {size} nodes.")
        return response
    except Exception as e:
        print(f"Error resizing node pool: {e}")
        return None


# Main function
if __name__ == "__main__":
    # Resize the node pool to 0 nodes
    desired_size = 3
    response = resize_node_pool(
        PROJECT_ID, ZONE, CLUSTER_ID, NODE_POOL_ID, desired_size)

    if response:
        print("Operation completed successfully.")
    else:
        print("Failed to resize the node pool.")
