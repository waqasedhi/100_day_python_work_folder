# from turtle import Turtle, Screen
#
# timmy=Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red","green")
# timmy.fd(100)
#
# screen=Screen()
# print(screen)
# screen.exitonclick()
import prettytable

from prettytable import PrettyTable
x=PrettyTable()
x.add_column("City name",
["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
x.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
x.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092,
1554769])
x.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9,
869.4])
print(x)

table=PrettyTable()

table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ["Electric","Water","Fire"])
print(table)

table.align="l"
print(table)
