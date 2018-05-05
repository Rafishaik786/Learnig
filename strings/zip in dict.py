cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]
print(cast_names)
cast = dict(zip(cast_names, cast_heights))
print(cast)
print(type(cast))

# cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
#
# names, heights = zip(*cast)
# print(names)
# print(heights)
# Output:
# ('Barney', 'Robin', 'Ted', 'Lily', 'Marshall')
# (72, 68, 72, 66, 76)
#
#
# data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
#
# data_transpose = tuple(zip(*data))
# print(data_transpose)
# Output:
# ((0, 3, 6, 9), (1, 4, 7, 10), (2, 5, 8, 11))
#
# data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
#
# data_transpose = tuple(zip(*data))
# print(data_transpose)
# Output:
# ((0, 3, 6, 9), (1, 4, 7, 10), (2, 5, 8, 11))
#
# cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
# heights = [72, 68, 72, 66, 76]
#
# for i, character in enumerate(cast):
#     cast[i] = character + " " + str(heights[i])
#
# print(cast)
# Output:
# ['Barney Stinson 72', 'Robin Scherbatsky 68', 'Ted Mosby 72', 'Lily Aldrin 66', 'Marshall Eriksen 76']
