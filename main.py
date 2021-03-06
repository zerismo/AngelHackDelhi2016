from flask import Flask,render_template,redirect,url_for,request
import json
from functions import *
import twitter
import re, json
from statistics import mean
app = Flask("App")

api = twitter.Api(
    consumer_key='7jbKM37yIz9pPNAsVwktacerc',
    consumer_secret='iEGbqG5fNHyJSsMLuJzib27lj7lI7CIiBtbC3YiT6Z17eU0XFe',
    access_token_key='47313714-VnLZ0lFKLxQbewnxskwDB6Zbj4VnF0Fq6rbrjPqPI',
    access_token_secret='HJuA4JBGOfFy7dZRVDQihw1l7dnkxVsNpOfer8YjZ0SZ9'
)
TWEET_COUNT = 10
p = re.compile('#@')

@app.route('/index')
def index():
    return redirect('/');

@app.route('/')
def slash():
    json_string = '{"loc": {"UZ": {"trends": {"insiders": 0.5685799620527161}, "name": "Uzbekistan"}, "CH": {"trends": {"insiders": -0.23922292456576877}, "name": "Switzerland"}, "BO": {"trends": {"insiders": 0.0}, "name": "Santa Cruz de la Sierra"}, "CU": {"trends": {"insiders": 0.6904825506134059}, "name": "Santa Clara"}, "UY": {"trends": {"SaltaLaBancaEnQuienDijo": 0.0}, "name": "Salto"}, "PY": {"trends": {"insiders": 0.0}, "name": "Asuncion"}, "MX": {"trends": {"Ramn": 0.0, "insiders": 0.0013005488811418608, "LadyPagaCuentas": 0.4814048859050132, "WUCAmFootball2016": 0.0}, "name": "Mexico"}, "CR": {"trends": {"SiLaSeleGana": 0.0}, "name": "Costa Rica"}, "MY": {"trends": {"insiders": 0.2414081876256932}, "name": "Malaysia"}, "PH": {"trends": {"LaRecontraPajaCuando": 0.0, "insiders": 0.13785081381930436, "Kalayaan2016": 0.5550497032100948, "_": 0.0}, "name": "Philippines"}, "AR": {"trends": {"LaRecontraPajaCuando": 0.0, "insiders": 0.32536809167664593, "SaltaLaBancaEnQuienDijo": 0.0}, "name": "Argentina"}, "UA": {"trends": {"insiders": 0.7242245628770796}, "name": "Ukraine"}, "IE": {"trends": {"insiders": 0.4609635791416509}, "name": "Dublin"}, "GB": {"trends": {"insiders": 0.07143744782623643, "ZAYNatCapitalSTB": -0.18952665401757204, "USAvPAR": 0.0, "____6": 0.7514551223043797}, "name": "Liverpool"}, "FI": {"trends": {"insiders": 0.0}, "name": "Finland"}, "IS": {"trends": {"insiders": 0.0}, "name": "Iceland"}, "PL": {"trends": {"insiders": 0.0}, "name": "Lublin"}, "TH": {"trends": {"insiders": 0.0}, "name": "Pattaya"}, "NL": {"trends": {"insiders": 0.0}, "name": "Veenendaal"}, "JM": {"trends": {"insiders": 0.0}, "name": "Jamaica"}, "SA": {"trends": {"insiders": -0.6280145725181376}, "name": "Saudi Arabia"}, "ES": {"trends": {"insiders": 0.0}, "name": "Comunidad de Madrid"}, "JP": {"trends": {"nitiasa": 0.7786856817316798, "insiders": -0.09626937951713377}, "name": "Japan"}, "FR": {"trends": {"insiders": 0.004229513355053868, "ONPC": 0.0}, "name": "France"}, "PK": {"trends": {"insiders": 0.020349679210371802}, "name": "Pakistan"}, "CN": {"trends": {"insiders": 0.1570036431295344}, "name": "Shenzhen"}, "US": {"trends": {"insiders": 0.024657964727397716, "Maicon": 0.8236550729900429, "NewEndingsForMovies": -0.3215621839375056, "CAMZ DA LOLO": 0.0, "USAvPAR": 0.0, "__": 0.20958842058527544, "blackboysbreaktheinternet": 0.0, "Kalayaan2016": 0.6397601553767088, "Iturbe": 0.7570003110696172, "_____": 0.3380597838488043, "___": 0.06397474918919399, "Venegas": 0.35883438684865315, "_16": 0.43743115697475904, "ENGRUS": 0.0, "precure": 0.0, "COLvCRC": 0.0, "BelmontStakes": 0.0, "LaRecontraPajaCuando": 0.0, "WUCAmFootball2016": 0.7603455746964065, "____6": 0.23043114159692993}, "name": "Alaska"}, "CA": {"trends": {"insiders": 0.005232601476345269, "__": 0.0, "NewEndingsForMovies": 0.0, "BelmontStakes": 0.6745392194237302}, "name": "British Columbia"}, "NO": {"trends": {"insiders": 0.0}, "name": "Norway"}, "KE": {"trends": {"insiders": 0.6280145725181376}, "name": "Kenya"}, "BM": {"trends": {"__": 0.0}, "name": "Bermuda"}, "LB": {"trends": {"insiders": 0.0}, "name": "Beirut"}, "QA": {"trends": {"insiders": -0.3125040301150242}, "name": "Qatar"}, "NG": {"trends": {"insiders": 0.0}, "name": "Nigeria"}, "AU": {"trends": {"insiders": 0.07441857115138537, "___": 0.0, "_16": 0.0}, "name": "Australia"}, "PE": {"trends": {"DejateAtrapar": 0.0}, "name": "Lima"}, "ID": {"trends": {"insiders": 0.0, "USAvPAR": 0.0, "_": 0.3087211844733484}, "name": "Borneo"}, "CO": {"trends": {"ColLeQuitaLoRica": 0.0, "insiders": 0.29971337806805837, "CAMZ DA LOLO": 0.0, "SoyDelVerdeYEstoyTriste": 0.0, "___": 0.4973942255445647}, "name": "Colombia"}, "NP": {"trends": {"insiders": 0.0}, "name": "Nepal"}, "TR": {"trends": {"insiders": -0.26371077587989317}, "name": "Istanbul"}, "GE": {"trends": {"insiders": 0.14162363847065682}, "name": "Georgia"}, "DE": {"trends": {"insiders": 0.0}, "name": "Germany"}, "BE": {"trends": {"insiders": 0.0}, "name": "Brussels"}, "LK": {"trends": {"insiders": 0.0}, "name": "Galle"}, "BR": {"trends": {"BakeOffBrasil": 0.0, "ZAYNatCapitalSTB": 0.8310235551983771, "Maicon": 0.2523334370232057, "MeCanseiDe": 0.0, "askharmonizer": 0.0, "SPN AND TWD ARE THE BEST": 0.0, "insiders": 0.12197449547919792, "CAMZ DA LOLO": 0.0, "LacrandoComMafiaSdv": 0.0}, "name": "Brazil"}, "IN": {"trends": {"Calleri": -0.28428998102635805, "SiLaSeleGana": 0.0, "Maicon": 0.0, "NewEndingsForMovies": -0.2558851909889926, "SaltaLaBancaEnQuienDijo": 0.0, "_____": 0.0, "CAMZ DA LOLO": -0.12978094695527997, "USAvPAR": 0.0, "_": -0.1610681386210803, "blackboysbreaktheinternet": 0.08252929382315391, "BakeOffBrasil": 0.0, "Ramn": 0.19039460640931252, "__": -0.04007567022038508, "ColLeQuitaLoRica": 0.0, "LacrandoComMafiaSdv": 0.0, "Venegas": 0.0, "_16": 0.13422344885090023, "askharmonizer": 0.0, "insiders": 0.009206554844491828, "precure": 0.3087741525472067, "SPN AND TWD ARE THE BEST": 0.0, "WUCAmFootball2016": 0.39245576744816746, "COLvCRC": 0.0, "nitiasa": 0.4173670837011783, "MeCanseiDe": 0.0, "IStandByBrad": -0.10814290158137388, "ONPC": 0.0, "___": -0.11371599241054323, "Kalayaan2016": 0.0, "Iturbe": -0.048698587447799785, "ZAYNatCapitalSTB": -0.09246369836086372, "ENGRUS": 0.07911105689387486, "DejateAtrapar": 0.0, "LaRecontraPajaCuando": 0.0, "BelmontStakes": 0.09636274563196146, "LadyPagaCuentas": 0.0, "SoyDelVerdeYEstoyTriste": 0.0, "____6": 0.1570036431295344}, "name": "India"}, "IT": {"trends": {"insiders": 0.0}, "name": "Rome"}, "VE": {"trends": {"DejateAtrapar": 0.0, "insiders": 0.0, "MaduroVzlaTeDetesta": 0.0}, "name": "Venezuela"}, "SG": {"trends": {"insiders": 0.3748259753615607, "IStandByBrad": 0.0, "___": 0.0}, "name": "Singapore"}, "ZA": {"trends": {"insiders": -0.08455827597446995}, "name": "South Africa"}, "RU": {"trends": {"insiders": 0.14615607041137058}, "name": "Russia"}}, "map": [{"value": 0.5685799620527161, "name": "Uzbekistan", "code": "UZ"}, {"value": -0.23922292456576877, "name": "Switzerland", "code": "CH"}, {"value": 0.0, "name": "Santa Cruz de la Sierra", "code": "BO"}, {"value": 0.6904825506134059, "name": "Santa Clara", "code": "CU"}, {"value": 0.0, "name": "Salto", "code": "UY"}, {"value": 0.0, "name": "Asuncion", "code": "PY"}, {"value": 0.12067635869653875, "name": "Mexico", "code": "MX"}, {"value": 0.0, "name": "Costa Rica", "code": "CR"}, {"value": 0.2414081876256932, "name": "Malaysia", "code": "MY"}, {"value": 0.17322512925734979, "name": "Philippines", "code": "PH"}, {"value": 0.10845603055888198, "name": "Argentina", "code": "AR"}, {"value": 0.7242245628770796, "name": "Ukraine", "code": "UA"}, {"value": 0.4609635791416509, "name": "Dublin", "code": "IE"}, {"value": 0.158341479028261, "name": "Liverpool", "code": "GB"}, {"value": 0.0, "name": "Finland", "code": "FI"}, {"value": 0.0, "name": "Iceland", "code": "IS"}, {"value": 0.0, "name": "Lublin", "code": "PL"}, {"value": 0.0, "name": "Pattaya", "code": "TH"}, {"value": 0.0, "name": "Veenendaal", "code": "NL"}, {"value": 0.0, "name": "Jamaica", "code": "JM"}, {"value": -0.6280145725181376, "name": "Saudi Arabia", "code": "SA"}, {"value": 0.0, "name": "Comunidad de Madrid", "code": "ES"}, {"value": 0.34120815110727304, "name": "Japan", "code": "JP"}, {"value": 0.002114756677526934, "name": "France", "code": "FR"}, {"value": 0.020349679210371802, "name": "Pakistan", "code": "PK"}, {"value": 0.1570036431295344, "name": "Shenzhen", "code": "CN"}, {"value": 0.21610882669831416, "name": "Alaska", "code": "US"}, {"value": 0.16994295522501887, "name": "British Columbia", "code": "CA"}, {"value": 0.0, "name": "Norway", "code": "NO"}, {"value": 0.6280145725181376, "name": "Kenya", "code": "KE"}, {"value": 0.0, "name": "Bermuda", "code": "BM"}, {"value": 0.0, "name": "Beirut", "code": "LB"}, {"value": -0.3125040301150242, "name": "Qatar", "code": "QA"}, {"value": 0.0, "name": "Nigeria", "code": "NG"}, {"value": 0.024806190383795123, "name": "Australia", "code": "AU"}, {"value": 0.0, "name": "Lima", "code": "PE"}, {"value": 0.10290706149111613, "name": "Borneo", "code": "ID"}, {"value": 0.1594215207225246, "name": "Colombia", "code": "CO"}, {"value": 0.0, "name": "Nepal", "code": "NP"}, {"value": -0.26371077587989317, "name": "Istanbul", "code": "TR"}, {"value": 0.14162363847065682, "name": "Georgia", "code": "GE"}, {"value": 0.0, "name": "Germany", "code": "DE"}, {"value": 0.0, "name": "Brussels", "code": "BE"}, {"value": 0.0, "name": "Galle", "code": "LK"}, {"value": 0.1339257208556423, "name": "Brazil", "code": "BR"}, {"value": 0.016665980149134344, "name": "India", "code": "IN"}, {"value": 0.0, "name": "Rome", "code": "IT"}, {"value": 0.0, "name": "Venezuela", "code": "VE"}, {"value": 0.1249419917871869, "name": "Singapore", "code": "SG"}, {"value": -0.08455827597446995, "name": "South Africa", "code": "ZA"}, {"value": 0.14615607041137058, "name": "Russia", "code": "RU"}]}'
    json_string = json_string.encode('utf-8').decode('ascii','ignore')
    print(json_string)
    return render_template("index.htm",json=json_string, index = "true")

