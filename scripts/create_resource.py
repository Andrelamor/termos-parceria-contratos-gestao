import os
import sys
import requests
from frictionless import Package
import ipdb

def create_resource(ckan_host):
  local_package = Package('datapackage.json')
  local_package_resouces_names = [i["name"] for i in local_package.resources]
  url = f'{ckan_host}/api/3/action/package_show?id={local_package.name}'
  ckan_package_resources = requests.get(url=url).json()["result"]["resources"]
  ckan_package_resources_urls = [i["url"] for i in ckan_package_resources]
  ckan_package_resources_names = [i.split('/')[-1].split('.')[0] for i in ckan_package_resources_urls]
  for name in local_package_resouces_names:
    if name not in ckan_package_resources_names:
      print(f'Criando recurso {name} com DPCKAN.')
      os.system(f'dpckan resource {name} create')
    else:
      print(f'Recurso {name} já existe no conjunto {ckan_host}/dataset/{local_package.name}.')

if __name__ == '__main__':  
  create_resource(sys.argv[1])