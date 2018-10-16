from keystoneauth1 import session, loading
from swiftclient import Connection
import os

env = os.environ




loader = loading.get_plugin_loader('password')
auth = loader.load_from_options(
                           auth_url=env['OS_AUTH_URL'],
                           username=env['OS_USERNAME'],
                           password=env['OS_PASSWORD'],
                           project_name=env['OS_PROJECT_NAME'],
                           project_domain_name=env['OS_USER_DOMAIN_NAME'],
                           project_id=env['OS_PROJECT_ID'],
                           user_domain_name=env['OS_USER_DOMAIN_NAME'])

sess = session.Session(auth=auth)

swift = Connection(session=sess)


resp_headers, containers = swift.get_account()

container_name = 'fabian_data'
container = swift.get_container(container_name)

files = os.listdir('data')
for filename in files:
    file_obj = os.path.join('data/', filename)
    with open(file_obj, 'r') as local:
        #print(local)
        swift.put_object(container_name, file_obj, contents=local, content_type="plain/text")

#print(swift.get_container(container_name))
