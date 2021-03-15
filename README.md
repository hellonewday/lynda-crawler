
**Introduction**

Lynda-Crawler is a Python - Selenium Automation Engine to crawl Lynda.com Learning Video.

**How-to-start**

Open Python file to edit, changing the downloadable videos directory (E:/), choosing some courses on lynda.com, then put it in approriate functions!

**Functions**

`download_video(url: String)`
This function helps you download a course from a course link.

`download_path(url: String)`
This function helps you download a learning path from a learning path link.

`download_courses_in_path(url: String, start: int, end: int)`
This function helps you download a range of courses in a learning path from a learning path link

`validate_filename(filename: String)`
This function is automatically set in every os built-in functions I've used, which helps you remove special characters while save it to your directory.  


