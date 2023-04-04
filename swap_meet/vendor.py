class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
    
    def add_item(self, item):
        self.inventory.append(item)
        return item
    
    def remove_item(self, item):
        if not item in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
