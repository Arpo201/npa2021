from ncclient import manager

m = manager.connect(
    host="10.0.15.22",
    port=830,
    username="admin",
    password="cisco",
    hostkey_verify=False
)

print("#Supported Capabilities (YANG models):")
for capability in m.server_capabilities:
    print(capability)
