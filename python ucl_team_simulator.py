import random


def interactive_intro():
    print("\n🔥 Welcome to the UEFA Champions League Final 2025 Simulator! 🔥")
    print("  Get ready for an epic showdown where UCL Champions are made! 🏆\n")


# List of clubs and their mottos
clubs = {
    "Barcelona": "Visca Barça! 🔵🔴",
    "Real Madrid": "Hala Madrid! ⚪",
    "Liverpool": "You'll Never Walk Alone! 🔴",
    "Bayern Munich": "Mia San Mia! 🔴⚪",
    "Paris Saint Germain": "Ici C'est Paris! 🔵🔴",
    "Inter Milan": "Forza Inter! ⚫🔵"
}

# Tactics
strategies = [
    "Total Football",
    "Kick and Rush",
    "Catenaccio",
    "Gegenpressing",
    "Jogo Bonito",
    "Park the Bus",
    "Counter Attack",
    "High Pressing",
    "Fast Build-Up",
    "Wide Play"
]

# Weather conditions
weather_conditions = ["Sunny ☀️", "Rainy 🌧️", "Snowy ❄️", "Windy 💨"]

# Captain choices
captains = ["Experienced Leader", "Young Star", "Midfield Maestro", "Defensive Wall", "Super Striker"]


def main():
    interactive_intro()

    # Randomly assign user's team
    your_team = random.choice(list(clubs.keys()))
    print(f"Your team in the Final UCL is: {your_team} - {clubs[your_team]}\n")

    # Create list of remaining teams
    remaining_clubs = list(clubs.keys())
    remaining_clubs.remove(your_team)

    # Randomly assign opponent
    opponent_team = random.choice(remaining_clubs)
    print(f"Your opponent in the Final is: {opponent_team} - {clubs[opponent_team]}\n")

    # Choose tactics
    print("Choose your tactics:")
    for i, strategy in enumerate(strategies, 1):
        print(f"{i}. {strategy}")

    tactic_choice = int(input("Enter the number of your tactic choice: ")) - 1
    tactic = strategies[tactic_choice]
    print(f"\nYou've chosen to play with {tactic} tactics! 🎮\n")

    # Choose captain
    print("Choose your team captain:")
    for i, captain in enumerate(captains, 1):
        print(f"{i}. {captain}")
    captain_choice = int(input("Enter the number of your captain choice: ")) - 1
    chosen_captain = captains[captain_choice]
    print(f"\nYour captain is {chosen_captain}! 🏅\n")

    # Weather condition
    weather = random.choice(weather_conditions)
    print(f"The weather during the final will be: {weather}\n")

    # Choose motivation
    print("Choose your team's motivation:")
    motivations = ["High Intensity", "Stay Calm", "Relaxed Approach"]
    for i, motivation in enumerate(motivations, 1):
        print(f"{i}. {motivation}")
    motivation_choice = int(input("Enter the number of your motivation choice: ")) - 1
    chosen_motivation = motivations[motivation_choice]
    print(f"\nYour team is set with a {chosen_motivation} mindset! 💪\n")

    # Choose home or away
    position = input("Do you want to play at home or away? (home/away): ").lower()

    # Generate random scores
    home_score = random.randint(0, 5)
    away_score = random.randint(0, 5)

    print("\n⚽ MATCH RESULT ⚽")
    print("-------------------------------------")
    if position == "home":
        print(f"{your_team} {home_score} - {away_score} {opponent_team}")
        if home_score > away_score:
            print("🏆 RESULT: YOU WIN THE CHAMPIONS LEAGUE! 🎉🥇")
        elif home_score < away_score:
            print("😢 RESULT: You lost the final. Better luck next time!")
        else:
            print("🤝 RESULT: It's a draw! Let's go to penalties!")
    else:
        print(f"{opponent_team} {home_score} - {away_score} {your_team}")
        if away_score > home_score:
            print("🏆 RESULT: YOU WIN THE CHAMPIONS LEAGUE! 🎉🥇")
        elif away_score < home_score:
            print("😢 RESULT: You lost the final. Better luck next time!")
        else:
            print("🤝 RESULT: It's a draw! Let's go to penalties!")
    print("-------------------------------------")

    # If draw, penalty shootout
    if home_score == away_score:
        print("⚽ Penalty Shootout! 🔥")
        penalties_you = random.randint(2, 5)
        penalties_opponent = random.randint(2, 5)
        print(f"{your_team} (Penalties) {penalties_you} - {penalties_opponent} {opponent_team}")
        if penalties_you > penalties_opponent:
            print("🏆 RESULT: YOU WIN ON PENALTIES! 🎉🥇")
        else:
            print("😢 RESULT: You lost in the penalty shootout. So close!")


if __name__ == "__main__":
    main()
