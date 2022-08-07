from flask_application import app, CATALOG_SERVER_IP, ORDER_SERVER_IP, CATALOG_PORT, ORDER_PORT

# Class Replication
class Replication:
    def __init__(self, catalog_ips, order_ips, catalog_ports, order_ports):
        self.catalog_ips = catalog_ips
        self.order_ips = order_ips
        self.catalog_ports = catalog_ports
        self.order_ports = order_ports
        self.catalog_turn = 0
        self.order_turn = 0

    def get_catalog_info(self):
        # Get ip address of the current catalog server
        catalog_ip = self.catalog_ips[self.catalog_turn]
        catalog_port = self.catalog_ports[self.catalog_turn]
        
        print("\n###########################################################")
        print(f"Request from catalog server with index={self.catalog_turn}, ip={self.catalog_ips[self.catalog_turn]}")
        print("###########################################################")

        # Round Robin algorithm
        self.catalog_turn += 1
        if self.catalog_turn >= len(self.catalog_ips):
            self.catalog_turn = 0

        return catalog_ip, catalog_port

    def get_order_info(self):
        # Get ip address of the current order server
        order_ip = self.order_ips[self.order_turn]
        order_port = self.order_ports[self.order_turn]
        
        print("\n###########################################################")
        print(f"Request from order server with index={self.order_turn}, ip={self.order_ips[self.order_turn]}")
        print("###########################################################")

        # Round Robin algorithm
        self.order_turn += 1
        if self.order_turn >= len(self.order_ips):
            self.order_turn = 0

        return order_ip, order_port


replication = Replication(CATALOG_SERVER_IP, ORDER_SERVER_IP, CATALOG_PORT, ORDER_PORT)
