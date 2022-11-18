import math


def main():
    sample = []

    with open("sample.txt", "r") as f:
        sample = f.read().splitlines()
        for i in range(len(sample)):
            sample[i] = sample[i].replace(",", ".")

            # Remove letters from the sample
            sample[i] = "".join([i for i in sample[i] if not i.isalpha()])

    print(f"Mean: {calc_mean(sample)} \nDeviation: {calc_deviation(sample)}")


def calc_deviation(sample):
    sample_sum = 0
    for i in range(len(sample)):
        sample[i] = float(sample[i])
        sample_sum += sample[i]

    mean = sample_sum / len(sample)

    deviation = 0
    for i in range(len(sample)):
        deviation += (sample[i] - mean) ** 2

    return round(math.sqrt(deviation / len(sample)), 5)


def calc_mean(sample):
    sample_sum = 0
    for i in range(len(sample)):
        sample[i] = float(sample[i])
        sample_sum += sample[i]

    return round(sample_sum / len(sample), 5)


if __name__ == "__main__":
    main()
