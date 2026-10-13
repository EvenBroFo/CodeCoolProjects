from cows_and_bulls import CowsAndBulls


def test_initial_state():
    game = CowsAndBulls()

    assert game.state == "ongoing"
    assert game.guess_count == 0


def test_random_number():
    game = CowsAndBulls()

    assert len(game.target) == 4
    assert game.target.isdigit()
    assert 1000 <= int(game.target) <= 9999

def test_cows_and_bulls():
    game = CowsAndBulls()
    game.target = "7624"

    result = game.guess("7296")

    assert result == "1 cow, 2 bulls"
    assert game.guess_count == 1

def test_winning_game():
    game = CowsAndBulls()
    game.target = "1234"

    result = game.guess("1234")

    assert result == "4 cows, 0 bulls"
    assert game.state == "finished"
    assert game.guess_count == 1