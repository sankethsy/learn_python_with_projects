import random


def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '🌟']
    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print(" | ".join(row))


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '🌟':
            return bet * 20
    return 0


def main():
    balance = 100

    print("=" * 50)
    print("           🍒 FRUIT SLOT MACHINE 🍒")
    print("=" * 50)
    print("Symbols: 🍒  🍉  🍋  🔔  🌟")

    while balance > 0:
        print("-" * 50)
        print(f"Current Balance : ₹{balance}")

        bet = input("Enter your bet: ₹")

        if not bet.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        bet = int(bet)

        if bet <= 0:
            print("Bet must be greater than ₹0.")
            continue

        if bet > balance:
            print("Insufficient balance.")
            continue

        balance -= bet

        print("\nSpinning...\n")

        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"\n🎉 Congratulations! You won ₹{payout}.")
        else:
            print("\nBetter luck next time!")

        balance += payout

        print(f"Balance : ₹{balance}")

        if balance == 0:
            print("\nYou have no balance left.")
            break

        play_again = input("\nPlay again? (Y/N): ").upper()

        if play_again != "Y":
            break

    print("\n" + "=" * 50)
    print(f"Game Over! Final Balance: ₹{balance}")
    print("Thank you for playing!")
    print("=" * 50)


if __name__ == "__main__":
    main()