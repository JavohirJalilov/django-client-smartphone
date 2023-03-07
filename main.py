import requests
from db import SmartPhoneDB

url = "http://127.0.0.1:8000/add_product/"
db = SmartPhoneDB()
tables = list(db.get_tables())
# i = 0
for i in tables:
    for product in db.get_all(i):
        name = product['brend']
        brend = product['model']
        price = round(float(''.join(product['price'].split()[:-1]))/11350, 2)
        color = product['color']
        ram = product['ram']
        memory = product['memory']
        img = product['img_url']
        if len(name) < 7:
            name = f"{brend} {name}"
        
        data = {
            "name":name,
            "color":color,
            "brend":brend,
            "price": price,
            "ram": int(ram),
            "memory": int(memory),
            "img": img
        }

        response = requests.post(url, json=data)
        print(response.json())
        # break