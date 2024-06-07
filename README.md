# monkeyDontTyoe
```
███╗   ███╗ ██████╗ ███╗   ██╗██╗  ██╗███████╗██╗   ██╗██████╗  ██████╗ ███╗   ██╗████████╗████████╗██╗   ██╗██████╗ ███████╗
████╗ ████║██╔═══██╗████╗  ██║██║ ██╔╝██╔════╝╚██╗ ██╔╝██╔══██╗██╔═══██╗████╗  ██║╚══██╔══╝╚══██╔══╝╚██╗ ██╔╝██╔══██╗██╔════╝
██╔████╔██║██║   ██║██╔██╗ ██║█████╔╝ █████╗   ╚████╔╝ ██║  ██║██║   ██║██╔██╗ ██║   ██║      ██║    ╚████╔╝ ██████╔╝█████╗  
██║╚██╔╝██║██║   ██║██║╚██╗██║██╔═██╗ ██╔══╝    ╚██╔╝  ██║  ██║██║   ██║██║╚██╗██║   ██║      ██║     ╚██╔╝  ██╔═══╝ ██╔══╝  
██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║  ██╗███████╗   ██║   ██████╔╝╚██████╔╝██║ ╚████║   ██║      ██║      ██║   ██║     ███████╗
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝      ╚═╝      ╚═╝   ╚═╝     ╚══════╝
```                                                                                                                          

This Python script automates interactions with the Monkeytype website using Selenium. This program helps the user to gain high WPM without even typing.

## Features

- Automates typing words in the Monkeytype typing test
- Displays typing statistics (WPM, accuracy, and consistency)
- Prompts user to run the test again or exit
- Handles keyboard interruption gracefully

## Prerequisites

- Python 3.5 or above
- Google Chrome
- ChromeDriver

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ItsAbhinavM/monkeyDontType
    cd monkeyDontType
    ```

2. Create a virtual environment:
    ```
    python -m venv venv or python3 -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```
        source venv/bin/activate
        ```

4. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```
    python monkeytype_automation.py
    ```

2. The script will open a Chrome browser and navigate to the Monkeytype website. Manually accept the cookies for a better experience.

3. The script will start the typing test automatically. It will type words and display your typing statistics (WPM, accuracy, and consistency) once the test is complete.

4. After the test, you will be prompted to run the test again or exit:
    ```
    do you wish to run again (y/n) :
    ```

5. If you choose 'y', the script will click the 'Next test' button and start a new test.

6. If you choose 'n', the script will exit and close the browser.

## Code Overview

- `get_word_from_web(url, delay=0.05)`: Initializes the Chrome driver, navigates to the given URL, and starts the typing test.
- `identifyWords(driver, delay)`: Identifies and types words on the Monkeytype website.
- `endCredits(driver)`: Displays typing statistics (WPM, accuracy, consistency) and prompts the user to run the test again or exit.
- `runAgain(driver)`: Handles the user's choice to run the test again or exit.

