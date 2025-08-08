from season_weeks import SeasonWeeks
from game_schedule import UpcomingGames
from season_standings import SeasonStanding
from team_statistics import TeamStatistics
from ml_model import PredictionModel
import constants

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, HttpResponseServerError


# Create your views here.

def games(request: HttpRequest):
    season = SeasonWeeks()
    week_num = season.get_week_num()
    if week_num == "Table doesn't exist":
        return HttpResponseServerError()

    game_schedule = UpcomingGames()
    games_query = game_schedule.get_upcoming_weekly_games(week_num)
    if games_query == "Table doesn't exist":
        return HttpResponseServerError()
    else:
        return HttpResponse(games_query)


def standings(request):
    name = request.GET.get('name')
    if name not in constants.team_names:
        return HttpResponseBadRequest()

    team_standings = SeasonStanding()
    results = team_standings.get_team_standing(name)
    if results == "Table doesn't exist":
        return HttpResponseServerError()
    else:
        return HttpResponse(results)


def predict(request):
    name1 = request.GET.get('team')
    name2 = request.GET.get('opponent')

    if name2 not in constants.team_names or name1 not in constants.team_names:
        return HttpResponseBadRequest()

    team_statistics = TeamStatistics()
    results1 = team_statistics.get_team_stats(name1)
    if results1 == "Table doesn't exist":
        return HttpResponseServerError()
    results2 = team_statistics.get_team_stats(name2)

    model = PredictionModel
    prediction = model.model_call(results1, results2)
    return HttpResponse(prediction)


def records(request):
    name = request.GET.get('name')
    if name not in constants.team_names:
        return HttpResponseBadRequest()

    team_statistics = TeamStatistics()
    results = team_statistics.get_team_stats(name)
    if results == "Table doesn't exist":
        return HttpResponseServerError()
    else:
        return HttpResponse(results)


def home(request):
    # TODO - Import in React Application when complete
    return render(request, "predictions/home.html")