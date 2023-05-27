from playwright.sync_api import sync_playwright

HOSTNAME = "https://codingcompetitions.withgoogle.com"
YEARS = [2013]
# PORXY_SERVER = "http://localhost:10809"
PORXY_SERVER = "http://172.29.128.1:10809"


def get_archive_link(year):
    ARCHIVE_ROOT = "/kickstart/archive"
    return HOSTNAME + ARCHIVE_ROOT + "/" + str(year)


def get_full_link(path):
    return HOSTNAME + path


with sync_playwright() as p:
    round_name_to_link = {}

    browser = p.chromium.launch(proxy={"server": PORXY_SERVER}, headless=False)
    page = browser.new_page()

    for year in YEARS:
        page.goto(get_archive_link(year))
        page.wait_for_selector(
            '//div[@class="schedule-row schedule-row__past"]')
        for round in page.query_selector_all(
                '//div[@class="schedule-row schedule-row__past"]'):
            round_name = round.query_selector("//span").inner_text()
            round_link = round.query_selector("//a").get_attribute("href")
            round_name_to_link[round_name] = round_link

    print(round_name_to_link)

    for round_name, round_link in round_name_to_link.items():
        problem_title_to_link = {}

        print(get_full_link(round_link))
        page.goto(get_full_link(round_link))
        for problem in page.query_selector_all(
                '//div[@class="problems-nav-selector-item-container section-row-column"]'
        ):
            problem_title = problem.query_selector("//p").inner_text()
            problem_link = problem.query_selector("//a").get_attribute("href")
            problem_title_to_link[problem_title] = problem_link

        print(problem_title_to_link)

        for problem_title, problem_link in problem_title_to_link.items():
            print(get_full_link(problem_link))

            page.goto(get_full_link(problem_link) + "#problem")
            problem = page.query_selector(
                '//div[@class="problem-description problem-analysis-detail"]')
            print(problem.inner_html())

            # TODO: also crawl analysis
            # page.goto(get_full_link(problem_link) + "#analysis")

    browser.close()
