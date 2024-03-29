from ncclient import manager
import xml.dom.minidom

m = manager.connect(
    host="10.0.15.22",
    port=830,
    username="admin",
    password="cisco",
    hostkey_verify=False
)

netconf_filter = """
<filter>
 <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
 <interface><name>GigabitEthernet1</name></interface>
 </interfaces-state>
</filter>
"""

netconf_reply = m.get(filter=netconf_filter)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
