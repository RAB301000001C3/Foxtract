# Foxtract.exe 

![foxtract](https://user-images.githubusercontent.com/85085158/227180996-764b77d3-f620-4a82-aada-d0eadc7e1c1d.png)

# Foxtract.py

![foxtract2](https://user-images.githubusercontent.com/85085158/227181028-fc56eaf8-02c6-4d52-a659-69b42cc2e639.png)


# Foxtract

Foxtract is a Python-based tool that extracts the browsing history from Mozilla Firefox's places.sqlite database using SQLite. It displays the URL, visit count, and last visit date of the current user to the URL.

# Usage

For Windows:
Foxtract.exe -f <places.sqlite> [--format]

1. Download the tool as a zip file and extract it to your desired directory.
2. Open the command prompt as an administrator.
3. Navigate to the directory where the tool was extracted using the "cd" command.
4. Run the ".\Setup.bat" script to install any required dependencies.
5. Once the setup is complete, you can use the tool with the following command:

For Linux:
python3 Foxtract.py -f <places.sqlite> [--format]

Note: If you are running the Windows executable on Linux, you can use Wine to run the tool.

The tool will extract the Mozilla Firefox browser history from the supplied "places.sqlite" file and display the URL, visit count, and last visit date of the current user to the URL. You can use the optional "--format" parameter for human-readable output.

# Compatibility

Foxtract is compatible with Windows. For Linux, use the raw Foxtract.py file that requires Python3 to run, or use Wine to run the Foxtract.exe file.

# License 

Foxtract is made for fun automation tool and free to use without restriction.

# Disclaimer

Foxtract is provided "as is" without warranty of any kind, express or implied. Use at your own risk.
