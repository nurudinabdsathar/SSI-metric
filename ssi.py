def compute_ssi(coarse, medium, fine):
    avg = abs((coarse + medium + fine) / 3)
    R1 = medium - coarse
    R2 = fine - medium
    variation = abs(R1) + abs(R2)
    penalty = 0.25 if R1 * R2 < 0 else 0.0
    ssi = 1 - (variation / avg) - penalty
    return max(ssi, 0.0)

# Example usage
if __name__ == "__main__":
    c, m, f = 10.2, 9.8, 10.0
    result = compute_ssi(c, m, f)
    print(f"SSI = {result:.4f}")
