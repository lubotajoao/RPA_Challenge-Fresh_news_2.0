import os
import traceback


def create_folder(folder_path: str) -> str:
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        return folder_path
    except Exception as e:
        print(f'An error occurred while creating folder:\n[{e}][\n{traceback.format_exc()}]')
