import os
import logging
from collections import namedtuple
from pathlib import Path

logging.basicConfig(filename='file_info.log', level=logging.INFO, encoding="utf-8")

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent_dir'])


def get_file_info(path):
    path = Path(path)

    if not path.exists():
        logging.error(f'Путь "{path}" не найден!.')
        return

    for item in path.iterdir():
        is_dir = item.is_dir()
        name = item.stem if not is_dir else item.name
        extension = item.suffix if not is_dir else ''
        parent_dir = path.name

        file_info = FileInfo(name, extension, is_dir, parent_dir)

        logging.info(
            f'Имя файла без расширения: {file_info.name}\n Расширение файла: {file_info.extension}\n Флаг каталога: {file_info.is_dir}\n Название родительского каталога: {file_info.parent_dir}\n-------------------------------------------------')


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Ипользовать в командом строке: python script.py <Укажите путь к папке>")
        sys.exit(1)

    directory_path = sys.argv[1]
    get_file_info(directory_path)
