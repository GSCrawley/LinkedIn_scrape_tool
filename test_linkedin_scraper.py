from linkedin_scraper import LinkedinScraper
from ai_context import AiContext

def test_linkedin_scraper():
    #Create a mock AI context
    ai_context = AiContext()

    #Set the input value for the operator in the AI context
    profile_urls = ['https://www.linkedin.com/in/gscrawley/']

    ai_context.set_input('profile_urls', LinkedinScraper, profile_urls)

    #Create an instance of the operator and run it
    linkedin_scraper = LinkedinScraper()
    
    linkedin_scraper.run_step({}, ai_context)

    #Get the output value from the AI context
    profile_infos = ai_context.get_output('profile_infos', LinkedinScraper)

    # Assert that the ouput value is correct
    assert len(profile_infos) == 1
    profile_info = profile_infos[0]

    assert 'Gideon Crawley' in profile_info
    assert 'San Francisco Bay Area' in profile_info
    assert 'Websites / Desktop & Mobile Apps / Streamlining business processes through automation.' in profile_info