import os
folders = ["healthcare_project/app","healthcare_project/db","healthcare_project/data","healthcare_project/utils"]
for f in folders:
  os.makedirs(f, exist_ok=True)
print("project structure created")

