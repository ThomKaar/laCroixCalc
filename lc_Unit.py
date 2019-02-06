

class lc_Unit:
	def __init__(self, storeName, price, flavor, volume):
    self.storeName = storeName
    self.price = price
    self.flavor = flavor
    self.volume = volume
    self.date = date
    self.client = client

    def __repr__(self):
        return {'storeName ':self.storeName, 'price':self.price, 
        'flavor ': self.flavor, 'volume ': self.volume, 'date ': self.date}

   	def put_lc_Unit(self):
   		client.put_item(
   			Tablename='lc_Unit',
   			Item={
   				'storeName': {
   					'S': str(self.storeName)
   				},
   				'price': {
   					'N': self.price
   				},
   				'flavor': {
   					'S': str(self.storeName)
   				},
   				'volume': {
   					'N': self.volume
   				},
   				'client': {
   					'S': str(self.date)
   				}
   			})