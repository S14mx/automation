import re


def read_template(file_path: str) -> str:
    try:
        with open(file_path) as sample_text:
            contents: str = sample_text.read()
            return contents
    except FileNotFoundError as e:
        raise e


def find_and_sort_emails(text: str) -> list[str]:
    emails: list[str] = re.findall("\S+@\S+", text)
    unique_emails = remove_duplicates(emails)
    unique_emails.sort()
    return unique_emails


def find_and_sort_phone_numbers(text: str) -> list[str]:

    phone_numbers: list[str] = re.findall(
        '(\d{3})?(\d{3})[-. ]*(\d{4})\S+', text)
    unique_numbers: list[tuple] = remove_duplicates(phone_numbers)
    unique_numbers.sort()
    number_list: list[str] = []
    for item in unique_numbers:
        number_list.append(list(item))

    for item in number_list:
        if item[0] == "":
            item[0] = "206"

    return ["-".join(item) for item in number_list]


def remove_duplicates(text: list[str]) -> list[str]:

    return list(dict.fromkeys(text))


def write_data_to_file(text: list[str], file_path: str):
    with open(file_path, "w") as saved_file:
        saved_file.write("\n".join(text))


if __name__ == "__main__":
    
    text_contents = read_template("assets/potential-contacts.txt")
    unique_sorted_emails = find_and_sort_emails(text_contents)
    unique_sorted_numbers = find_and_sort_phone_numbers(text_contents)
    write_data_to_file(unique_sorted_emails, "assets/emails.txt")
    write_data_to_file(unique_sorted_numbers, "assets/phone-numbers.txt")
