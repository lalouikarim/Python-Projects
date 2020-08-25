import requests
from bs4 import BeautifulSoup
import pandas

request = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
content = request.content
soup = BeautifulSoup(content, "html.parser")
pages_number = soup.find_all("a", {"class": "Page"})[-1].text
df_length = 0
j = 0
iterations = 0
lot_size = []
for page in range(0, int(pages_number)*10, 10):
    request = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s=" + str(page) + ".html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    all = soup.find_all("div", {"class": "propertyRow"})
    all_addresses = []
    all_fullbaths = []
    all_sqfeets = []
    all_halfbaths = []
    prices = []
    addresses = []
    beds = []
    fullbaths = []
    halfbaths = []
    sqfeet  =[]
    all_beds = []
    localities = []
    for items in all:
        prices.append(items.find("h4", {"class": "propPrice"}).text.replace("\n", "").replace(" ", ""))
        all_addresses.append(items.find_all("span", {"class": "propAddressCollapse"}))
        all_beds.append(items.find("span", {"class": "infoBed"}))
        all_fullbaths.append(items.find("span", {"class": "infoValueFullBath"}))
        all_sqfeets.append(items.find("span", {"class": "infoSqFt"}))
        all_halfbaths.append(items.find("span", {"class": "infoValueHalfBath"}))
        if "Lot Size" not in items.text:
            lot_size.append("None")
        else:
            features = items.find_all("div", {"class", "propertyFeatures"})
            for feature_name in features:
                name = feature_name.find_all("span", {"class", "featureName"})
                for size in name:
                    if "Acres" in size.text:
                        lot_size.append(size.text)
            
    for i in range(len(all_addresses)):
        addresses.append(all_addresses[i][0].text)
        localities.append(all_addresses[i][1].text)

    for i in range(len(all_beds)):
        if all_beds[i] is not None:
            beds.append(all_beds[i].find("b").text)
        else:
            beds.append("None")

    for i in range(len(all_fullbaths)):
        if all_fullbaths[i] is not None:
            fullbaths.append(all_fullbaths[i].find("b").text)
        else:
            fullbaths.append("None")

    for i in range(len(all_sqfeets)):
        if all_sqfeets[i] is not None:
            sqfeet.append(all_sqfeets[i].find("b").text)
        else:
            sqfeet.append("None")

    for i in range(len(all_halfbaths)):
        if all_halfbaths[i] is not None:
            halfbaths.append(all_halfbaths[i].find("b").text)
        else:
            halfbaths.append("None")

    if iterations == 0:
        df = pandas.DataFrame(columns = ["Address", "Area", "Beds", "Full Baths", "Half Baths", "Locality", "Lot Size", "Price"])
        df["Address"] = [address for address in addresses]
        df["Area"] = [area for area in sqfeet]
        df["Beds"] = [bed for bed in beds]
        df["Full Baths"] = [fullbath for fullbath in fullbaths]
        df["Half Baths"] = [halfbath for halfbath in halfbaths]
        df["Locality"] = [locality for locality in localities]
        df["Lot Size"] = [size for size in lot_size]
        df["Price"] = [price for price in prices]
        df_length = len(addresses)
        
    else:
        df_t = df.T
        for h in range(df_length,len(addresses)+df_length, 1):
            df_t[h] = [addresses[h-df_length], sqfeet [h-df_length], beds[h-df_length], fullbaths[h-df_length], halfbaths[h-df_length], localities[h-df_length],lot_size[h-1], prices[h-df_length]]
        df = df_t.T
        df_length += len(addresses)
    iterations += 1

df.to_csv("Propreties.csv")
'''
another method is to use a list of dictionaries;
that means store each property with its propreties in a dict and then append it to the list;
 and then df = pandas.DataFrame(l); l is the list
'''
