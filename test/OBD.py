import obd

connection = obd.OBD() # auto connect

c = obd.commands.RPM

response = connection.query(c)

print(response.value)

connection.close()