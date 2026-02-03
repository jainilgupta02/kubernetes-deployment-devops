from kubernetes import client, config
import time

def watch_pods(namespace="default"):
    config.load_kube_config()
    v1 = client.CoreV1Api()

    print(f"📡 Watching pods in namespace: {namespace}\n")

    while True:
        pods = v1.list_namespaced_pod(namespace)

        print("Current Pods:")
        for pod in pods.items:
            print(f"- {pod.metadata.name}: {pod.status.phase}")

        print("\n---\n")
        time.sleep(5)

if __name__ == "__main__":
    watch_pods()
