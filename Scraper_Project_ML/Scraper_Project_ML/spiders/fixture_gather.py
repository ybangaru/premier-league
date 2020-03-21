import scrapy
import datefinder, sys
from Scraper_Project_ML.items import LeagueTable, CompetitionRecord


class Fixture_Schedule(scrapy.Spider):

    name = "Fixture_Schedule"

    years_list = [str(item) for item in range(2014, 2020)]

    urls = "https://www.transfermarkt.com/premier-league/jahrestabelle/wettbewerb/GB1/saison_id/"

    base_url = "https://www.transfermarkt.com"

    def start_requests(self):

        # print(self.urls + self.years_list[0])

        # Get Data for Past 5 Years
        for item in self.years_list:
            # print(item)
            yield scrapy.Request(
                url=self.urls + item, callback=self.parse, meta={"season": item}
            )

        # yield scrapy.Request(
        #     url=self.urls + self.years_list[0],
        #     callback=self.parse,
        #     meta={"season": self.years_list[0]},
        # )

    def parse(self, response):

        club_season = response.meta["season"]

        # print(f"Season for request is {club_season}")

        all_column_names = response.xpath(
            "/html/body/div[2]/div[10]/div[1]/div[2]/table/thead/tr/th/text()"
        ).getall()[1:]

        # Win/Loss/Draw/PointsPerMatch
        season_stats = response.xpath(
            "/html/body/div[2]/div[10]/div[1]/div[2]/table/tbody/tr/td/text()"
        ).getall()

        # Per Club Ranking for the season(Might be useful)
        season_ranking = response.xpath(
            "/html/body/div[2]/div[10]/div[1]/div[2]/table/tbody/tr/td[@class='rechts hauptlink']/text()"
        ).getall()

        # Name of the club in a particular season
        season_club_name = response.xpath(
            "/html/body/div[2]/div[10]/div[1]/div[2]/table/tbody/tr/td[@class='no-border-links hauptlink']/a/text()"
        ).getall()

        # To get the names for leagues/competition this club was invloved in and to follow this link to get it's data
        club_schedule_link = [
            self.base_url + i + "/plus/1#EL"
            for i in response.xpath(
                "/html/body/div[2]/div[10]/div[1]/div[2]/table/tbody/tr/td[@class='no-border-links hauptlink']/a/@href"
            ).getall()
        ]

        club_ids = response.xpath(
            "/html/body/div[2]/div[10]/div[1]/div[2]/table/tbody/tr/td[@class='no-border-links hauptlink']/a/@id"
        ).getall()

        """
        Getting the Annual Premier League Standings for the Season
        """

        for table_data in response.css(
            "div.large-8.columns div.box:nth-child(2) table tbody tr"
        ):

            league_standing = table_data.css("td:nth-child(1)::text").get()
            team_name = table_data.css("td:nth-child(3) a::text").get()
            team_link = (
                self.base_url + table_data.css("td:nth-child(3) a::attr(href)").get()
            )
            club_id = int(table_data.css("td:nth-child(3) a::attr(id)").get())
            matches = int(table_data.css("td:nth-child(4)::text").get())
            win = int(table_data.css("td:nth-child(5)::text").get())
            loss = int(table_data.css("td:nth-child(6)::text").get())
            draw = int(table_data.css("td:nth-child(7)::text").get())
            goals_scored, goals_conceded = (
                table_data.css("td:nth-child(8)::text").get().split(":")
            )
            plus_minus = int(table_data.css("td:nth-child(9)::text").get())
            points_end_season = int(table_data.css("td:nth-child(10)::text").get())

            item_dict = LeagueTable()

            # print(
            #     league_standing,
            #     team_name,
            #     team_link,
            #     matches,
            #     win,
            #     loss,
            #     draw,
            #     goals_scored,
            #     goals_conceded,
            #     plus_minus,
            #     points_end_season,
            #     club_id,
            # )

            item_dict["league_standing"] = league_standing
            item_dict["team_name"] = team_name
            item_dict["team_link"] = team_link
            item_dict["total_matches"] = matches
            item_dict["wins"] = win
            item_dict["loss"] = loss
            item_dict["draw"] = draw
            item_dict["goals_scored"] = int(goals_scored)
            item_dict["goals_conceded"] = int(goals_conceded)
            item_dict["plus_minus"] = plus_minus
            item_dict["Points"] = points_end_season
            item_dict["club_id"] = club_id
            item_dict["season"] = club_season
            item_dict["collection_name"] = "League"

            yield item_dict

            # sys.exit()

        for link, _id, name in zip(club_schedule_link, club_ids, season_club_name):
            # print(link, _id, name)
            yield scrapy.Request(
                url=link,
                callback=self.schedule_parse,
                meta={"season": club_season, "club_name": name, "club_id": _id},
            )

    def schedule_parse(self, response):

        """
        Here we parse the competition names and include detail stats about the match that this particular team was involved in

        Getting the Club Name from The Previous Request and the year also so we can add all the data here itself
        """

        # print(
        #     f"Response for {response.meta['club_name']},{response.meta['season']},{response.meta['club_id']} is {response}"
        # )

        # Names for each competition
        # all_competition_names = response.xpath(
        #     "/html/body/div[2]/div[10]/div[1]/div[@class='box']/div[@class='table-header']/h2/a/text()"
        # ).getall()

        # Table Columns(Get Only Once)
        # competition_columns = response.xpath(
        #     '/html/body/div[2]/div[10]/div/div[@class="box"]/div[@class="responsive-table"]/table/thead/tr/th/text()'
        # ).get()

        # MathcDay Info(Might not be the same)
        # matchday_info = response.xpath(
        #     '/html/body/div[2]/div[10]/div/div[@class="box"]/div[@class="responsive-table"]/table/tbody/tr/td[@class="zentriert"][1]/text()'
        # ).getall()

        # Date Info
        # date_info = response.xpath(
        #     '/html/body/div[2]/div[10]/div/div[@class="box"]/div[@class="responsive-table"]/table/tbody/tr/td[2]/text()'
        # ).getall()

        # Time Info
        # time_info = response.xpath(
        #     '/html/body/div[2]/div[10]/div/div[@class="box"]/div[@class="responsive-table"]/table/tbody/tr/td[@class="zentriert"][2]/text()'
        # ).getall()

        # Home Team
        # home_team = response.xpath(
        #     '/html/body/div[2]/div[10]/div/div[@class="box"]/div[@class="responsive-table"]/table/tbody/tr/td[5]/a/text()'
        # ).getall()

        # Away Team
        # away_team = response.xpath(
        #     '/html/body/div[2]/div[10]/div/div[@class="box"]/div[@class="responsive-table"]/table/tbody/tr/td[7]/a/text()'
        # ).getall()

        # Formation
        # formation = response.xpath(
        #     '/html/body/div[2]/div[10]/div/div[@class="box"]/div[@class="responsive-table"]/table/tbody/tr/td[8]/text()'
        # ).getall()

        # Coach For Match
        # coach_for_match = response.xpath(
        #     '/html/body/div[2]/div[10]/div/div[@class="box"]/div[@class="responsive-table"]/table/tbody/tr/td[9]/a/text()'
        # ).getall()

        # Match_result
        # match_result = response.xpath(
        #     '/html/body/div[2]/div[10]/div/div[@class="box"]/div[@class="responsive-table"]/table/tbody/tr/td[11]/a/span/text()'
        # ).getall()

        # Match_Statistics_Link

        # match_stats_link = [
        #     self.base_url + i
        #     for i in response.xpath(
        #         '/html/body/div[2]/div[10]/div/div[@class="box"]/div[@class="responsive-table"]/table/tbody/tr/td[11]/a/@href'
        #     ).getall()
        # ]

        # Loop to loop in Data for Div with League Matches which we want
        for data in [
            x for x in response.css("div.box") if x.css("div.table-header h2 a[name]")
        ]:

            # Dynamic Competition Name Per Div Box
            competition_name = data.css("div.table-header img::attr(title)").get()
            # print(competition_name)

            pipeline_dict = CompetitionRecord()
            pipeline_dict["competition_name"] = competition_name
            pipeline_dict["club_name"] = response.meta["club_name"]
            pipeline_dict["season"] = response.meta["season"]
            pipeline_dict["club_id"] = int(response.meta["club_id"])

            # Individual Competition Row
            for row in data.css("div.responsive-table table tbody tr"):
                # Separate for Premier Leaague and Other Leagues
                match_day = row.css("td:first_child::text").get().strip(
                    "\n\t"
                ) or row.css("td:first_child a::text").get().strip("\n\t")

                # We can use some Sort of List Unpacking here but this strucutre is more
                # explicit hence I prefer it
                match_date = list(
                    datefinder.find_dates(row.css("td:nth-child(2)::text").get())
                )[0].strftime("%d-%m-%Y")
                match_time = row.css("td:nth-child(3)::text").get()
                home_team = row.css("td:nth-child(5) a::text").get()
                away_team = row.css("td:nth-child(7) a::text").get()
                play_style = row.css("td:nth-child(8)::text").get()
                coach = row.css("td:nth-child(9) a::text").get()
                result = row.css("td:nth-child(11) a span::text").get()
                match_result_link = (
                    self.base_url + row.css("td:nth-child(11) a::attr(href)").get()
                )

                home_score, away_score = result.split(":")

                pipeline_dict["match_type"] = match_day
                pipeline_dict["match_date"] = match_date
                pipeline_dict["match_time"] = match_time
                pipeline_dict["home_team"] = home_team
                pipeline_dict["away_team"] = away_team
                pipeline_dict["play_style"] = play_style
                pipeline_dict["coach"] = coach
                pipeline_dict["result"] = result
                pipeline_dict["home_score"] = int(home_score)
                pipeline_dict["away_score"] = int(away_score)
                pipeline_dict["match_result_link"] = match_result_link
                pipeline_dict["collection_name"] = "Competition"

                # print(pipeline_dict)

                yield pipeline_dict
                # print(
                #     match_day,
                #     match_date,
                #     match_time,
                #     home_team,
                #     away_team,
                #     play_style,
                #     coach,
                #     result,
                #     match_result_link,
                # )
