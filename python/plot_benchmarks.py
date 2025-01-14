from prettytable import PrettyTable

table = PrettyTable()

table.title = "Benchmarks - dt = 1/60, t_end = 1"
table.field_names = ["Nr of processes", "10 bodies", "100 bodies", "1000 bodies"]
table.add_row(["1", "17.03", "8.59", "0.18"])
table.add_row(["2", "16.74", "10.94", "0.34"])
table.add_row(["4", "15.47", "11.89", "0.45"])
table.add_row(["8", "15.34", "12.59", "0.74"])

print(table)
