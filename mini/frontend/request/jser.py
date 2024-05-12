
import json

def mkj(name, request, data):
    lst = {}
    lst['name'] = name
    lst['request'] = request
    if isinstance(data, bytes):
            data = data.decode('utf-8', 'ignore')
    lst['data'] = data
    return json.dumps(lst).encode('utf-8')
    
def rj(jsn):
    return json.loads(jsn)['data']

'''formate
json=>{clientname :<>, request :<>, data :<>}'''
