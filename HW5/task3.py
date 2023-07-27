names = ["Иван", "Мария", "Петр"]
bets = [1000, 1500, 800]
bonuses = ["10.25%", "5%", "15.5%"]

result_dict = {name: bet * float(bonus.strip('%')) / 100 for name, bet, bonus in zip(names, bets, bonuses)}

print(result_dict)
