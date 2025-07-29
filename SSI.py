def compute_ssi(coarse, medium, fine):
    average = abs((coarse + medium + fine) / 3)
    variation = abs(medium - coarse) + abs(fine - medium)
    penalty = 0.20 if (coarse - medium) * (medium - fine) < 0 else 0

    if average == 0:
        ssi = 0.0
    else:
        ssi = 1 - (variation / average) - penalty

    if ssi < 0:
        ssi = 0.0

    if ssi < 0.0:
        classification = "Clamped to 0 (Complete Instability)"
    elif 0.0 <= ssi < 0.39:
        classification = "Unstable"
    elif 0.39 <= ssi <= 0.80:
        classification = "Nearly Stable"
    else:
        classification = "Stable"

    return round(ssi, 4), classification


if __name__ == "__main__":
    print("\n==============================")
    print("   SOLUTION STABILITY INDEX")
    print("==============================")
    print("This tool calculates the SSI (Solution Stability Index),")
    print("a dimensionless number from 0 to 1 that indicates the stability")
    print("of your simulation result across three mesh resolutions.\n")
    print("⚠️  Please enter dimensionless COEFFICIENTS (e.g., Ct, Cp, Nu), not raw values like pressure or force.\n")

    while True:
        try:
            c = float(input("Enter coarse value: "))
            m = float(input("Enter medium value: "))
            f = float(input("Enter fine value: "))
            ssi_val, ssi_class = compute_ssi(c, m, f)
            print(f"\nSSI = {ssi_val} ({ssi_class})\n")
        except ValueError:
            print("Please enter valid numeric inputs.\n")

        retry = input("Do you want to try again? (y/n): ").strip().lower()
        if retry != 'y':
            print("Exiting program.")
            break
