from grabfuctions import get_team_lines 
from grabfuctions import read_csv_to_list
from grabfuctions import flatten_team_lines
import pandas as pd
import os
filepath = '/Users/matthewdomaratzky/Documents/Oleg/MyProjects/Fantasy Hockey/FCHL2024-25/data/external/Team_List.csv'
csv_data = read_csv_to_list(filepath)
team_list = [item[0] for item in csv_data]
team_data = {}
for k in team_list:
    team_data[k]= get_team_lines(k)
print("Created Dictionary of Team Names with their Line Combos")
##lines = get_team_lines("anaheim ducks")


# Flatten the nested teams dictionary
flattened_teams = flatten_team_lines(team_data)
df = pd.DataFrame(list(flattened_teams.items()), columns=['Team_Line', 'Players'])
print("Changing file path for output")
folder_path = '/Users/matthewdomaratzky/Documents/Oleg/MyProjects/Fantasy Hockey/FCHL2024-25/data/interim'
file_name = 'team_data_v1.csv'
# Define the full file path
file_path = os.path.join(folder_path, file_name)
df.to_csv(file_path, index=False)
print(f"File saved to: {file_path}")