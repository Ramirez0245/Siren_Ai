import json
import pandas as pd
from src.pos import Order


class Customer_Data:
    data = {}
    data_frame = pd.DataFrame()

    def __init__(self, file_path):
        self.file_path = file_path
        self.read_data()

    def read_data(self):
        with open(self.file_path, "r") as file:
            data = file.read()
            self.data = json.loads(data)

    def get_data(self):
        return self.data

    def save_data(self):
        with open(self.file_path, "w") as file:
            file.write(json.dumps(self.data))

    def save_order(self, order: Order, used_app=False):
        drink = order.get_drinks()
        item_aray = []

        for d in drink:
            d_data = {
                "name": d.name,
                "size": d.size,
                "type": d.type,
                "add_ins": d.customizations,
                "category": d.category,
                "price": d.price,
            }
            item_aray.append(d_data)

        order_data = {
            "id": order.id,
            "total": order.total,
            "used_app": used_app,
            "customer_id": order.customer_id,
            "items": item_aray,
        }
        self.data["orders"].append(order_data)
        print("Order saved: ", order.id)
        self.save_data()

    def get_order(self, order_id):
        return self.data[order_id]

    def count(self) -> int:
        return len(self.data)

    def process_data(self):
        df = pd.DataFrame.from_dict(self.data["orders"])
        df["total_rounded"] = df["total"].round(2)

        order_ids = []
        used_apps = []
        order_totals = []
        customer_ids = []
        order_items = []

        for index, row in df.iterrows():
            order_id = row["id"]
            items = row["items"]

            app_used = row.get("used_app", False)
            total = row.get("total_rounded", 0)

            for item in items:
                item_info = {
                    "order_id": order_id,
                    "app_used": app_used,
                    "name": item["name"],
                    "size": item["size"],
                    "type": item["type"],
                    "add_ins": item["add_ins"],
                    "category": item["category"],
                }
                order_items.append(item_info)
                order_ids.append(order_id)
                used_apps.append(app_used)
                order_totals.append(total)

        self.df = pd.DataFrame(order_items)
        self.df.fillna(0, inplace=True)
        self.df.dropna(inplace=True)

        self.df = pd.get_dummies(self.df, columns=["category"])
        # self.df = pd.get_dummies(self.df, columns=["category"])

    def __str__(self):
        return str(self.data)
