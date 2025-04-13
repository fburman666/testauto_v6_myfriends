from playwright.sync_api import sync_playwright

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser_type = context.playwright.chromium
    context.browser = context.browser_type.launch(headless=False)

def before_scenario(context, scenario):
    context.page = context.browser.new_page()
    context.base_url = "https://forverkliga.se/JavaScript/my-contacts/#/"
    context.friends_url = "https://forverkliga.se/JavaScript/my-contacts/#/friends"

def after_scenario(context, scenario):
    if context.page:
        context.page.close()

def after_all(context):
    if context.browser:
        context.browser.close()
    if context.playwright:
        context.playwright.stop()