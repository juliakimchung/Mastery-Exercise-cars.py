makes = (
  (1, "Toyota"), (2, "Nissan"),
  (3, "Ford"), (4, "Mini"),
  (5, "Honda"), (6, "Dodge"),
)

models = (
  (1, "Altima", 2), (2, "Thunderbird", 3),
  (3, "Dart", 6), (4, "Accord", 5),
  (5, "Prius", 1), (6, "Countryman", 4),
  (7, "Camry", 1), (8, "F150", 3),
  (9, "Civic", 5), (10, "Ram", 6),
  (11, "Cooper", 4), (12, "Pilot", 5),
  (13, "Xterra", 2), (14, "Sentra", 2),
  (15, "Charger", 6)
)

colors = (
  (1, "Black" ), (2, "Charcoal" ), (3, "Red" ), (4, "Brick" ),
  (5, "Blue" ), (6, "Navy" ), (7, "White" ), (8, "Ivory" )
)

available_car_colors = (
  (1, 1), (1, 2), (1, 7), 
  (2, 1), (2, 3), (2, 7), 
  (3, 2), (3, 3), (3, 7), 
  (4, 3), (4, 5), (4, 8),
  (5, 2), (5, 4), (5, 8), 
  (6, 2), (6, 6), (6, 7), 
  (7, 1), (7, 3), (7, 7), 
  (8, 1), (8, 5), (8, 8),
  (9, 1), (9, 6), (9, 7), 
  (10, 2), (10, 5), (10, 7), 
  (11, 3), (11, 6), (11, 8), 
  (12, 1), (12, 4), (12, 7),
  (13, 2), (13, 6), (13, 8), 
  (14, 2), (14, 5), (14, 8), 
  (15, 1), (15, 4), (15, 7)
)
for make in makes:
    for model in models:
        if make[0] == model[2]:
            print ("\n" + "{:-^24s}".format(make[1]))
            print("\n"+ model[1] + " is available in ")
            for available_color in available_car_colors:
                if available_color[0] == model[0]:
                    for color in colors:
                        if available_color[1] == color[0]:
                            print( "".join(color[1])  )



make = [(make[1], model[1], color[1] ) for make in makes for model in models for available_color in available_car_colors for color in colors if make[0] == model[2] if available_color[0]== model[0] if available_color[1] == color[0]]
print(make)

print("\n" + "{:-^44s}".format(make[0][0]))
print(make[0][1] + " is avaialble in " + make[0][2] + ", " + make[1][2] + ", " + make[2][2])

print(make[3][1] + " is available in " + make[3][2] + ", " + make[4][2] + ", " + make[5][2])

print(make[6][1] + " is available in " + make[6][2] + ", " + make[7][2] + ", " + make[8][2])



d = { make[1]:  {model[1]: [color[1] for available_color in available_car_colors if available_color[0] == model[0] for color in colors   if available_color[1] == color[0]] for model in models if make[0] == model[2] }  for make in makes  }
print(d)



Toyota = {}
Toyota["Prius"] = ["Charcoal", "Brick", "Ivory"]
Toyota["Camry"] = ["Black", "Red", "White"]
print(Toyota)
print({k + " is available in " + v[0] + "," + v[1] + "," + v[2] for (k,v) in Toyota.items()})




# model = [model for model in models if model[1] == "Accord" ]
# print("\n" + model[0][1] + " is available in")
# available_color = [ available_color for available_color in available_car_colors]
# color =[color for color in available_color ]
# print(model)
# print(color)

# makes = {'make': {'model': ['color']} for 'model', 'color' in 'make'['model'].items()}
# print(makes)

# cars = {
#         'Toyota' : {
#                 'Prius': ['Charcoal', 'Brick', 'Ivory'],
#                 'Camry': ['Black', 'Red', 'White']
#             },
#         'Nissan' : {
#                 'Altima': ['Black', 'Charcoal', 'White'],
#                 'Xterra': ['Charcoal', 'Navy', 'Ivory'],
#                 'Sentra': ['Charcoal', 'Blue', 'Ivory']
#             },
#         'Ford' :  {
#                 'Thunderbird': ['Charcoal', 'Red', 'White'],
#                 'F150': ['Black', 'Blue', 'Ivory']
#             },
#         'Mini' :  {
#                 'Countryman': ['Charcola', 'Navy', 'White'],
#                 'Cooper': ['Red', 'Blue','White']
#             },
#         'Honda' : {
#                 'Accord': ['Red', 'Blue', 'Ivory'],
#                 'Civic': ['Black', 'Navy', 'White'],
#                 'Pilot': ['Black', 'Brick', 'White']
#             },
#         'Dodge' : {
#                 'Dart': ['Charcoal', 'Red', 'White'],
#                 'Ram' : ['Charcoal', 'Blue', 'White'],
#                 'Charger': ['Black', 'Brick', 'White']
#             }
# }

# for maker, value in cars.items():
#     for model, color in cars[maker].items():
#         print(model + " is available in " + color[len(color)-2] + ", "+ color[len(color)-1] + ", " + color[len(color)-len(color)] + ".")

# car_color_availability = []
# for key, value in cars.items():
#     print(key)
#     print(value)


# for model, color in Nissan.items():
#     # for n in range(len(color)):
#         print(model + " is available in " + color[len(color)-2] + ", " + color[len(color)-1] + ", " + color[len(color)-len(color)])

# for model, color in Ford.items():
#     # for n in range(len(color)):
#         print(model + " is available in " + color[0] + ", " + color[1] + ", " + color[2])

# for model, color in Mini.items():
#     # for n in range(len(color)):
#         print(model + " is available in " + color[0] + ", " + color[1] + ", " + color[2])


# for model, color in Honda.items():
#     # for n in range(len(color)):
#         print(model + " is available in " + color[0] + ", " + color[1] + ", " + color[2])

# for model, color in Dodge.items():
#     # for n in range(len(color)):
#     print(model + " is available in " + color[0] + ", " + color[1] + ", " + color[2])


# T = list(cars['Toyota'].items())
# N = list(cars['Nissan'].items())
# # F = list(Ford.items())
# # M = list(Mini.items())
# # H = list(Honda.items())
# # D = list(Dodge.items())

# print(T)
# print(N)
# print(T[0][0])
# pirus = T[0][0]
# camry = T[1][0]
# print(camry)
# print(pirus)
# print(pirus + " is available in " + T[0][1][0] + "," + T[0][1][1] + "," + T[0][1][2])
# print(camry + " is available in " + T[1][1][0] + "," + T[1][1][1] + "," +T[1][1][2])


























