import requests
from base_operator import BaseOperator
from ai_context import AiContext
from bs4 import BeautifulSoup

class LinkedInScraper(BaseOperator):
    @staticmethod
    def declare_name():
        return 'LinkedInScraper'
    
    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.ACT.value
    
    @staticmethod
    def declare_parameters():
        return []
    
    @staticmethod
    def declare_inputs():
        return [
            {
                "name": "profile_urls",
                "data_type": "string []"
            }
        ]
    
    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "profile_infos",
                "data_type": "string []"
            }
        ]
        
    def run_step(self, step, ai_context: AiContext):
        profile_urls = ai_context.get_input('profile_urls', self)
        profile_infos = []
        for profile_url in profile_urls:
            # Use requests to get the HTML content of the LinkedIn profile page
            page = requests.get(profile_url)
            soup = BeautifulSoup(page.content, 'html.parser')

            # use BeautifulSoup to scrape the desired information from the page
            profile_info = soup.find('main', class_='scaffold-layout__main')
            profile_infos.append(profile_info.get_text())
            
            ai_context.set_output('profile_infos', self, profile_infos)

            
           

            # # Extract the profile location
            # profile_location = soup.find('span', class_='text-body-small inline t-black--light break-words').text
            # profile_infos.append(profile_location)

            # # Extract the profile headline
            # profile_headline = soup.find('div', class_='text-body-medium break-words').text
            # profile_infos.append(profile_headline)

            # # Extract the profile summary
            # profile_summary = soup.find('div', class_='pv-shared-text-with-see-more full-width t-14 t-normal t-black display-flex align-items-center').text
            # profile_infos.append(profile_summary)

            # # Extract the profile's number of followers
            # num_followers = soup.find('p', class_='pvs-header__subtitle pvs-header__optional-link text-body-small').text
            # profile_infos.append(num_followers)

            
            # # Extract the job titles from the profile
            # job_title = soup.find('div', class_='display-flex align-items-center mr1 t-bold').text
            # profile_infos.append(job_title)


