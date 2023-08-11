import csv
import pickle
from pathlib import Path


def conv_to_csv(file_name: Path) -> None:
    with (open(file_name, 'rb') as f_pickle,
          open(f'{file_name.stem}.csv', "w", newline='', encoding='utf-8') as f_csv):
        new_dict = pickle.load(f_pickle)

        csv_write = csv.DictWriter(
            f_csv,
            fieldnames=list(new_dict.keys()),
            dialect='excel',
            delimiter=',',
            quoting=csv.QUOTE_NONNUMERIC)

        csv_write.writeheader()
        csv_write.writerows([new_dict])


if __name__ == "__main__":
    conv_to_csv(Path("new_user.pickle"))
