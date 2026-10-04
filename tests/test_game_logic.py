from logic_utils import check_guess, parse_guess

def test_parse_whole_number_guess():
    assert parse_guess("24") == (True, 24, None)

def test_parse_decimal_guess_is_rejected():
    assert parse_guess("24.9") == (False, None, "That is not a number.")

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 24 and guess is 50, the hint should be "Go LOWER!"
    result = check_guess(50, 24)
    assert result == ("Too High", "📈 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📉 Go HIGHER!")
