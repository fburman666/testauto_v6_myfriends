from playwright.sync_api import sync_playwright, expect
from behave import given, when, then
from time import sleep



#Som en användare vill jag kunna visa lista med alla mina vänner så att jag kan skryta om hur många jag har
@given(u'användaren är inloggad på startsidan')
def step_given_user_at_start_page(context):
    context.page.goto(context.base_url)


@when(u'användaren klickar på knappen "Vänlista"')
def step_when_user_clicks_friendslist(context):
    friends_button = context.page.get_by_role("link", name="Vänlista")
    friends_button.click(timeout=200)
    #sleep(2)


@then(u'listan med vänner visas')
def step_check_friends_list(context):
    friend = context.page.get_by_text("William Riker")
    expect(friend).to_have_count(1, timeout=200)


 #Som en användare vill jag kunna ändra uppgifter för en vän så att info är rätt när vännerna ändrar status
@given(u'användaren är inloggad på "friends"-sidan')
def step_given_user_at_friends_page(context):
    context.page.goto(context.friends_url)


@when(u'användaren klickar på "Ändra" för vännen "Data"')
def step_user_clicks_update_data(context):
    update_button = context.page.get_by_role("main").locator("div").filter(has_text="Data android.data@starfleet.").locator("a")
    update_button.click()

@when(u'användaren ändrar email till: "paranoid.android.data@starfleet.com"')
def step_user_updates_email(context):
    email_textbox = context.page.get_by_role("textbox").nth(1)
    new_email_address = "paranoid.android.data@starfleet.com"
    email_textbox.fill(new_email_address)
    sleep(2)

@when(u'användaren klickar på knappen "Spara"')
def step_user_clicks_save(context):
    save_button = context.page.get_by_role("button", name="Spara")
    save_button.click()

@then(u'listan med vänner visas med den uppdaterade informationen')
def step_check_new_email_address(context):
    new_email = context.page.get_by_text("paranoid.android.data@starfleet.com")
    expect(new_email).to_be_visible(timeout=200)


  #Som en användare vill jag kunna ta bort en vän så att listan är rätt ifall vännen blir en ovän
@given(u'användaren är åter inloggad på "friends"-sidan')
def step_given_user_at_friends_page(context):
    context.page.goto(context.friends_url)

@when(u'användaren klickar på "Ta bort" för vännen "Spock"')
def step_remove_spock_from_list(context):
    remove_button = context.page.get_by_role("main").locator("div").filter(has_text="Spock science.officer.spock@").locator("button")
    remove_button.click(timeout=200)

@then(u'Spock försvinner ur listan')
def step_check_that_spock_is_gone(context):
    friends_list = context.page.get_by_text("Spock")
    expect(friends_list).to_be_hidden(timeout=200)



#Som en användare vill jag kunna söka efter vänner baserat på namn, oberoende av stora eller små bokstäver så att sökningen blir enkel
@given(u'användaren är ännu en gång inloggad på "friends"-sidan')
def step_given_user_at_friends_page(context):
    context.page.goto(context.friends_url)


@when(u'användaren anger "jean" i sökfältet')
def step_search_for_jean(context):
    textbox = context.page.get_by_role("textbox", name="Sök namn")
    textbox.fill("jean")

@then(u'Jean-Luc visas i vänlistan men ingen annan vän')
def step_check_friends_list(context):
    friends = context.page.get_by_text("@")
    friend_jean_luc = context.page.get_by_text("Jean-Luc")
    expect(friends).to_have_count(1, timeout=200)
    expect(friend_jean_luc).to_have_count(1, timeout=200)


