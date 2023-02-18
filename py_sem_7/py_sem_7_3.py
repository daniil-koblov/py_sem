# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# same

def same_by(charac, objects):
    list_characteristic = [charac(i) for i in objects]
    for i in range(len(list_characteristic) - 1):
        if list_characteristic[i] != list_characteristic[i + 1]: return False
    return True


values = [0, 2, 10, 6]    

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')




# def find_farthest_orbit(list_of_orbits):
# 	list_of_elliptical_orbits = [i for i in list_of_orbits if i[0] != i[1]]
# 	list_of_areas = [(i[0] * i[1]) for i in list_of_elliptical_orbits]
# 	max_area_index = list_of_areas.index(max(list_of_areas))
# 	return list_of_elliptical_orbits[max_area_index]