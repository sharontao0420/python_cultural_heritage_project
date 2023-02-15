


# nat_count_dict = {}

# with open('Artworks1.csv') as file:
#     processed_art_csv = csv.DictReader(file)
#     # head()

#     for art in processed_art_csv:
#         nats = art['Nationality'].split(' ')
#         for nat in nats: # french | america
#             new_count = nat_count_dict.get(nat, 0) + 1
#             nat_count_dict[nat] = new_count
# # print(nat_count_dict)

# for nat in nat_count_dict:
#     print('{}:{}'.format(nat,nat_count_dict[nat]))




#split out the art pieces into separate csv files. One for each nationality e.g. `(Belgian).csv`
#All those files should be in a sub folder called ‘res’ (make sure you create the folder manually before running your script
import csv
import os

os.makedirs('res', exist_ok=True)

nationality_writers = {}
# nationality_writers = {'belgian':{'file':"", 'csv':''}}



with open('Artworks.csv') as file:
  processed_csv = csv.reader(file)
  header_row = next(processed_csv,None)
  for row in processed_csv:
    nationalities_str = row[4]
    nationalities = nationalities_str.split(' ')
    
    for nat in nationalities:
      if nat not in nationality_writers:
        nat_file = open(f'res/{nat}.csv', 'w')
        nat_writer = csv.writer(nat_file)
        nat_writer.writerow(header_row)
        nat_writer.writerow(row)
        nationality_writers[nat] = nat_writer
      else:
        nationality_writers[nat].writerow(row)

# for files in nationality_writers:
#   nationality_writers[files]['file'].close()







