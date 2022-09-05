import os
import subprocess

def run():
    try:
        assert os.environ["VIRTUAL_ENV"].endswith("ex02/bteak")
        subprocess.call(["pip", "install", "beautifulsoup4", "pytest"])
        freeze = subprocess.check_output(["pip", "freeze"]).decode("utf-8")
        print(freeze, end="")
        with open("requirements.txt", "w") as file:
            file.write(freeze)

    except Exception as e:
        print(f"Error caught! {e}")


if __name__ == "__main__":
    run()