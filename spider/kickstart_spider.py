from playwright.sync_api import sync_playwright

HOSTNAME = "https://codingcompetitions.withgoogle.com"

YEARS = [x for x in range(2013, 2023)]


def get_archive_link(year):
    ARCHIVE_ROOT = "/kickstart/archive"
    return HOSTNAME + ARCHIVE_ROOT + "/" + str(year)


def get_full_link(path):
    return HOSTNAME + path


round_name_to_link = {}
with sync_playwright() as p:
    browser = p.chromium.launch(proxy={"server": "http://localhost:10809"},
                                headless=False)
    page = browser.new_page()

    for year in YEARS:
        page.goto(get_archive_link(year))
        for schedule_row in page.query_selector_all(
                '//div[@class="schedule-row schedule-row__past"]'):
            round_name = schedule_row.query_selector("//span").inner_text()
            round_link = schedule_row.query_selector("//a").get_attribute(
                "href")
            round_name_to_link[round_name] = get_full_link(round_link)
    browser.close()

print(len(round_name_to_link))
print(round_name_to_link)
