from bs4 import BeautifulSoup
import webbrowser

# Lade die HTML-Datei
with open("weather_widget.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Erstelle ein BeautifulSoup-Objekt
soup = BeautifulSoup(html_content, "html.parser")

realtemp = "1"
fealttemp = "5"
aircondition = "10"
weather = "Sonnig"

# Temperatur ändern (Beispiel: auf 10° und 2°)
temp_divs = soup.select(".weather-widget .left .temp div")
temp_divs[0].string = realtemp + "°"
temp_divs[1].string = fealttemp + "°"

# Bedingung ändern (z.B. auf „Regen“)
condition_div = soup.select_one(".weather-widget .right .condition")
condition_div.string = weather

# Luftfeuchtigkeit ändern (z.B. auf 80%)
humidity_div = soup.select_one(".weather-widget .right .humidity")
humidity_div.contents[0].replace_with(aircondition + "%")

# Speichere die Änderungen zurück in die HTML-Datei
with open("weather_widget_updated.html", "w", encoding="utf-8") as file:
    file.write(str(soup))
webbrowser.open("weather_widget_updated.html")