from prettytable import PrettyTable
#http://blog.csdn.net/codeway3d/article/details/52798804
#PrettyTable,from_csv,from_html,from_db_cursor
table = PrettyTable(["animal", "ferocity"])
table.add_row(["wolverine", 100])
table.add_row(["grizzly", 87])
table.add_row(["Rabbit of Caerbannog", 110])
table.add_row(["cat", -1])
table.add_row(["platypus", 23])
table.add_row(["dolphin", 63])
table.add_row(["albatross", 44])
#table.add_column(["one","two","three","four","five","six","seven"])
table.sort_key("ferocity")
table.reversesort = True

print(table)
