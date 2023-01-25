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



#print the name of the first class on Wednesday in room 612, with the name of the prof and when the start is.
#please note my output formate: <class name> - <prof name> - <start time>
print(schedule['wednesday'][612][0]['class'],'-',schedule['wednesday'][612][0]['prof'],'-',schedule['wednesday'][612][0]['start'])

#output sample (not the correct output:

# ❯ python3 pratt_schedule3.py
# Human-Information Behavior - Pattuelli - 6.5


