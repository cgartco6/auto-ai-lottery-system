from pipeline.fetch_data import fetch_lottery_data
from analytics.frequency_analysis import number_frequency
from models.monte_carlo_model import monte_carlo_predictions
from analytics.ranking import rank_combinations


def generate():

    df = fetch_lottery_data()

    freq = number_frequency(df)

    combos = monte_carlo_predictions(freq)

    ranked = rank_combinations(combos)

    top13 = ranked[:13]
    top6 = ranked[:6]

    return top13, top6
