from requests import post, get

base_url = "https://adb-469900930702604.4.azuredatabricks.net"

params = {
          "statement":"select * from students",
          "warehouse_id":"29904bc1f8b09eb4",
          "catalog":"hive_metastore",
          "schema":"default",
          "wait_timeout": "50s"}

headers = {"Authorization": "Bearer dapic06d12e62597bcd0a3834f7298561e2d"}

req = post(f"{base_url}/api/2.0/sql/statements",headers=headers,json=params)

req.json()
