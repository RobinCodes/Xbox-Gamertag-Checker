import requests
import os

# User-agent
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def check_gamertag_availability(gamertag):
    url = f'https://xboxgamertag.com/search/{gamertag}'  # URL to check gamertags
    try:
        response = requests.get(url, headers=HEADERS) # send request (with user-agent)
        if response.status_code == 200:
            if "not available" in response.text.lower():  
                return False  # taken
            return True  # available
        else:
            return False  # This would run a HTTP error and messes with the output as 404 runs when a gamertag is not found
    except requests.RequestException as e:
        print(f"> Error checking {gamertag}: {e}")
        return None  # request errors (these wont be logged in working.txt)

def main(input_file, output_file):
    updated_gamertags = []

    with open(input_file, 'r') as f:
        gamertags = [line.strip() for line in f.readlines()]

    for gamertag in gamertags:
        is_available = check_gamertag_availability(gamertag)

        if is_available is True:  # Available gamertag
            print(f'> {gamertag} - Taken!')
        elif is_available is False:  # Taken or error case
            print(f'> {gamertag} - Available!')
            updated_gamertags.append(f'{gamertag}')  

    with open(output_file, 'w') as f:
        for tag in updated_gamertags:
            f.write(tag + '\n')

    print(f'\n> Available Gamertags stored in: {output_file}.')

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear') # clears command line
    print("Xbox Gamertag Checker | https://github.com/RobinCodes\n")
    to_check = 'gamertags.txt'  
    updated_gamertags_file = 'working.txt'  
    main(to_check, updated_gamertags_file)
