"""
Aircraft Maintenance Reliability Analysis
Reliability Metrics Module
"""


def calculate_mtbf(total_operating_time, number_of_failures):
    """
    Calculate Mean Time Between Failures (MTBF).
    """
    if number_of_failures == 0:
        return float("inf")

    return total_operating_time / number_of_failures


def calculate_mttr(total_repair_time, number_of_repairs):
    """
    Calculate Mean Time To Repair (MTTR).
    """
    if number_of_repairs == 0:
        return 0

    return total_repair_time / number_of_repairs


def calculate_failure_rate(number_of_failures, total_operating_time):
    """
    Calculate failure rate.
    """
    if total_operating_time == 0:
        return 0

    return number_of_failures / total_operating_time


def reliability_summary(
    total_operating_time,
    number_of_failures,
    total_repair_time,
    number_of_repairs
):
    """
    Calculate the main aircraft reliability metrics.
    """

    mtbf = calculate_mtbf(
        total_operating_time,
        number_of_failures
    )

    mttr = calculate_mttr(
        total_repair_time,
        number_of_repairs
    )

    failure_rate = calculate_failure_rate(
        number_of_failures,
        total_operating_time
    )

    return {
        "MTBF": mtbf,
        "MTTR": mttr,
        "Failure Rate": failure_rate
    }
