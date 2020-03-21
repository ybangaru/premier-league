import scrapy
import datefinder, sys
from Scraper_Project_ML.items import Manager_Stats


class Manager_Schedule(scrapy.Spider):

    """
    Spider to scrape the data related to manager stats for a particular season
    """

    name = "Manager_Schedule"

    base_url = "https://www.statbunker.com/managers/ManagersPerformance?comp_id="

    competition_ids = list(
        map(
            lambda x: (str(x[0]), str(x[1])),
            [(481, 2014), (515, 2015), (556, 2016), (586, 2017), (614, 2018)],
        )
    )

    def start_requests(self):
        for item in self.competition_ids:
            yield scrapy.Request(
                self.base_url + item[0],
                callback=self.Parse_Request,
                meta={"season": item[1]},
            )

    def Parse_Request(self, response):

        table_columns = response.xpath(
            "/html/body/div[4]/div/div/table/thead/tr/th/text()"
        ).getall()

        record_insertion = Manager_Stats()

        for table_data in response.css("table.table tbody tr"):
            matches_played = table_data.css("td:nth-child(1)::text").get()
            manager_name = table_data.css("td:nth-child(2) a p::text").get()
            club_name = table_data.css("td:nth-child(3) a img::attr(alt)").get()
            matches_won = table_data.css("td:nth-child(4)::text").get()
            matches_draw = table_data.css("td:nth-child(5)::text").get()
            matches_lost = table_data.css("td:nth-child(6)::text").get()
            goal_for = table_data.css("td:nth-child(7)::text").get()
            goal_against = table_data.css("td:nth-child(8)::text").get()
            goal_difference = table_data.css("td:nth-child(9)::text").get()
            win_percentage = (
                table_data.css("td:nth-child(10)::text").get().split("%")[0]
            )
            total_points = table_data.css("td:nth-child(11)::text").get()
            points_match = table_data.css("td:nth-child(12)::text").get()

            record_insertion["matches_played"] = matches_played
            record_insertion["manager_name"] = manager_name
            record_insertion["matches_won"] = matches_won
            record_insertion["club_name"] = club_name
            record_insertion["matches_draw"] = matches_draw
            record_insertion["matches_lost"] = matches_lost
            record_insertion["goals_for"] = goal_for
            record_insertion["goals_against"] = goal_against
            record_insertion["goal_difference"] = goal_difference
            record_insertion["win_percentage"] = win_percentage
            record_insertion["total_points"] = total_points
            record_insertion["points_match"] = points_match
            record_insertion["collection_name"] = "Manager"
            record_insertion["season"] = response.meta["season"]

            yield record_insertion
