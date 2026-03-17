TAX_RATE_MULTIPLIER = 1.15
LOG_FILE_PATH = "log.txt"
TOTAL_MESSAGE_TEMPLATE = "Total: {amount:.2f}"


def calculate_total_amount(amount):
    return amount * TAX_RATE_MULTIPLIER


def format_total_message(total_amount):
    return TOTAL_MESSAGE_TEMPLATE.format(amount=total_amount)


def print_total(total_amount):
    print(format_total_message(total_amount))


def append_results_to_log(results, log_file_path=LOG_FILE_PATH):
    with open(log_file_path, "a") as log_file:
        log_file.write(str(results) + "\n")


def process_data(data):
    calculated_totals = []
    for amount in data:
        total_amount = calculate_total_amount(amount)
        print_total(total_amount)
        calculated_totals.append(total_amount)

    append_results_to_log(calculated_totals)
    return calculated_totals
