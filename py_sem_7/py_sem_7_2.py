# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

def find_farthest_orbit(orbits):
    pi = 3.14
    orbits_new = [(0, 0)]
    max = 0
    for i in orbits:
        if i[0] != i[1] and max < pi * i[0] * i[1]:
            max = pi * i[0] * i[1]
            orbits_new.pop()
            orbits_new.append(i)
    return orbits_new[0]

print(*find_farthest_orbit(orbits))

# def find_farthest_orbit(list_of_orbits):
# 	list_of_elliptical_orbits = [i for i in list_of_orbits if i[0] != i[1]]
# 	list_of_areas = [(i[0] * i[1]) for i in list_of_elliptical_orbits]
# 	max_area_index = list_of_areas.index(max(list_of_areas))
# 	return list_of_elliptical_orbits[max_area_index]