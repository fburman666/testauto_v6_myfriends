Feature: Lägga till och hantera vänner i "mina vänner" appen
#Som en användare vill jag kunna visa lista med alla mina vänner så att jag kan skryta om hur många jag har
  Scenario: visa lista med alla mina vänner
    Given användaren är inloggad på startsidan
    When användaren klickar på knappen "Vänlista"
    Then listan med vänner visas

  #Som en användare vill jag kunna ändra uppgifter för en vän så att info är rätt när vännerna ändrar status
  Scenario: Editering av väninfo
    Given användaren är inloggad på "friends"-sidan
    When användaren klickar på "Ändra" för vännen "Data"
    And användaren ändrar email till: "paranoid.android.data@starfleet.com"
    And användaren klickar på knappen "spara"
    Then listan med vänner visas med den uppdaterade informationen