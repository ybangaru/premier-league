import scrapy

class NewManagerData(scrapy.Spider):

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0;'}

    name = "managerstats"
    base_url = "https://www.transfermarkt.co.in/schnellsuche/ergebnis/schnellsuche?query="
    start_urls=[]
    iters=0

    manager_ids = ["Carlo Ancelotti"]#, "Roberto Martínez", "David Moyes", "Martin Jol", "Michael Laudrup", "Paolo Di Canio","Chris Hughton",
        # "Arsène Wenger", "Malky Mackay", "Paul Lambert", "Steve Clarke", "Sam Allardyce", "Brendan Rodgers", "Mark Hughes",
        # "Mauricio Pochettino", "Ian Holloway", "José Mourinho", "André Villas-Boas", "Steve Bruce", "Alan Pardew",
        # "Manuel Pellegrini", "Kevin Ball", "Gustavo Poyet", "Keith Millen", "Tony Pulis", "René Meulensteen", "Keith Downing",
        # "Tim Sherwood", "David Kerslake", "Ole Gunnar Solskjaer", "Pepe Mel", "Garry Monk", "Felix Magath", "John Carver",
        # "Neil Adams", "Ryan Giggs", "Harry Redknapp", "Louis van Gaal", "Alan Irvine", "Nigel Pearson", "Ronald Koeman",
        # "Sean Dyche", "Neil Warnock", "Rob Kelly", "Chris Ramsey", "Dick Advocaat", "Quique Sánchez Flores", "Claudio Ranieri",
        # "Alex Neil", "Eddie Howe", "Steve McClaren", "Slaven Bilic", "Jürgen Klopp", "Kevin MacDonald", "Rémi Garde",
        # "Alan Curtis", "Steve Holland", "Guus Hiddink", "Francesco Guidolin", "Rafael Benítez", "Eric Black", "David Unsworth",
        # "Mike Phelan", "Aitor Karanka", "Walter Mazzarri", "Pep Guardiola", "Claude Puel", "Antonio Conte", "Bob Bradley",
        # "Marco Silva", "Paul Clement", "Craig Shakespeare", "Steve Agnew", "David Wagner", "Mauricio Pellegrino",
        # "Frank de Boer", "Roy Hodgson", "Michael Appleton", "Gary Megson", "Leon Britton", "Carlos Carvalhal", "Eddie Niedzwiecki",
        # "Javi Gracia", "Darren Moore", "Maurizio Sarri", "Nuno Espírito Santo", "Slavisa Jokanovic", "Unai Emery",
        # "Kelvin Davis", "Ralph Hasenhüttl", "Mark Hudson", "Jan Siewert", "Mike Stowell", "Scott Parker", "Daniel Farke",
        # "Graham Potter", "Chris Wilder", "Dean Smith", "Freddie Ljungberg", "Hayden Mullins", "Duncan Ferguson",
        # "Carlo Ancelotti", "Mikel Arteta"]

    for manager in manager_ids:
        manager = manager.split(' ')
        manager = '+'.join(manager)
        start_urls.append(base_url+manager)

    def parse(self, response):
        # open_in_browser(response)
        site_url = 'https://www.transfermarkt.co.in'
        manager_url = response.xpath("//div[@id='yw2']//a[contains(text(),'Carlo Ancelotti')]/@href").get()
        # manager_url = response.xpath("//div[@id='yw2']//a[contains(text(),'{}')]/@href".format(manager_ids[{self.iters}])).get()
        stats_url = site_url+manager_url
        self.iters+=1
        stats_url = stats_url.replace("profil","leistungsdatenDetail",1)
        yield scrapy.Request(url=stats_url, callback=self.stats_requests)


    def stats_requests(self, response):
        for item in response.xpath("//tr[@class='odd' or @class='even']"):
            match_date  = item.xpath("//td[@class='zentriert'][1]/text()").get()
            # league_name = item.xpath("//td[@class='zentriert'][2]//a/@title").get()
            season      = item.xpath("//td[@class='zentriert'][3]//a/@title").get()
            hometeam    = item.xpath("//td[@class='rechts hauptlink no-border-rechts']//a/text()").get()
            awayteam    = item.xpath("//td[@class='hauptlink no-border-links']//a/text()").get()
            result      = item.xpath("//td[@class='zentriert hauptlink']//span/text()").get()
            tactic      = item.xpath("//td[@class='zentriert'][5]/text()").get()

            yield {
                'match_date' :  match_date,
                # 'league_name' : league_name,
                'season' : season,
                'hometeam' : hometeam,
                'awayteam' : awayteam,
                'result' : result,
                'tactic' : tactic
            }