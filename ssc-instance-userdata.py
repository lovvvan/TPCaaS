# http://docs.openstack.org/developer/python-novaclient/ref/v2/servers.html
import time, os, sys
import inspect
from os import environ as env

from  novaclient import client
import keystoneclient.v3.client as ksclient
from keystoneauth1 import loading
from keystoneauth1 import session

flavor = "ssc.xsmall"
private_net = "UPPMAX 2021/1-5 Internal IPv4 Network"
floating_ip_pool_name = "Public External IPv4 Network"
# The floating_ip is not set dynamically, need to set after this code is run.
# First find an available floating ip by:
# 1. list floating_ips by "openstack floating ip list"
# 2. Choose a floating_ip that has Fixed IP Address = None
# 3. Run this code
# 4. Connect the floating ip to the created instance by: openstack server add floating ip <instance-name> <floating ip>
#floating_ip = "130.238.28.178"
image_name = "Ubuntu 20.04 - 2021.03.23"

loader = loading.get_plugin_loader('password')

auth = loader.load_from_options(auth_url=env['OS_AUTH_URL'],
                                username=env['OS_USERNAME'],
                                password=env['OS_PASSWORD'],
                                project_name=env['OS_PROJECT_NAME'],
                                project_domain_name=env['OS_USER_DOMAIN_NAME'],
                                project_id=env['OS_PROJECT_ID'],
                                user_domain_name=env['OS_USER_DOMAIN_NAME'])

sess = session.Session(auth=auth)
nova = client.Client('2.1', session=sess)
print ("user authorization completed.")

image = nova.glance.find_image(image_name)

flavor = nova.flavors.find(name=flavor)

if private_net != None:
    net = nova.neutron.find_network(private_net)
    nics = [{'net-id': net.id}]
else:
    sys.exit("private-net not defined.")


#print("Path at terminal when executing this file")
#print(os.getcwd() + "\n")
cfg_file_path =  os.getcwd()+'/cloud-cfg.txt'
if os.path.isfile(cfg_file_path):
    userdata = open(cfg_file_path)
else:
    sys.exit("cloud-cfg.txt is not in current working directory")

secgroups = ['default']

print ("Creating instance ... ")
instance = nova.servers.create(name="Lovisa-lab3", key_name="beancloud", image=image, flavor=flavor, userdata=userdata, nics=nics,security_groups=secgroups)
inst_status = instance.status
print ("waiting for 10 seconds.. ")
time.sleep(10)

while inst_status == 'BUILD':
    print ("Instance: "+instance.name+" is in "+inst_status+" state, sleeping for 5 seconds more...")
    time.sleep(5)
    instance = nova.servers.get(instance.id)
    inst_status = instance.status

print ("Instance: "+ instance.name +" is in " + inst_status + "state")

#floatingIPThing = FloatingIPCloudMixin()
#floating_ip = available_floating_ip(self, private_net, instance)
#print("floting ip", floating_ip)
