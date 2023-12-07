import os
import shutil
import subprocess
import sys

from pathlib import Path

rstbConvention = "ResourceSizeTable.Product."
rstbEnding = ".rsizetable.zs"

# TODO: Can we assume that the target game
# version matches the version of the dump?
version: str = input("Enter Your Game Version: (100, 110, 111, 120, 121, etc..): ")


def get_exe_dir() -> Path:
    """
    Returns the folder that the running script is in as a `Path` object.
    """
    return Path(os.getcwd())


def prompt_for_game_path():
    """
    Prompts the user for a game path and sets a
    global variable `game_path` to the users input.

    The prompt will iterate until the path exists with the file `Pack/ZsDic.pack.zs`.
    """

    global game_path
    while not (
        (game_path := Path(input("Enter the path to the game dump: ").strip("'\"")))
        / "Pack"
        / "ZsDic.pack.zs"
    ).exists():
        print("Invalid game dump path. Please make sure the 'romfs' folder exists.")


def copy_vanilla_rstb(temp_folder) -> Path:
    """
    Copies the vanilla RESTBL file into the provided `temp_folder` and returns a `Path` object to the copied file.
    """

    vanilla_rstb_path: Path = (
        game_path / "System" / "Resource" / f"{rstbConvention}{version}{rstbEnding}"
    )
    temp_rstb_path: Path = temp_folder / f"{rstbConvention}{version}{rstbEnding}"

    shutil.copyfile(vanilla_rstb_path, temp_rstb_path)
    print(f"Copied vanilla RSTB to: {temp_rstb_path}")
    return temp_rstb_path


def merge_restbls(merged_romfs_folder, restbl_paths):
    """
    Call TotkRSTB with `--merge` to merge the `restbl_paths` into one restbl file
    """

    # Assuming the first item in restbl_paths is the vanilla RSTB
    vanilla_rstb_path: Path = restbl_paths[0]
    final_merged_rstb_path: Path = (
        merged_romfs_folder
        / "System"
        / "Resource"
        / f"Merged.Product.{version}.rsizetable.zs"
    )

    # Merge Restbls using TotkRSTB or your preferred method
    # This part should be adapted based on your specific merging process

    # Example using TotkRSTB:
    totkrstb_path: Path = get_exe_dir() / "Dependencies" / "TotkRSTB.exe"
    subprocess.run(
        [totkrstb_path, "--mergerestbl", restbl_path for restbl_path in restbl_paths]
    )

    # Rename the merged RSTB
    vanilla_rstb_path.rename(final_merged_rstb_path)


def main():
    """
    Merges the provided restbl with the vanilla restbl file for a specified game version.

    (This file is an alteration of GPTCML.py)

    #### Usage:
      `<modded_restbl> <modded_restbl_output>`
    """

    # Step 1: Prompt for Game Dump Path
    prompt_for_game_path()

    # Step 2: Create a temporary folder within the program's current working directory
    temp_folder: Path = get_exe_dir() / "tmp"
    os.makedirs(temp_folder, exist_ok=True)

    # Step 3: Copy Vanilla RSTB to Temporary Location
    temp_rstb_path = copy_vanilla_rstb(temp_folder)

    # Step 4: Create a new folder for the merged RomFS mod
    merged_romfs_folder: Path = get_exe_dir() / "merged"
    os.makedirs(merged_romfs_folder, exist_ok=True)

    print(sys.argv)

    # Step 5: Merge Restbls
    restbl_paths = [temp_rstb_path]  # Example restbl_paths
    restbl_paths.extend(sys.argv[2::])
    merge_restbls(merged_romfs_folder, restbl_paths)

    print(f"Restbls merged in: {merged_romfs_folder}")


if __name__ == "__main__":
    main()
