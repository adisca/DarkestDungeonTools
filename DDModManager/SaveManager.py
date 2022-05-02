import os
import subprocess

from pathlib import Path


class SaveFileManager:
    def __init__(self, save_editor_path, saves_location, profile_nb):
        if profile_nb < 0 or profile_nb > 9:
            raise ValueError("Profile number out of bounds")
        else:
            self.SaveEditorPath = save_editor_path
            self.ProfileNb = profile_nb
            self.SaveProfilePath = Path(saves_location, f"profile_{profile_nb}")

    def swap_profile(self, profile_nb):
        if profile_nb < 0 or profile_nb > 9:
            raise ValueError("Profile number out of bounds")
        else:
            self.ProfileNb = profile_nb
            self.SaveProfilePath = Path(self.SaveProfilePath.parent, f"profile_{profile_nb}")

    def decrypt_save_info(self, file):
        output = f"temp/{file}"
        if not os.path.exists(Path(f'{self.SaveProfilePath}/{file}')):
            print(f"{file} doesn't exist encrypted")
            return None
        else:
            subprocess.call(['java', '-jar', Path(f'{self.SaveEditorPath}/DDSaveEditor.jar'), 'decode',
                             '-o', output, Path(f'{self.SaveProfilePath}/{file}')])
            print(f'decrypted {file}!')
            return output

    def encrypt_save_info(self, file):
        if not os.path.exists(f"temp/{file}"):
            print(f"{file} doesn't exist decrypted")
        else:
            debug = ['java', '-jar', Path(f'{self.SaveEditorPath}/DDSaveEditor.jar'), 'encode',
                             '-o', Path(f'{self.SaveProfilePath}/{file}'), f"temp/{file}"]
            subprocess.call(['java', '-jar', Path(f'{self.SaveEditorPath}/DDSaveEditor.jar'), 'encode',
                             '-o', Path(f'{self.SaveProfilePath}/{file}'), f"temp/{file}"])
            print(f'encrypted {file}!')
