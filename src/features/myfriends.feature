Feature: Lägga till och hantera vänner i "mina vänner" appen

#Som en användare vill jag kunna visa lista med alla mina vänner så att jag kan skryta om hur många jag har
  Scenario: visa lista med alla mina vänner
    Given användaren är inloggad på startsidan
    When användaren klickar på knappen "Vänlista"
    Then listan med vänner visas

  #Som en användare vill jag kunna ändra uppgifter för en vän så att info är rätt när vännerna ändrar status
  Scenario: Lyckad editering av vännen Datas email-adress
    Given användaren är inloggad på "friends"-sidan
    When användaren klickar på "Ändra" för vännen "Data"
    And användaren ändrar email till: "paranoid.android.data@starfleet.com"
    And användaren klickar på knappen "spara"
    Then listan med vänner visas med den uppdaterade informationen

 #Som en användare vill jag kunna ta bort en vän så att listan är rätt ifall vännen blir en ovän
 Scenario: Lyckad borttagning av en vän som blivit ovän
  Given användaren är åter inloggad på "friends"-sidan
  When användaren klickar på "Ta bort" för vännen "Spock"
  Then Spock försvinner ur listan





#Som en användare vill jag kunna söka efter vänner baserat på namn, oberoende av stora eller små bokstäver så att sökningen blir enkel
Scenario: Lyckad sökning efter kamraten Jean-Luc
  Given användaren är ännu en gång inloggad på "friends"-sidan
  When användaren anger "jean" i sökfältet
  Then Jean-Luc visas i vänlistan men ingen annan vän




#Som en användare vill jag kunna söka efter vänner baserat på e-post, oberoende av stora eller små bokstäver så att sökningen blir enkel
#Som en användare vill jag kunna lägga till ny vän så att jag får många vänner
#Som en användare vill jag kunna se om formuläret visar ett felmeddelande när inte båda (ny vän-)fälten är ifyllda så att jag ser att något gick fel
