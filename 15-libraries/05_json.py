"""
===========================================
Materi : Library JSON
===========================================
"""

import json

data = {
    "nama" : "Naya", 
    "umur" : 19,
    "jurusan" : "IPA"
}

data_json = json.dumps(data)

print(data_json)

data_python = json.loads(data_json)

print(data_python)
print(data_python["nama"])