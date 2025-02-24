from bs4 import BeautifulSoup
import requests
import csv


date = input("Enter the data in this format MM/DD/YYYY needed for the champion: ")
HEADER = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/116.0.0.0' ,'Accep-Language':'en-US;q=0.5'})
page = requests.get(f"https://www.yallakora.com/Match-Center/?date={date}",headers=HEADER)


def main(page):

    matches_detail = []

    if page.status_code == 200:
        src = page.content
        soup = BeautifulSoup(src, 'lxml')
        championships = soup.find_all('div', {'class': 'matchCard'})
        number_of_championships = len(championships)
             
    def scraping_match_info(championships):
        championship_title = championships.find('div', class_="title").find('h2').text.strip()
        all_matches = championships.find_all('div', class_= 'teamsData')
        number_of_matches = len(all_matches)

        for i in range(number_of_matches):
           
            teamA = all_matches[i].find('div', class_='teamA').text.strip()
            teamB = all_matches[i].find('div', class_='teamB').text.strip()
            
                      
            match_result = all_matches[i].find('div', class_='MResult').find_all('span', class_='score')
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
            
            match_time = all_matches[i].find('div', class_='MResult').find('span', class_='time').text.strip()

           
            matches_detail.append({
                "Championship Title": championship_title,
                "Team 1": teamA,
                "Team 2": teamB,
                "Score": score,
                "Timing": match_time
            })

    for i in range(number_of_championships):
        scraping_match_info(championships[i])    
    
    keys = matches_detail[0].keys()

    with open(r'C:\Users\pc\Desktop\DataPipeline/matchs_file.csv', 'w', encoding='UTF-8') as matches_file:

        dict_writer = csv.DictWriter(matches_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(matches_detail)
        print("file created successfully")

    print(matches_detail)
main(page=page)