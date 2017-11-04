from collections import namedtuple

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
#列表推导式
tshirts = [(color, size) for color in colors for size in sizes]
for t in tshirts:
	print(t)
#print(tshirts)
#迭代式，理论上把列表推导式的方括号换成圆括号就是了
tshirts2 = ((color, size) for color in colors for size in sizes)
for t in tshirts2:
	print(t)

#元组
metro_areas = [
('Tokyo','JP',36.933,(35.689722,139.691667)),
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
	if longitude <= 0:
		print(fmt.format(name, latitude, longitude))

#具名元组
#_fields，_make，_asdict
City = namedtuple('City', 'name country population coordinates')
City._fields
LatLong = namedtuple('LatLong', 'lat long')
#创建元组
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
#把元组作为参数创建City实例
delhi = City._make(delhi_data)
print(delhi._asdict())
print("~~~~~~~~~~~~~~")
for key, value in delhi._asdict().items():
	print(key + ':', value)

print("~~~~~~~~~~~~~~~~")
#切片
invoice = """
0.....6................................40........52...55........
1909	Pimoroni PiBrella				$17.50		3	 $52.50
1489	6mm Tactile Switch x20			$4.95		2	$9.90
1510	Panavise Jr. - PV-201			$28.00		1	$28.00
1601	PiTFT Mini Kit 320x240			$34.95		1	$34.95
"""
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
	print(item[UNIT_PRICE], item[DESCRIPTION])