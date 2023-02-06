schedule = {
	"monday" : {

				612 : [
						{
							'class' : 'Human-Information Behavior',
							'prof'	: 'Pattuelli',
							'start'	: 6.5
						},
						{
							'class' : 'Information Professions',
							'prof'	: 'Lopatovska',
							'start'	: 12.5
						}
					],
				611	:[
						{
							'class' : 'Research Mthds/Law Lit',
							'prof'	: 'Hollander',
							'start'	: 3.5
						},
						{
							'class' : 'Strategic Leadership',
							'prof'	: 'Norberg',
							'start'	: 6.5
						}
					],
				602	:[
						{
							'class' : 'Conservation and Preservation',
							'prof'	: 'Hagadorn',
							'start'	: 6.5
						}
					],
				609	:[
						{
							'class' : 'Info Services & Resources',
							'prof'	: 'Drabinski',
							'start'	: 6.5
						}
					]
			},

	"tuesday": {

				609 : [

						{
							'class' : 'Information Arch/Inter Design',
							'prof'	: 'MacDonald',
							'start'	: 3.5
						},
						{
							'class' : 'Information Arch/Inter Design',
							'prof'	: 'MacDonald',
							'start'	: 6.5
						}
				],

				611 : [

						{
							'class' : 'Information Professions',
							'prof'	: 'Berry',
							'start'	: 6.5
						}
				],

				613 : [
						{
							'class' : 'Acad Libraries and Scholarly',
							'prof'	: 'Rabina',
							'start'	: 6.5
						},
						{
							'class' : 'Info Services & Resources',
							'prof'	: 'Rabina',
							'start'	: 3.5
						}
				]
			},

	"wednesday": {

				609 : [

						{
							'class' : 'Info Services & Resources',
							'prof'	: 'Kroski',
							'start'	: 6.5
						},
						{
							'class' : 'Usability Theory & Practice',
							'prof'	: 'MacDonald',
							'start'	: 3.5
						}
				],

				612 : [

						{
							'class' : 'Mgmt of Archives/Sp Collection',
							'prof'	: 'Cucchiara',
							'start'	: 3.5
						}
				],

				613 : [
						{
							'class' : 'Government Info Sources',
							'prof'	: 'Rabina',
							'start'	: 6.5
						}
				],

				410 : [
						{
							'class' : 'Library Media Centers',
							'prof'	: 'Taylor-Swee',
							'start'	: 3.5
						}
				],

				702 : [
						{
							'class' : 'Mgmt of Archives/Sp Collection',
							'prof'	: 'Cucchiara',
							'start'	: 6.5
						}
				]
			},

	"thursday": {

				611 : [

						{
							'class' : 'Information Science Research',
							'prof'	: 'Lopatovska',
							'start'	: 3.5
						}
				],

				612 : [
						{
							'class' : 'Information Professions',
							'prof'	: 'Lopatovska',
							'start'	: 6.5
						}
				],

				410 : [
						{
							'class' : 'Information Professions',
							'prof'	: 'Sula',
							'start'	: 3.5
						}
				]
			}
}



#loop through each day, print out the day name.
#Sort the rooms for the day and loop through them and print the room number.
#Then loop through each class and print it out.



# for day, class_room_dict in schedule.items():
# 	print(day)

# 	room_nums = class_room_dict.keys()
# 	sorted_room_num = sorted(room_nums)

# 	for room_num in sorted_room_num:
# 			courses = class_room_dict[room_num]
# 			print(room_num)
# 			for course in courses:
# 				print(course["class"])


for weekday, classes_info_dict1 in schedule.items():
	print(weekday)

	rooms = classes_info_dict1.keys()
	sorted_rooms = sorted(rooms)

	for room in sorted_rooms:
		classes_info_dict2 = classes_info_dict1[room]
		print(room)
		for course in classes_info_dict2:
			print(course['class'])



#output sample:

# ❯ python3 pratt_schedule3.py
# monday
# 602
# Conservation and Preservation
# 609
# Info Services & Resources
# ...


