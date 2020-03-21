# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class LeagueTable(Item):
    # Model for League Table(Standing Per Season Per Team)

    league_standing = Field()
    team_name = Field()
    team_link = Field()
    total_matches = Field()
    wins = Field()
    loss = Field()
    draw = Field()
    goals_scored = Field()
    goals_conceded = Field()
    plus_minus = Field()
    Points = Field()
    club_id = Field()
    season = Field()
    collection_name = Field()


class CompetitionRecord(Item):
    # Model for Competition Table(Participation Per Competiotion Per Season Per Team)

    match_type = Field()
    match_date = Field()
    match_time = Field()
    home_team = Field()
    away_team = Field()
    play_style = Field()
    coach = Field()
    result = Field()
    home_score = Field()
    away_score = Field()
    match_result_link = Field()
    club_id = Field()
    season = Field()
    club_name = Field()
    competition_name = Field()
    collection_name = Field()


class Manager_Stats(Item):
    # Model for Manager Stats Per Season Per Team
    matches_played = Field()
    manager_name = Field()
    club_name = Field()
    matches_won = Field()
    matches_draw = Field()
    matches_lost = Field()
    goals_for = Field()
    goals_against = Field()
    goal_difference = Field()
    win_percentage = Field()
    total_points = Field()
    points_match = Field()
    collection_name = Field()
    season = Field()

