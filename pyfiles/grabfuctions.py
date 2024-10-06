import requests
import os
from bs4 import BeautifulSoup

def get_team_lines(team_name):
   
    # URL for the team line combinations on DailyFaceoff
    url = f'https://www.dailyfaceoff.com/teams/{team_name}/line-combinations'
    # Custom headers to mimic a real browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Send a GET request to the page with the custom headers
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the page content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all img tags that contain player names in the 'alt' attribute
        img_tags = soup.find_all('img', alt=True)

        # List to store player names
        players = []

        # Loop through the img tags and filter out only those with 'player' in their src attribute
        for img_tag in img_tags:
            if 'player' in img_tag['src']:
                player_name = img_tag['alt']
                players.append(player_name)

        # Check if there are enough players to form lines
        if len(players) >= 23:
            # Group the players into lines and pairings
            lines = {
                "Line 1": players[:3],
                "Line 2": players[3:6],
                "Line 3": players[6:9],
                "Line 4": players[9:12],
                "Defensive Pairing 1": players[12:14],
                "Defensive Pairing 2": players[14:16],
                "Defensive Pairing 3": players[16:18],
                "Powerplay": players[18:23]
            }

            return lines  # Return the lines dictionary
        else:
            return {"Error": "Not enough players found to fill all lines and pairings."}

    else:
        return {"Error": f"Failed to retrieve data for {team_name}. Status code: {response.status_code}"}
import csv

def read_csv_to_list(file_path):
    data_list = []
    
    # Open the CSV file
    with open(file_path, mode='r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        
        # Iterate over the rows in the CSV file
        for row in csv_reader:
            # Append each row (as a list) to the data_list
            data_list.append(row)
    
    return data_list

def flatten_team_lines(teams_dict):
    flat_dict = {}
    
    # Loop through each team and its lines
    for team, lines in teams_dict.items():
        for line, players in lines.items():
            # Create a new key in the format 'Team_Line'
            new_key = f'{team}_{line}'
            flat_dict[new_key] = players
    
    return flat_dict