@app.route('/submit' , methods=['GET', 'POST'])
def sub():
    query = request.form['search']
    # print(query)
    # query = 'udta'
    # query_params = query.split('_')

    # print(query_params)
    # return 'Hi'
    term = None
    # since = None
    # until = None

    # for param in query_params:
    #     # Search with this keyword
    #     try:
    #         param = param.split('=')
    #         value = param[1]
    #         param = param[0]
    #     except:
    #         continue
    #     if param == 'keyword':
    #         term = value
    #     # Time period start
    #     elif param == 'start':
    #         since = value
    #     # Time period end
    #     elif param == 'until':
    #         until = value

    map_output = []
    loc_sentiments = {}
    tweet_sentiment = []
    tweets = api.GetSearch(term=query, count=TWEET_COUNT, lang='en')
    for tweet in tweets:
        text = tweet.text.encode('utf-8').decode('ascii', 'ignore')
        text = p.sub(' ', text)
        sentiment = sentiment_detect(tweet.text.encode('utf-8').decode('ascii', 'ignore'))
        location = tweet.user.location
        if not location or location == 'Global':
            location = {
                'code': 'IN',
                'label': 'India'
            }
        else:
            location = country_extract(location)
        if location['code'] in loc_sentiments:
            loc_sentiments[location['code']].append(sentiment)
        else:
            loc_sentiments[location['code']] = [sentiment]
        tweet_sentiment.append((tweet.text.encode('utf-8').decode('ascii', 'ignore'), sentiment))
    tweet_list = []
    for key in loc_sentiments:
        loc_sentiments[key] = mean(loc_sentiments[key])
        map_output.append({
            'code': key,
            'value': loc_sentiments[key]
        })

    mu = [loc_sentiments[key] for key in loc_sentiments]
    mu = mean(mu)
    

    for i in range(len(tweet_sentiment)):
        tweet_sentiment[i] = (tweet_sentiment[i][0], (tweet_sentiment[i][1]-mu)**2)
    tweet_sentiment = sorted(tweet_sentiment, key=get_key)
    if len(tweet_sentiment) > 5:
        tweet_sentiment = tweet_sentiment[:5]

    tweet_sentiment = [tweet for (tweet, s) in tweet_sentiment]

    output = str({
        "tweets": tweet_sentiment,
        "map_data": map_output
    })

    output = json.dumps(output).encode('utf-8').decode('ascii','ignore')
    output = json.loads(output)
    print(output)
    return render_template('index.htm', json=output, index = "false")

if __name__ == "__main__":
    app.run(debug=True)

