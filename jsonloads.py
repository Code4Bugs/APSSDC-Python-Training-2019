import json
data='''[{"name":"srinivas","mobile":"8756897567","gmail":"bharath@gmail.com"},
{"name":"sdsameer","mobile":"7657686576","gmail":"sameer@gmail.com"}]'''
jsonobj = json.loads(data)
print(jsonobj)
type(jsonobj)