import os
import sys
from frictionless import Package

def compare_data_resource_paths():
  data_resources_names = os.listdir('data')
  data_resources_paths = [os.path.join('data', i) for i in data_resources_names]
  data_resources_paths.sort()
  print(data_resources_paths)
  local_package = Package('datapackage.json')
  datapackage_resources_paths = [i["path"] for i in local_package.resources]
  datapackage_resources_paths.sort()
  print(datapackage_resources_paths)
  if data_resources_paths != datapackage_resources_paths:
    print("Resources presentes no arquivo datapackage.json diferente dos listados da pasta data.")
    sys.exit(1)
  print("Resources presentes no arquivo datapackage.json iguais aos listados da pasta data.")

if __name__ == '__main__':
  compare_data_resource_paths()
