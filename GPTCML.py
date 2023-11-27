import os
import shutil
import subprocess

rstbConvention = "ResourceSizeTable.Product."
rstbEnding = ".rsizetable.zs"

version = input("Enter Your Game Version: (100, 110, 111, 120, 121, etc..): ")

def prompt_for_game_dump_path():
    while True:
        game_dump_path = input("Enter the path to the game dump: ").strip('\'"')
        game_dump_path = os.path.abspath(game_dump_path)

        romfs_path = os.path.join(game_dump_path)
        if os.path.exists(romfs_path):
            return romfs_path
        else:
            print("Invalid game dump path. Please make sure the 'romfs' folder exists.")

def copy_vanilla_rstb(game_dump_path, temp_folder):
    vanilla_rstb_path = os.path.join(game_dump_path, 'System', 'Resource', f'{rstbConvention}{version}{rstbEnding}')
    temp_rstb_path = os.path.join(temp_folder, f'{rstbConvention}{version}{rstbEnding}')

    shutil.copy2(vanilla_rstb_path, temp_rstb_path)
    print(f"Copied vanilla RSTB to: {temp_rstb_path}")
    return temp_rstb_path

def merge_restbls(merged_romfs_folder, restbl_paths):
    vanilla_rstb_path = restbl_paths[0][0]  # Assuming the first item in restbl_paths is the vanilla RSTB
    final_merged_rstb_path = os.path.join(merged_romfs_folder, 'System', 'Resource', f'Merged.Product.{version}.rsizetable.zs')

    # Merge Restbls using TotkRSTB or your preferred method
    # This part should be adapted based on your specific merging process

    # Example using TotkRSTB:
    totkrstb_path = os.path.join(os.getcwd(), 'Dependencies', 'TotkRSTB.exe')
    subprocess.run([totkrstb_path, '--mergerestbl', vanilla_rstb_path] + [restbl_path[0] for restbl_path in restbl_paths[1:]])

    # Rename the merged RSTB
    os.rename(vanilla_rstb_path, final_merged_rstb_path)

def main():
    # Step 1: Prompt for Game Dump Path
    game_dump_path = prompt_for_game_dump_path()

    # Step 2: Create a temporary folder within the program's current working directory
    temp_folder = os.path.join(os.getcwd(), 'temp')
    os.makedirs(temp_folder, exist_ok=True)

    # Step 3: Copy Vanilla RSTB to Temporary Location
    temp_rstb_path = copy_vanilla_rstb(game_dump_path, temp_folder)

    # Step 4: Create a new folder for the merged ROMFS
    merged_romfs_folder = os.path.join(os.getcwd(), 'Merged RomFS')
    os.makedirs(merged_romfs_folder, exist_ok=True)

    # Step 5: Merge Restbls
    restbl_paths = [(index,) for index in range(1, 10)]  # Example restbl_paths
    merge_restbls(merged_romfs_folder, restbl_paths)

    print(f"Restbls merged in: {merged_romfs_folder}")

if __name__ == "__main__":
    main()
