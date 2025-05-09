import os


working_directory = os.getcwd()


def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file_path = os.path.join(working_directory, data_file_name)
    data_file_path_report = os.path.join(working_directory, report_file_name)

    report_source = open(data_file_path)
    report_formatted = {}

    for line in report_source:
        if "," in line:
            key, value = line.split(",")
            report_formatted[key] = int(value) + report_formatted.get(key, 0)
    report_source.close()

    report_formatted["result"] = (
        report_formatted["supply"] - report_formatted["buy"]
    )

    report = open(data_file_path_report, "x")

    supply = report_formatted["supply"]
    buy = report_formatted["buy"]
    result = report_formatted["result"]

    report.writelines(
        [
            f"supply,{supply}\n",
            f"buy,{buy}\n",
            f"result,{result}\n",
        ]
    )
    report.close()
