import json
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

with open("sample_data.json", "r") as file:
    data = json.load(file)
    for par in data['imdata']:
        print(f"{par['l1PhysIf']['attributes']['dn']}{' '*30}{par['l1PhysIf']['attributes']['fecMode']}{' '*3}{par['l1PhysIf']['attributes']['mtu']}")