lottery_number = int(input("Enter a two-digit lottery number: "))

if 10 <= lottery_number <= 99:
    user_number = int(input("Enter your two-digit guess: "))

    lottery_digit1 = lottery_number // 10
    lottery_digit2 = lottery_number % 10

    user_digit1 = user_number // 10
    user_digit2 = user_number % 10

    if user_number == lottery_number:
        print(f"Exact match! You win Rs.10,000. Lottery number: {lottery_number}")
    elif user_digit1 == lottery_digit2:
        if user_digit2 == lottery_digit1:
            print(f"Matched all digits! You win Rs.3,000. Lottery number: {lottery_number}")
        else:
            print(f"One digit matched! You win Rs.1,000. Lottery number: {lottery_number}")
    elif user_digit2 == lottery_digit1:
        print(f"One digit matched! You win Rs.1,000. Lottery number: {lottery_number}")
    elif user_digit1 == lottery_digit1:
        print(f"One digit matched! You win Rs.1,000. Lottery number: {lottery_number}")
    elif user_digit2 == lottery_digit2:
        print(f"One digit matched! You win Rs.1,000. Lottery number: {lottery_number}")
    else:
        print(f"Sorry, no match. Lottery number was: {lottery_number}")
else:
    print("Please enter a valid two-digit number.")