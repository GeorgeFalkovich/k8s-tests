import googleapiclient.discovery
import google.auth


def resize_node_pool(request):
    """
    Cloud Function to resize a GKE node pool to zero.
    Triggered by an HTTP request.
    """
    # Replace these variables with your GCP details
    PROJECT_ID = "georgef-sandbox"
    ZONE = "us-central1-a"  # e.g., "us-central1-a"
    CLUSTER_ID = "my-gke-cluster"
    NODE_POOL_ID = "alpha-pool"

    # Parse JSON input from the HTTP request
    request_json = request.get_json()
    # Default to zero if no size is provided
    size = request_json.get('size', 0)

    try:
        # Authenticate using the default service account of the Cloud Function
        credentials, _ = google.auth.default()
        service = googleapiclient.discovery.build(
            'container', 'v1', credentials=credentials)

        # Build the request to resize the node pool
        request = service.projects().zones().clusters().nodePools().setSize(
            projectId=PROJECT_ID,
            zone=ZONE,
            clusterId=CLUSTER_ID,
            nodePoolId=NODE_POOL_ID,
            body={"nodeCount": size}
        )

        # Execute the API call
        response = request.execute()
        return f"Node pool '{NODE_POOL_ID}' resized to {size} nodes. Response: {response}", 200

    except Exception as e:
        return f"Error resizing node pool: {str(e)}", 500
