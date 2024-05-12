import json

def unpack(jsr):
    return json.loads(jsr)

def pack(request, data):
    dict = {}
    dict['response'] = request
    if isinstance(data, bytes):
            data = data.decode('utf-8', 'ignore')
    dict['data'] = data
    
    return json.dumps(dict).encode("utf-8")

