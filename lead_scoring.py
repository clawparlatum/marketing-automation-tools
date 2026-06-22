def calculate_score(opened_email, clicked_link, purchased):
    score = 0

    if opened_email:
        score += 10

    if clicked_link:
        score += 25

    if purchased:
        score += 100

    return score


print(calculate_score(True, True, False))
