import json

from fastmcp import FastMCP

mcp = FastMCP("Kubernetes Tools")

try:
    # Use load_incluster_config() if running inside k8s
    print("K8s Config Loaded.")
except Exception as e:
    print(f"Error loading K8s config: {e}")
    v1_core = None
    v1_apps = None


@mcp.tool()
def list_pods(namespace: str = "default") -> str:
    """
    List all pods in the specified Kubernetes namespace.
    Returns a JSON string summary of pod names.
    """
    # print(f"--> [TOOL executing] Listing pods in namespace: {namespace}")
    pod_names = ['checkout-api-4a5b7c38', 'vmeconnector-e78c976a']
    # print(f"--> [TOOL response] {pod_names}")
    return json.dumps({"pods": pod_names})


@mcp.tool()
def delete_pod(pod_name: str, namespace: str = "default") -> str:
    """
    Delete a specific Kubernetes pod by name.
    """
    # print(f"--> [TOOL executing] Deleting pod: {pod_name} in namespace: {namespace}")
    # print(f"--> [TOOL executing] Pod: {pod_name} in namespace: {namespace}")
    return json.dumps({"status": "success", "message": f"Pod {pod_name} deleted."})


if __name__ == "__main__":
    # This runs the server over Stdio (Standard Input/Output) by default,
    # which is ideal for local integration with Claude Desktop or local scripts.
    mcp.run()
